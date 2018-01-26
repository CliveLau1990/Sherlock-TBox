#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Copyright (C) 2015-2018 Shenzhen Auto-link world Information Technology Co., Ltd.
  All Rights Reserved

  Name: MqttComm.py
  Purpose:

  Created By:    Clive Lau <liuxusheng@auto-link.com.cn>
  Created Date:  2018-01-11

  Changelog:
  Date         Desc
  2018-01-11   Created by Clive Lau
"""

# Builtin libraries
import time
import threading

# Third-party libraries
from robot.api import logger
import paho.mqtt.client as mqtt

# Customized libraries
from Protobuf import tbox_pb2
from MqttDump import MqttDump
from CanComm.CanProtoDFSK import EnumDoorStatus
from CanComm.CanProtoDFSK import EnumLockStatus
from CanComm.CanProtoDFSK import EnumHandbrakeStatus
from CanComm.CanProtoDFSK import EnumAcOnOffStatus
from CanComm.CanProtoDFSK import EnumEmsEngineStatus
from CanComm.CanProtoDFSK import EnumWiperStatus
from CanComm.CanProtoDFSK import EnumGearPos


# MQTT Server Settings
MQTT_MAJOR_SERVER = "test.mosquitto.org"
# MQTT_MINOR_SERVER = "14.21.42.158"
MQTT_MINOR_SERVER = "192.168.3.8"
MQTT_MAJOR_ENCRYPTION = "Encryption/mosquitto.org.crt"
MQTT_MINOR_ENCRYPTION = "Encryption/autolink_tbox.crt"
MQTT_SERVER_PORT = 8883
MQTT_USER = ""
MQTT_PWD = ""

# MQTT Topic Settings
MQTT_WILL_TOPIC = "all/will"
MQTT_REPORT_TOPIC = "device/gate/report"
MQTT_BUSINESS_TOPIC = "device/gate/business"
MQTT_DEVICE_TOPIC_PREFIX = "gate/per/device/"
MQTT_DEVICE_TOPIC_SUFFIX = "/order"


class MqttComm(object):
    """"""

    IPADDRS = {'mosquitto.org': 'test.mosquitto.org', 'auto-link.com.cn': '192.168.3.8'}

    def __init__(self, expected_device, server):
        # LogTag
        self._tag = self.__class__.__name__ + ' '
        logger.info(self._tag + "__init__ called")
        # Message head parameter
        self._protocol_version = 0
        self._equipment_id_type = tbox_pb2.PDID
        self._msg_id = 1
        self._token = "token-" + expected_device
        # MQTT parameter
        self._mqttc = None
        self._expected_device = expected_device
        self._server = MqttComm.IPADDRS[server]
        self._is_connected = False
        self._msgtop = None
        self._handle_topic_dict = {
            MQTT_WILL_TOPIC:     self.__handle_topic_will,
            MQTT_REPORT_TOPIC:   self.__handle_topic_report,
            MQTT_BUSINESS_TOPIC: self.__handle_topic_business,
        }
        self._handle_report_dict = {
            tbox_pb2.DATAMINING:     self.__on_response_datamining,
            tbox_pb2.VEHICLE_STATUS: self.__on_response_vehicle,
        }
        self._handle_business_dict = {
            tbox_pb2.LOGIN:                self.__on_response_login,
            tbox_pb2.REMOTE_CONFIG_RESULT: self.__on_response_remote_config,
        }
        # Sync parameter
        self._event = threading.Event()
        self._result = False
        # Threading parameter
        self._parse_thread = None
        # CAN msg parameter
        self._can_msg_type = None
        self._can_config_item = None
        self._can_config_data = None

    def __del__(self):
        logger.info(self._tag + "__del__ called")

    def on_create(self):
        logger.info(self._tag + "on_create called")
        # MsgTop
        self._msgtop = tbox_pb2.MsgTop()
        # MQTT onCreate
        self._mqttc = mqtt.Client()
        encryption = MQTT_MAJOR_ENCRYPTION if self._server == MQTT_MAJOR_SERVER else MQTT_MINOR_ENCRYPTION
        if encryption != '':
            try:
                self._mqttc.tls_set(encryption)
                self._mqttc.tls_insecure_set(True)
            except Exception, e:
                logger.error(self._tag + "Exception on set MQTT TLS: " + str(e))
        if MQTT_USER != '':
            self._mqttc.username_pw_set(MQTT_USER, MQTT_PWD)
        self._mqttc.on_connect = self.__on_connect
        self._mqttc.on_message = self.__on_message
        try:
            self._mqttc.connect(self._server, MQTT_SERVER_PORT)
            self._mqttc.loop_start()
        except Exception, e:
            logger.error(self._tag + "Exception on connect MQTT Server: " + str(e))
            return False
        return True

    def on_destroy(self):
        logger.info(self._tag + "on_destroy called")
        # MQTT onDestroy
        if self._mqttc is None:
            return
        self._mqttc.unsubscribe(MQTT_WILL_TOPIC)
        self._mqttc.unsubscribe(MQTT_REPORT_TOPIC)
        self._mqttc.unsubscribe(MQTT_BUSINESS_TOPIC)
        self._mqttc.loop_stop(True)
        self._mqttc.disconnect()

    @property
    def is_connected(self):
        logger.console(self._tag + "is connected: " + str(self._is_connected))
        return self._is_connected

    def __on_connect(self, client, userdata, flags, rc):
        logger.console(self._tag + "Connected with result:" + mqtt.connack_string(rc))
        client.subscribe(MQTT_WILL_TOPIC, qos=1)
        client.subscribe(MQTT_REPORT_TOPIC, qos=1)
        client.subscribe(MQTT_BUSINESS_TOPIC, qos=1)

    def __on_message(self, client, userdata, msg):
        logger.console(self._tag + "=====================New Message=====================")
        self._parse_thread = threading.Thread(target=self.__parse_thread, args=(client, userdata, msg,), name='on_parse')
        self._parse_thread.daemon = True
        self._parse_thread.start()
        self._parse_thread.join()

    def __parse_thread(self, client, userdata, msg):
        logger.console((self._tag + "__parse_thread called"))
        self._handle_topic_dict[msg.topic](client, userdata, msg)

    def __handle_topic_will(self, client, userdata, msg):
        logger.console(self._tag + "__handle_topic_will called")
        logger.console(self._tag + msg.payload)
        if self._expected_device == msg.payload:
            logger.warn("Entry WILL Topic: " + msg.payload)
            self._is_connected = False

    def __handle_topic_report(self, client, userdata, msg):
        logger.console(self._tag + "__handle_topic_report called")
        msgtop = tbox_pb2.MsgTop()
        msgtop.ParseFromString(msg.payload)
        if self.__is_valid_device(msgtop):
            # set parameter
            if not self._is_connected:
                self._protocol_version = msgtop.message_head.protocol_version
                self._equipment_id_type = msgtop.message_head.equipment_id_type
                self._msg_id = msgtop.message_head.message_id
                self._token = "token-" + self._expected_device
                self._is_connected = True
            MqttDump.dump(msgtop)
            handle = self._handle_report_dict.get(msgtop.message_head.msg_type, None)
            if handle is not None:
                handle(client, userdata, msgtop)

    def __handle_topic_business(self, client, userdata, msg):
        logger.console(self._tag + "__handle_topic_business called")
        msgtop = tbox_pb2.MsgTop()
        msgtop.ParseFromString(msg.payload)
        if self.__is_valid_device(msgtop):
            # set parameter
            if not self._is_connected:
                self._protocol_version = msgtop.message_head.protocol_version
                self._equipment_id_type = msgtop.message_head.equipment_id_type
                self._msg_id = msgtop.message_head.message_id
                self._token = "token-" + self._expected_device
                self._is_connected = True
            MqttDump.dump(msgtop)
            handle = self._handle_business_dict.get(msgtop.message_head.msg_type, None)
            if handle is not None:
                handle(client, userdata, msgtop)

    def __on_response_datamining(self, client, userdata, msgtop):
        self._msgtop.datamining.CopyFrom(msgtop.datamining)

    def __on_response_vehicle(self, client, userdata, msgtop):
        self._msgtop.vehicle_status.CopyFrom(msgtop.vehicle_status)

    def __inc_msg_id(self):
        self._msg_id = (self._msg_id + 1) % 0xFFFF
        if self._msg_id == 0:
            self._msg_id = 1
        return self._msg_id

    def __is_valid_device(self, msgtop):
        logger.info(self._tag + "__is_valid_device called, DevId:" + msgtop.message_head.equipment_id)
        return msgtop.message_head.equipment_id == self._expected_device

    def __fill_message_head(self, msgtop, msg_id, msg_type, flag=False):
        msgtop.message_head.protocol_version = self._protocol_version
        msgtop.message_head.equipment_id_type = self._equipment_id_type
        msgtop.message_head.equipment_id = self._expected_device
        msgtop.message_head.message_id = msg_id
        msgtop.message_head.msg_type = msg_type
        msgtop.message_head.message_create_time = int(time.time())
        msgtop.message_head.token = self._token
        msgtop.message_head.flag = flag

    def __on_response_login(self, client, userdata, msgtop):
        """ on_response_login """
        logger.console(self._tag + "on_response_login called")
        # set parameter
        if not self._is_connected:
            self._protocol_version = msgtop.message_head.protocol_version
            self._equipment_id_type = msgtop.message_head.equipment_id_type
            self._msg_id = msgtop.message_head.message_id
            self._token = "token-" + self._expected_device
            self._is_connected = True
        publish_msg = tbox_pb2.MsgTop()
        # message_head
        self.__fill_message_head(publish_msg, self._msg_id, tbox_pb2.LOGIN_RESPONSE)
        # login_response
        publish_msg.login_response.ack_code.ack_code = tbox_pb2.SUCCESS
        publish_msg.login_response.ack_code.code_desp = "Succeed to login"
        publish_msg.login_response.token = self._token
        # publish
        client.publish(MQTT_DEVICE_TOPIC_PREFIX + self._expected_device + MQTT_DEVICE_TOPIC_SUFFIX,
                       publish_msg.SerializeToString())
        logger.console(self._tag + "on_response_login done")

    def __set_remote_config_item(self, msgtop, item, data):
        if item == tbox_pb2.MQTT_SERVER_ADDR:
            msgtop.remote_config_request.config_data.mqtt_server_addr = data
        elif item == tbox_pb2.MQTT_SERVER_TOPIC:
            msgtop.remote_config_request.config_data.mqtt_server_topic = data
        elif item == tbox_pb2.MQTT_KEY_BUSINESS_SERVER_ADDR:
            msgtop.remote_config_request.config_data.mqtt_key_business_server_addr = data
        elif item == tbox_pb2.MQTT_KEY_BUSINESS_SERVER_TOPIC:
            msgtop.remote_config_request.config_data.mqtt_key_business_server_topic = data
        elif item == tbox_pb2.ECALL_NUMBER:
            msgtop.remote_config_request.config_data.ecall_number = data
        elif item == tbox_pb2.BCALL_NUMBER:
            msgtop.remote_config_request.config_data.bcall_number = data
        elif item == tbox_pb2.ICALL_NUMBER:
            msgtop.remote_config_request.config_data.icall_number = data
        elif item == tbox_pb2.ECALL_ENABLE:
            msgtop.remote_config_request.config_data.ecall_enable = True if data.lower() == 'true' else False
        elif item == tbox_pb2.BCALL_ENABLE:
            msgtop.remote_config_request.config_data.bcall_enable = True if data.lower() == 'true' else False
        elif item == tbox_pb2.ICALL_ENABLE:
            msgtop.remote_config_request.config_data.icall_enable = True if data.lower() == 'true' else False
        elif item == tbox_pb2.SMS_GATE_NUMBER_UPLOAD:
            msgtop.remote_config_request.config_data.sms_gate_number_upload = data
        elif item == tbox_pb2.SMS_GATE_NUMBER_DOWNLOAD:
            msgtop.remote_config_request.config_data.sms_gate_number_download = data
        elif item == tbox_pb2.DATAMINING_UPLOAD_FREQUENCY:
            msgtop.remote_config_request.config_data.datamining_upload_frequency = int(data)
        elif item == tbox_pb2.VEHICLE_STATUS_UPLOAD_FREQUENCY:
            msgtop.remote_config_request.config_data.vehicle_status_upload_frequency = int(data)
        elif item == tbox_pb2.IGNITION_BLOWOUT_UPLOAD_ENABLE:
            msgtop.remote_config_request.config_data.ignition_blowout_upload_enable = True if data.lower() == 'true' else False
        elif item == tbox_pb2.UPLOAD_ALERT_ENABLE:
            msgtop.remote_config_request.config_data.upload_alert_enable = True if data.lower() == 'true' else False
        elif item == tbox_pb2.SVT_ENABLE:
            msgtop.remote_config_request.config_data.svt_enable = True if data.lower() == 'true' else False
        elif item == tbox_pb2.ELETRONIC_DEFENSE_ENABLE:
            msgtop.remote_config_request.config_data.eletronic_defense_enable = True if data.lower() == 'true' else False
        elif item == tbox_pb2.ABNORMAL_MOVE_THRESHOLD_VALUE:
            msgtop.remote_config_request.config_data.abnormal_move_threshold_value = True if data.lower() == 'true' else False
        else:
            logger.error(self._tag + "Invalid RemoteConfigItem")

    def __on_response_remote_config(self, client, userdata, msgtop):
        """ on_response_remote_config """
        logger.console(self._tag + "on_response_remote_config called")
        if self._msg_id != msgtop.message_head.message_id:
            logger.warn(self._tag + "on_response_remote_config: Not expected msg_id")
            return
        if msgtop.HasField("remote_config_result"):
            # TODO: Handle receive mulit-config_items
            for config in msgtop.remote_config_result.config_results:
                self._result = config.result
            self._event.set()

    def on_request_remote_config(self, item, data, timeout):
        """
        """
        logger.info(self._tag + "on_request_remote_config called")
        convert_config_item_dict = {
            'MQTT_SERVER_ADDR':                tbox_pb2.MQTT_SERVER_ADDR,
            'MQTT_SERVER_TOPIC':               tbox_pb2.MQTT_SERVER_TOPIC,
            'MQTT_KEY_BUSINESS_SERVER_ADDR':   tbox_pb2.MQTT_KEY_BUSINESS_SERVER_ADDR,
            'MQTT_KEY_BUSINESS_SERVER_TOPIC':  tbox_pb2.MQTT_KEY_BUSINESS_SERVER_TOPIC,
            'ECALL_NUMBER':                    tbox_pb2.ECALL_NUMBER,
            'BCALL_NUMBER':                    tbox_pb2.BCALL_NUMBER,
            'ICALL_NUMBER':                    tbox_pb2.ICALL_NUMBER,
            'ECALL_ENABLE':                    tbox_pb2.ECALL_ENABLE,
            'BCALL_ENABLE':                    tbox_pb2.BCALL_ENABLE,
            'ICALL_ENABLE':                    tbox_pb2.ICALL_ENABLE,
            'SMS_GATE_NUMBER_UPLOAD':          tbox_pb2.SMS_GATE_NUMBER_UPLOAD,
            'SMS_GATE_NUMBER_DOWNLOAD':        tbox_pb2.SMS_GATE_NUMBER_DOWNLOAD,
            'DATAMINING_UPLOAD_FREQUENCY':     tbox_pb2.DATAMINING_UPLOAD_FREQUENCY,
            'VEHICLE_STATUS_UPLOAD_FREQUENCY': tbox_pb2.VEHICLE_STATUS_UPLOAD_FREQUENCY,
            'IGNITION_BLOWOUT_UPLOAD_ENABLE':  tbox_pb2.IGNITION_BLOWOUT_UPLOAD_ENABLE,
            'UPLOAD_ALERT_ENABLE':             tbox_pb2.UPLOAD_ALERT_ENABLE,
            'DATAMING_ENABLE':                 tbox_pb2.DATAMING_ENABLE,
            'SVT_ENABLE':                      tbox_pb2.SVT_ENABLE,
            'ELETRONIC_DEFENSE_ENABLE':        tbox_pb2.ELETRONIC_DEFENSE_ENABLE,
            'ABNORMAL_MOVE_THRESHOLD_VALUE':   tbox_pb2.ABNORMAL_MOVE_THRESHOLD_VALUE,
        }
        config_item = convert_config_item_dict[item]
        self._result = False
        publish_msg = tbox_pb2.MsgTop()
        # message_head
        self.__fill_message_head(publish_msg, self.__inc_msg_id(), tbox_pb2.REMOTE_CONFIG_REQUEST)
        # remote_config_request
        publish_msg.remote_config_request.config_items.append(config_item)
        self.__set_remote_config_item(publish_msg, config_item, data)
        # publish
        self._mqttc.publish(MQTT_DEVICE_TOPIC_PREFIX + self._expected_device + MQTT_DEVICE_TOPIC_SUFFIX, publish_msg.SerializeToString())
        MqttDump.dump(publish_msg, logger.info)
        # wait_event
        self._event.wait(int(timeout))
        if not self._event.isSet() or not self._result:
            logger.error(self._tag + "Exception on remote_config_request: Timeout to wait event")
        self._event.clear()
        return self._result

    def on_request_can_data(self, item, timeout):
        """
        """
        logger.info(self._tag + "on_request_can_data called")
        data_dict = {
            'ENGINE_SPEED':       self._msgtop.datamining.engine_speed,
            'DRIVER_DOOR_STS':    EnumDoorStatus.Open.name if self._msgtop.vehicle_status.lf_door_status == tbox_pb2.ONOFF_STATE_ON else EnumDoorStatus.Close.name,
            'PASSENGER_DOOR_STS': EnumDoorStatus.Open.name if self._msgtop.vehicle_status.rf_door_status == tbox_pb2.ONOFF_STATE_ON else EnumDoorStatus.Close.name,
            'LEFTREAR_DOOR_STS':  EnumDoorStatus.Open.name if self._msgtop.vehicle_status.lr_door_status == tbox_pb2.ONOFF_STATE_ON else EnumDoorStatus.Close.name,
            'RIGHTREAR_DOOR_STS': EnumDoorStatus.Open.name if self._msgtop.vehicle_status.rr_door_status == tbox_pb2.ONOFF_STATE_ON else EnumDoorStatus.Close.name,
            'TAILGATE_STS':       EnumDoorStatus.Open.name if self._msgtop.vehicle_status.trunk_door_status == tbox_pb2.ONOFF_STATE_ON else EnumDoorStatus.Close.name,
            'DRIVER_DOOR_LOCK_STS': EnumLockStatus.Locked.name if self._msgtop.vehicle_status.lock_status == tbox_pb2.ONOFF_STATE_ON else EnumLockStatus.Unlock.name,
            'HANDBRAKE_SIGNAL':   EnumHandbrakeStatus.Up.name if self._msgtop.vehicle_status.hand_break_status == tbox_pb2.ONOFF_STATE_ON else EnumHandbrakeStatus.Down.name,
            'AC_STS':             EnumAcOnOffStatus.On.name if self._msgtop.vehicle_status.air_condition_status == tbox_pb2.ONOFF_STATE_ON else EnumAcOnOffStatus.Off.name,
            'FRONT_DEFROST_STS':  EnumAcOnOffStatus.On.name if self._msgtop.vehicle_status.air_condition_defrost_status == tbox_pb2.ONOFF_STATE_ON else EnumAcOnOffStatus.Off.name,
            'REAR_DEFROST_STS':   EnumAcOnOffStatus.On.name if self._msgtop.vehicle_status.air_condition_rear_defrost_status == tbox_pb2.ONOFF_STATE_ON else EnumAcOnOffStatus.Off.name,
            'AC_TEMPERATURE':     str(self._msgtop.vehicle_status.air_condition_temperature),
            'ENGINE_STS':         EnumEmsEngineStatus.KeyOff.name if self._msgtop.vehicle_status.engine_status == tbox_pb2.ENGINESTATE_UNKNOWN else EnumEmsEngineStatus(self._msgtop.vehicle_status.engine_status - 1).name,
            'WIPER_STS':          ('On' if self._msgtop.vehicle_status.wiper_Status == tbox_pb2.ONOFF_STATE_ON else 'Off'),
            'GEAR_STS':           EnumGearPos.S.name if self._msgtop.vehicle_status.gear_position == tbox_pb2.GEAR_S else EnumGearPos(self._msgtop.vehicle_status.gear_position).name,
        }
        return data_dict[item]


if __name__ == '__main__':
    pass
