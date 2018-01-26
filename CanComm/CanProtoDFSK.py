#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Copyright (C) 2015-2017 Shenzhen Auto-link world Information Technology Co., Ltd.
  All Rights Reserved

  Name: CanProtoDFSK.py
  Purpose:

  Created By:    Clive Lau <liuxusheng@auto-link.com.cn>
  Created Date:  2017-12-28

  Changelog:
  Date         Desc
  2017-12-28   Created by Clive Lau
"""

# Builtin libraries

# Third-party libraries

# Customized libraries
from CanMsgBasic import *


@unique
class EnumValidInvalidStatus(Enum):
    Valid = 0
    Invalid = 1


class Ems302(CanMsgBasic):
    """ 发动机管理系统 """
    def __init__(self):
        super(Ems302, self).__init__('EMS_302',
                                     EnumMsgType.Normal,
                                     0x302,
                                     EnumMsgTransmitType.Cycle,
                                     EnumMsgSignalType.Cycle,
                                     100,
                                     8,
                                     ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # 发动机转速故障
        self.__engine_speed_error = 0
        # 节气门位置故障
        self.__throttle_position_error = 0
        # 加速踏板故障
        self.__acc_pedal_error = 0
        # 发动机转速
        self.__engine_speed = 0
        # 发动机节气门位置
        self.__engine_throttle_position = 0
        # 加速踏板位置
        self.__acc_pedal = 0

    @property
    def engine_speed_error(self):
        """ 发动机转速故障 """
        return self.__engine_speed_error

    @engine_speed_error.setter
    def engine_speed_error(self, status):
        """ 发动机转速故障 """
        try:
            if status not in EnumValidInvalidStatus:
                raise AttributeError
            self.__engine_speed_error = status.value
        except AttributeError:
            print("AttributeError on engine_speed_error")

    @property
    def throttle_position_error(self):
        """ 节气门位置故障 """
        return self.__throttle_position_error

    @throttle_position_error.setter
    def throttle_position_error(self, status):
        """ 节气门位置故障 """
        try:
            if status not in EnumValidInvalidStatus:
                raise AttributeError
            self.__throttle_position_error = status.value
        except AttributeError:
            print("AttributeError on throttle_position_error")

    @property
    def acc_pedal_error(self):
        """ 加速踏板故障 """
        return self.__acc_pedal_error

    @acc_pedal_error.setter
    def acc_pedal_error(self, status):
        """ 加速踏板故障 """
        try:
            if status not in EnumValidInvalidStatus:
                raise AttributeError
            self.__acc_pedal_error = status.value
        except AttributeError:
            print("AttributeError on acc_pedal_error")

    @property
    def engine_speed(self):
        """ 发动机转速 """
        return int(self.__engine_speed * 0.25)

    @engine_speed.setter
    def engine_speed(self, value):
        """ 发动机转速 """
        try:
            if not isinstance(value, int):
                raise AttributeError
            self.__engine_speed = int('FFFF', 16) if value < 0 or value > 16383.5 else int(value / 0.25)
        except AttributeError:
            print("AttributeError on engine_speed")

    @property
    def engine_throttle_position(self):
        """ 发动机节气门位置 """
        return int(self.__engine_throttle_position * 0.4)

    @engine_throttle_position.setter
    def engine_throttle_position(self, value):
        """ 发动机节气门位置 """
        try:
            if not isinstance(value, int):
                raise AttributeError
            if value < 0 or value > int('FA', 16):
                raise ValueError
            self.__engine_throttle_position = int('FF', 16) if value < 0 or value > 100 else int(value / 0.4)
        except ValueError:
            print("AttributeError on engine_throttle_position")

    @property
    def acc_pedal(self):
        """ 加速踏板位置 """
        return int(self.__acc_pedal * 0.4)

    @acc_pedal.setter
    def acc_pedal(self, value):
        """ 加速踏板位置 """
        try:
            if not isinstance(value, int):
                raise AttributeError
            self.__acc_pedal = int('FF', 16) if value < 0 or value > 100 else int(value / 0.4)
        except AttributeError:
            print("AttributeError on acc_pedal")

    def encode(self):
        # 发动机转速故障 + 节气门位置故障 + 加速踏板故障
        self._msg_data[0] = hex((self.__engine_speed_error << 2) |
                                (self.__throttle_position_error << 3) |
                                (self.__acc_pedal_error << 4))
        # 发动机转速
        self._msg_data[1] = hex(self.__engine_speed >> 8)
        self._msg_data[2] = hex(self.__engine_speed % 256)
        # 发动机节气门位置
        self._msg_data[3] = hex(self.__engine_throttle_position)
        # 加速踏板位置
        self._msg_data[4] = hex(self.__acc_pedal)
        return self._msg_data

    def dump(self):
        super(Ems302, self).dump()
        print("-> EMS_EngineSpeedErr:\t\t" + EnumValidInvalidStatus(self.engine_speed_error).name)
        print("-> EMS_ThrottlePosErr:\t\t" + EnumValidInvalidStatus(self.throttle_position_error).name)
        print("-> EMS_AccPedalErr:\t\t\t" + EnumValidInvalidStatus(self.acc_pedal_error).name)
        print("-> EMS_EngineSpeed:\t\t\t" + (str(self.engine_speed) if self.__engine_speed != int('FFFF', 16) else 'Invalid'))
        print("-> EMS_EngineThrottlePos:\t" + (str(self.engine_throttle_position) if self.__engine_throttle_position != int('FF', 16) else 'Invalid'))
        print("-> EMS_AccPedal:\t\t\t" + (str(self.acc_pedal) if self.__acc_pedal != int('FF', 16) else 'Invalid'))


@unique
class EnumEmsEngineStatus(Enum):
    KeyOff = 0
    KeyOn = 1
    Cranking = 2
    Running = 3


class Ems303(CanMsgBasic):
    """ 发动机管理系统 """
    def __init__(self):
        super(Ems303, self).__init__('EMS_303',
                                     EnumMsgType.Normal,
                                     0x303,
                                     EnumMsgTransmitType.Cycle,
                                     EnumMsgSignalType.Cycle,
                                     100,
                                     8,
                                     ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # 发动机运行状态
        self.__engine_status = 0
        # 发动机启动成功状态
        self.__engine_start_flag = 0

    @property
    def engine_status(self):
        """ 发动机运行状态 """
        return self.__engine_status

    @engine_status.setter
    def engine_status(self, status):
        """ 发动机运行状态 """
        try:
            if status not in EnumEmsEngineStatus:
                raise AttributeError
            self.__engine_status = status.value
            self.__engine_start_flag = 1
        except AttributeError:
            print("AttributeError on engine_status")

    def encode(self):
        # 发动机运行状态　+ 发动机启动成功状态
        self._msg_data[0] = hex((self.__engine_status << 0) |
                                (self.__engine_start_flag << 3))
        return self._msg_data

    def dump(self):
        super(Ems303, self).dump()


@unique
class EnumLampStatus(Enum):
    Off = 0
    On = 1
    NotUsed = 2
    Error = 3


@unique
class EnumDoorStatus(Enum):
    Close = 0
    Open = 1


@unique
class EnumLockStatus(Enum):
    Default = 0
    Unlock = 1
    Locked = 2
    Error = 3
    Invalid = 4
    InvalidValue1 = 5
    InvalidValue2 = 6
    InitialValue = 7


@unique
class EnumHandbrakeStatus(Enum):
    Invalid = 0
    Up = 1
    Down = 2
    Reserved = 3


@unique
class EnumFindCarStatus(Enum):
    Invalid = 0
    NotAllowed = 1
    Executing = 2
    Finished = 3


class Bcm350(CanMsgBasic):
    """ 车身控制器 """
    def __init__(self):
        super(Bcm350, self).__init__('BCM_350',
                                     EnumMsgType.Normal,
                                     0x350,
                                     EnumMsgTransmitType.Cycle,
                                     EnumMsgSignalType.Cycle,
                                     100,
                                     8,
                                     ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # 近光灯工作状态
        self.__low_beam_status = 0
        # 远光灯工作状态
        self.__high_beam_status = 0
        # 前雾灯工作状态
        self.__front_fog_lamp_status = 0
        # 后雾灯工作状态
        self.__rear_fog_lamp_status = 0
        # 左转向灯信号
        self.__turn_indicator_left = 0
        # 右转向灯信号
        self.__turn_indicator_right = 0
        # 左前门状态
        self.__driver_door_status = 0
        # 右前门状态
        self.__passenger_door_status = 0
        # 左后门状态
        self.__left_rear_door_status = 0
        # 右后门状态
        self.__right_rear_door_status = 0
        # 尾门状态
        self.__tailgate_status = 0
        # 左前门门锁状态
        self.__driver_door_lock_status = 7
        # 手刹信号
        self.__handbrake_signal = 0
        # 寻车控制请求执行状态
        self.__find_car_valid = 0

    @property
    def low_beam_status(self):
        """ 近光灯工作状态 """
        return self.__low_beam_status

    @low_beam_status.setter
    def low_beam_status(self, status):
        """ 近光灯工作状态 """
        try:
            if status not in EnumLampStatus:
                raise AttributeError
            self.__low_beam_status = status.value
        except AttributeError:
            print("AttributeError on low_beam_status")

    @property
    def high_beam_status(self):
        """ 远光灯工作状态 """
        return self.__high_beam_status

    @high_beam_status.setter
    def high_beam_status(self, status):
        """ 远光灯工作状态 """
        try:
            if status not in EnumLampStatus:
                raise AttributeError
            self.__high_beam_status = status.value
        except AttributeError:
            print("AttributeError on high_beam_status")

    @property
    def front_fog_lamp_status(self):
        """ 前雾灯工作状态 """
        return self.__front_fog_lamp_status

    @front_fog_lamp_status.setter
    def front_fog_lamp_status(self, status):
        """ 前雾灯工作状态 """
        try:
            if status not in EnumLampStatus:
                raise AttributeError
            self.__front_fog_lamp_status = status.value
        except AttributeError:
            print("AttributeError on front_fog_lamp_status")

    @property
    def rear_fog_lamp_status(self):
        """ 后雾灯工作状态 """
        return self.__rear_fog_lamp_status

    @rear_fog_lamp_status.setter
    def rear_fog_lamp_status(self, status):
        """ 后雾灯工作状态 """
        try:
            if status not in EnumLampStatus:
                raise AttributeError
            self.__rear_fog_lamp_status = status.value
        except AttributeError:
            print("AttributeError on rear_fog_lamp_status")

    @property
    def turn_indicator_left(self):
        """ 左转向灯信号 """
        return self.__turn_indicator_left

    @turn_indicator_left.setter
    def turn_indicator_left(self, status):
        """ 左转向灯信号 """
        try:
            if status not in EnumLampStatus:
                raise AttributeError
            self.__turn_indicator_left = status.value
        except AttributeError:
            print("AttributeError on turn_indicator_left")

    @property
    def turn_indicator_right(self):
        """ 右转向灯信号 """
        return self.__turn_indicator_right

    @turn_indicator_right.setter
    def turn_indicator_right(self, status):
        """ 右转向灯信号 """
        try:
            if status not in EnumLampStatus:
                raise AttributeError
            self.__turn_indicator_right = status.value
        except AttributeError:
            print("AttributeError on turn_indicator_right")

    @property
    def driver_door_status(self):
        """ 左前门状态 """
        return self.__driver_door_status

    @driver_door_status.setter
    def driver_door_status(self, status):
        """ 左前门状态 """
        try:
            if status not in EnumDoorStatus:
                raise AttributeError
            self.__driver_door_status = status.value
        except AttributeError:
            print("AttributeError on driver_door_status")

    @property
    def passenger_door_status(self):
        """ 右前门状态 """
        return self.__passenger_door_status

    @passenger_door_status.setter
    def passenger_door_status(self, status):
        """ 右前门状态 """
        try:
            if status not in EnumDoorStatus:
                raise AttributeError
            self.__passenger_door_status = status.value
        except AttributeError:
            print("AttributeError on passenger_door_status")

    @property
    def left_rear_door_status(self):
        """ 左后门状态 """
        return self.__left_rear_door_status

    @left_rear_door_status.setter
    def left_rear_door_status(self, status):
        """ 左后门状态 """
        try:
            if status not in EnumDoorStatus:
                raise AttributeError
            self.__left_rear_door_status = status.value
        except AttributeError:
            print("AttributeError on left_rear_door_status")

    @property
    def right_rear_door_status(self):
        """ 右后门状态 """
        return self.__right_rear_door_status

    @right_rear_door_status.setter
    def right_rear_door_status(self, status):
        """ 右后门状态 """
        try:
            if status not in EnumDoorStatus:
                raise AttributeError
            self.__right_rear_door_status = status.value
        except AttributeError:
            print("AttributeError on right_rear_door_status")

    @property
    def tailgate_status(self):
        """ 尾门状态 """
        return self.__tailgate_status

    @tailgate_status.setter
    def tailgate_status(self, status):
        """ 尾门状态 """
        try:
            if status not in EnumDoorStatus:
                raise AttributeError
            self.__tailgate_status = status.value
        except AttributeError:
            print("AttributeError on tailgate_status")

    @property
    def driver_door_lock_status(self):
        """ 左前门门锁状态 """
        return self.__driver_door_lock_status

    @driver_door_lock_status.setter
    def driver_door_lock_status(self, status):
        """ 左前门门锁状态 """
        try:
            if status not in EnumLockStatus:
                raise AttributeError
            self.__driver_door_lock_status = status.value
        except AttributeError:
            print("AttributeError on driver_door_lock_status")

    @property
    def handbrake_signal(self):
        """ 手刹信号 """
        return self.__handbrake_signal

    @handbrake_signal.setter
    def handbrake_signal(self, status):
        """ 手刹信号 """
        try:
            if status not in EnumHandbrakeStatus:
                raise AttributeError
            self.__handbrake_signal = status.value
        except AttributeError:
            print("AttributeError on handbrake_signal")

    @property
    def find_car_valid(self):
        """ 寻车控制请求执行状态 """
        return self.__find_car_valid

    @find_car_valid.setter
    def find_car_valid(self, status):
        """ 寻车控制请求执行状态 """
        try:
            if status not in EnumFindCarStatus:
                raise AttributeError
            self.__find_car_valid = status.value
        except AttributeError:
            print("AttributeError on find_car_valid")

    def encode(self):
        # 近光灯工作状态 + 远光灯工作状态 + 前雾灯工作状态 + 后雾灯工作状态
        self._msg_data[0] = hex((self.__low_beam_status << 0) |
                                (self.__high_beam_status << 2) |
                                (self.__front_fog_lamp_status << 4) |
                                (self.__rear_fog_lamp_status << 6))
        # 左转向灯信号 + 右转向灯信号 + 左前门状态 + 右前门状态 + 左后门状态 + 右后门状态
        self._msg_data[1] = hex((self.__turn_indicator_left << (8 % 8)) |
                                (self.__turn_indicator_right << (10 % 8)) |
                                (self.__driver_door_status << (12 % 8)) |
                                (self.__passenger_door_status << (13 % 8)) |
                                (self.__left_rear_door_status << (14 % 8)) |
                                (self.__right_rear_door_status << (15 % 8)))
        # 尾门状态 + 左前门门锁状态 + 手刹信号 + 寻车控制请求执行状态
        self._msg_data[2] = hex((self.__tailgate_status << (16 % 8)) |
                                (self.__driver_door_lock_status << (17 % 8)) |
                                (self.__handbrake_signal << (20 % 8)) |
                                (self.__find_car_valid << (22 % 8)))
        return self._msg_data

    def dump(self):
        super(Bcm350, self).dump()
        print("-> BCM_LowBeamStatus:\t\t" + EnumLampStatus(self.low_beam_status).name)
        print("-> BCM_HighBeamStatus:\t\t" + EnumLampStatus(self.high_beam_status).name)
        print("-> BCM_FrontFogLampStatus:\t" + EnumLampStatus(self.front_fog_lamp_status).name)
        print("-> BCM_RearFogLampStatus:\t" + EnumLampStatus(self.rear_fog_lamp_status).name)
        print("-> BCM_TurnIndicatorLeft:\t" + EnumLampStatus(self.turn_indicator_left).name)
        print("-> BCM_TurnIndicatorRight:\t" + EnumLampStatus(self.turn_indicator_right).name)
        print("-> BCM_DriverDoorStatus:\t" + EnumDoorStatus(self.driver_door_status).name)
        print("-> BCM_PassengerDoorStatus:\t" + EnumDoorStatus(self.passenger_door_status).name)
        print("-> BCM_LeftRearDoorStatus:\t" + EnumDoorStatus(self.left_rear_door_status).name)
        print("-> BCM_RightRearDoorStatus:\t" + EnumDoorStatus(self.right_rear_door_status).name)
        print("-> BCM_TailgateStatus:\t\t" + EnumDoorStatus(self.tailgate_status).name)
        print("-> BCM_DriverDoorLockStatus:" + EnumLockStatus(self.driver_door_lock_status).name)
        print("-> BCM_HandbrakeSignal:\t\t" + EnumHandbrakeStatus(self.handbrake_signal).name)
        print("-> BCM_FindCarValid:\t\t" + EnumFindCarStatus(self.find_car_valid).name)


class EnumNmStatus(Enum):
    Inactive = 0
    Active = 1


class Bcm401(CanMsgBasic):
    """ BCM网络管理报文 """
    def __init__(self):
        super(Bcm401, self).__init__('BCM_401',
                                     EnumMsgType.NM,
                                     0x401 - 0x400,
                                     EnumMsgTransmitType.Event,
                                     EnumMsgSignalType.Cycle,
                                     200,
                                     8,
                                     ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # 近光灯工作状态
        self.__destination_address = 0x1
        self.__alive = 0x1
        self.__ring = 0
        self.__limp_home = 0
        self.__sleep_indication = 0
        self.__sleep_acknowledge = 0

    @property
    def destination_address(self):
        """ 目标地址 """
        return self.__destination_address

    @destination_address.setter
    def destination_address(self, value):
        """ 目标地址 """
        try:
            if not isinstance(value, int):
                raise AttributeError
            self.__destination_address = 0x1 if value < 0 or value > 255 else value
        except AttributeError:
            print("destination_address invalid param")

    @property
    def alive(self):
        """  """
        return self.__alive

    @alive.setter
    def alive(self, status):
        """  """
        try:
            if status not in EnumNmStatus:
                raise AttributeError
            self.__alive = status.value
        except AttributeError:
            print("AttributeError on alive")

    @property
    def ring(self):
        """  """
        return self.__ring

    @ring.setter
    def ring(self, status):
        """  """
        try:
            if status not in EnumNmStatus:
                raise AttributeError
            self.__ring = status.value
        except AttributeError:
            print("AttributeError on ring")

    @property
    def limp_home(self):
        """  """
        return self.__limp_home

    @limp_home.setter
    def limp_home(self, status):
        """  """
        try:
            if status not in EnumNmStatus:
                raise AttributeError
            self.__limp_home = status.value
        except AttributeError:
            print("AttributeError on limp_home")

    @property
    def sleep_indication(self):
        """  """
        return self.__sleep_indication

    @sleep_indication.setter
    def sleep_indication(self, status):
        """  """
        try:
            if status not in EnumNmStatus:
                raise AttributeError
            self.__sleep_indication = status.value
        except AttributeError:
            print("AttributeError on sleep_indication")

    @property
    def sleep_acknowledge(self):
        """  """
        return self.__sleep_acknowledge

    @sleep_acknowledge.setter
    def sleep_acknowledge(self, status):
        """  """
        try:
            if status not in EnumNmStatus:
                raise AttributeError
            self.__sleep_acknowledge = status.value
        except AttributeError:
            print("AttributeError on sleep_acknowledge")

    def encode(self):
        # 目标地址
        self._msg_data[0] = hex(self.__destination_address << 0)
        # Alive + Ring + LimpHome + SleepIndication + SleepAcknowledge
        self._msg_data[1] = hex((self.__alive << (8 % 8)) |
                                (self.__ring << (9 % 8)) |
                                (self.__limp_home << (10 % 8)) |
                                (self.__sleep_indication << (12 % 8)) |
                                (self.__sleep_acknowledge << (13 % 8)))
        return self._msg_data

    def dump(self):
        super(Bcm401, self).dump()
        print("-> BCM_NM_DestinationAddress:" + hex(self.destination_address))
        print("-> BCM_NM_Alive:\t\t\t " + EnumNmStatus(self.alive).name)
        print("-> BCM_NM_Ring:\t\t\t\t " + EnumNmStatus(self.ring).name)
        print("-> BCM_NM_LimpHome:\t\t\t " + EnumNmStatus(self.limp_home).name)
        print("-> BCM_NM_SleepIndication:\t " + EnumNmStatus(self.sleep_indication).name)
        print("-> BCM_NM_SleepAcknowledge:\t " + EnumNmStatus(self.sleep_acknowledge).name)


@unique
class EnumBcmOnOffStatus(Enum):
    Off = 0
    On = 1


@unique
class EnumBcmValidInvalidStatus(Enum):
    Invalid = 0
    Valid = 1


@unique
class EnumWiperStatus(Enum):
    Stop = 0
    LowSpeed = 1
    HighSpeed = 2
    Interrupt = 3
    Wash = 4
    Reserved = 5
    SwitchFailure = 6
    Invalid = 7


class Bcm365(CanMsgBasic):
    """ 车身控制器 """
    def __init__(self):
        super(Bcm365, self).__init__('BCM_365',
                                     EnumMsgType.Normal,
                                     0x365,
                                     EnumMsgTransmitType.Cycle,
                                     EnumMsgSignalType.Cycle,
                                     100,
                                     8,
                                     ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # ESCL电源请求的响应信号
        self.__escl_power_resp = 0
        # ESCL解锁信号反馈
        self.__escl_unlock_feedback = 0
        # 电源继电器输出状态
        self.__power_relay_output_status = 0
        # 点火信号状态
        self.__ignition_status = 0
        # 雨刷状态
        self.__wiper_status = 0
        # 前挡风玻璃洗涤喷水信号
        self.__sprinkler_status = 0
        # 前挡风玻璃洗涤喷水信号有效标志
        self.__sprinkler_status_valid = 0
        # 后除霜状态
        self.__rear_defrost_status = 0
        # 后除霜状态有效标志位
        self.__rear_defrost_status_valid = 0
        # 外后视镜折叠状态
        self.__exterior_mirror_elec_flod_status = 0
        # 车身防盗状态
        self.__vehicle_antt_status = 0

    @property
    def rear_defrost_status(self):
        """ 后除霜状态 """
        return self.__rear_defrost_status

    @rear_defrost_status.setter
    def rear_defrost_status(self, status):
        """ 后除霜状态 """
        try:
            if status not in EnumBcmOnOffStatus:
                self.__rear_defrost_status_valid = EnumBcmValidInvalidStatus.Invalid.value
                raise AttributeError
            self.__rear_defrost_status = status.value
            self.__rear_defrost_status_valid = EnumBcmValidInvalidStatus.Valid.value
        except AttributeError:
            print("AttributeError on rear_defrost_status")

    @property
    def wiper_status(self):
        """ 雨刷状态 """
        return self.__wiper_status

    @wiper_status.setter
    def wiper_status(self, status):
        """ 雨刷状态 """
        try:
            if status not in EnumWiperStatus:
                raise AttributeError
            self.__wiper_status = status.value
        except AttributeError:
            print("AttributeError on wiper_status")

    def encode(self):
        # ESCL电源请求的响应信号 + ESCL解锁信号反馈 + 电源继电器输出状态
        self._msg_data[0] = hex((self.__escl_power_resp << 0) |
                                (self.__escl_unlock_feedback << 2) |
                                (self.__power_relay_output_status << 4))
        # 点火信号状态　+　雨刷状态 + 前挡风玻璃洗涤喷水信号　+ 前挡风玻璃洗涤喷水信号有效标志
        self._msg_data[1] = hex((self.__ignition_status << (8 % 8)) |
                                (self.__wiper_status << (11 % 8)) |
                                (self.__sprinkler_status << (14 % 8)) |
                                (self.__sprinkler_status_valid << (15 % 8)))
        # 后除霜状态　+ 后除霜状态有效标志
        self._msg_data[2] = hex((self.__rear_defrost_status << (16 % 8)) |
                                (self.__rear_defrost_status_valid << (17 % 8)) |
                                (self.__exterior_mirror_elec_flod_status << (18 % 8)) |
                                (self.__vehicle_antt_status << (20 % 8)))
        return self._msg_data

    def dump(self):
        super(Bcm365, self).dump()


@unique
class EnumAcOnOffStatus(Enum):
    Off = 0
    On = 1


@unique
class EnumAcValidInvalidStatus(Enum):
    Invalid = 0
    Valid = 1


class Ac378(CanMsgBasic):
    """ 空调 """
    def __init__(self):
        super(Ac378, self).__init__('AC_378',
                                    EnumMsgType.Normal,
                                    0x378,
                                    EnumMsgTransmitType.Cycle,
                                    EnumMsgSignalType.Cycle,
                                    100,
                                    8,
                                    ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # 当前环境温度(摄氏度)
        self.__outside_ambient_temperature = 0
        # 当前环境温度有效状态
        self.__outside_ambient_temperature_valid = 0
        # 空调系统中压信号
        self.__pressure_status = 0
        # 空调系统中压信号有效标志
        self.__pressure_status_valid = 0
        # 压缩机开关请求
        self.__ac_request = 0
        # 压缩机开关请求有效状态
        self.__ac_request_valid = 0
        # 鼓风机开关状态
        self.__blower_on_off_status = 0
        # 鼓风机开关状态有效标志
        self.__blower_on_off_status_valid = 0
        # 后除霜开关请求
        self.__rear_defrost_request = 0
        # 后除霜开关请求有效标志
        self.__rear_defrost_request_valid = 0
        # 按键或旋钮操作导致空调控制器状态发生变化时,需向DVD请求显示变更(此标志维持的时间为:100ms,即空调控制器只需发一次)
        self.__display_active = 0
        # AC Max状态
        self.__ac_max_mode = 0
        # 设置温度
        self.__set_temperature = 0
        # 鼓风机当前档位
        self.__blower_speed_level = 0
        # 出风模式
        self.__air_distribute_mode = 0
        # 前除霜状态
        self.__defrost_mode = 0
        # 内外循环状态
        self.__air_let_mode = 0
        # Auto模式状态
        self.__auto_mode = 0
        # Off状态
        self.__on_off_state = 0
        # Rear状态
        self.__rear_mode = 0
        # AC工作指示灯
        self.__ac_indicator = 0

    @property
    def set_temperature(self):
        """ 设置温度 """
        return int(self.__set_temperature * 0.5)

    @set_temperature.setter
    def set_temperature(self, value):
        """ 设置温度 """
        try:
            if not isinstance(value, float):
                raise AttributeError
            # self.__set_temperature = int('7F', 16) if value < 17.0 or value > 32.0 else int(value / 0.5)
            self.__set_temperature = int(value / 0.5)
        except AttributeError:
            print("AttributeError on set_temperature")

    @property
    def defrost_mode(self):
        """ 前除霜状态 """
        return self.__defrost_mode

    @defrost_mode.setter
    def defrost_mode(self, status):
        """ 前除霜状态 """
        try:
            if status not in EnumAcOnOffStatus:
                raise AttributeError
            self.__defrost_mode = status.value
        except AttributeError:
            print("AttributeError on defrost_mode")

    @property
    def on_off_state(self):
        """ OnOff状态 """
        return self.__on_off_state

    @on_off_state.setter
    def on_off_state(self, status):
        """ OnOff状态 """
        try:
            if status not in EnumAcOnOffStatus:
                raise AttributeError
            self.__on_off_state = status.value
        except AttributeError:
            print("AttributeError on on_off_state")

    def encode(self):
        # 当前环境温度(摄氏度)
        self._msg_data[0] = hex(self.__outside_ambient_temperature)
        # 当前环境温度有效状态 + 空调系统中压信号 + 空调系统中压信号有效状态 + 压缩机开关请求 + 压缩机开关请求有效状态 + 鼓风机开关状态 + 鼓风机开关状态有效状态
        self._msg_data[1] = hex((self.__outside_ambient_temperature_valid << (8 % 8)) |
                                (self.__pressure_status << (9 % 8)) |
                                (self.__pressure_status_valid << (11 % 8)) |
                                (self.__ac_request << (12 % 8)) |
                                (self.__ac_request_valid << (13 % 8)) |
                                (self.__blower_on_off_status << (14 % 8)) |
                                (self.__blower_on_off_status_valid << (15 % 8)))
        # 后除霜开关请求 + 后除霜开关请求有效标志位 + 按键或旋钮操作导致空调控制器状态发生变化 + AC MAX状态
        self._msg_data[2] = hex((self.__rear_defrost_request << (20 % 8)) |
                                (self.__rear_defrost_request_valid << (21 % 8)) |
                                (self.__display_active << (22 % 8)) |
                                (self.__ac_max_mode << (23 % 8)))
        # 设置温度
        self._msg_data[3] = hex(self.__set_temperature << (24 % 8))
        # 鼓风机当前档位 + 出风模式 + 前除霜状态
        self._msg_data[4] = hex((self.__blower_speed_level << (32 % 8)) |
                                (self.__air_distribute_mode << (36 % 8)) |
                                (self.__defrost_mode << (39 % 8)))
        # 内外循环状态 + Auto模式状态 + Off状态 + Rear状态　+ AC工作指示灯
        self._msg_data[5] = hex((self.__air_let_mode << (40 % 8)) |
                                (self.__auto_mode << (41 % 8)) |
                                (self.__on_off_state << (42 % 8)) |
                                (self.__rear_mode << (43 % 8)) |
                                (self.__ac_indicator << (44 % 8)))
        return self._msg_data

    def dump(self):
        super(Ac378, self).dump()


@unique
class EnumGearPos(Enum):
    P = 0
    R = 1
    N = 2
    D = 3
    ManualGear1 = 4
    ManualGear2 = 5
    ManualGear3 = 6
    ManualGear4 = 7
    ManualGear5 = 8
    ManualGear6 = 9
    S = 10
    Unknown = 11
    Z1 = 12
    Z2 = 13
    Z3 = 14
    Invalid = 15


class Tcu328(CanMsgBasic):
    """ 变速箱控制单元 """
    def __init__(self):
        super(Tcu328, self).__init__('TCU_328',
                                     EnumMsgType.Normal,
                                     0x328,
                                     EnumMsgTransmitType.Cycle,
                                     EnumMsgSignalType.Cycle,
                                     100,
                                     8,
                                     ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # Gear Position
        self.__gear_position_status = 0
        # Validity of Gear Position
        self.__gear_position_vd = 0
        # TCU warning for meter display
        self.__ind_fault_status = 0

    @property
    def gear_position_status(self):
        """ 变速箱档位 """
        return self.__gear_position_status

    @gear_position_status.setter
    def gear_position_status(self, status):
        """ 变速箱档位 """
        try:
            if status not in EnumGearPos:
                self.__gear_position_vd = 1
                raise AttributeError
            self.__gear_position_status = status.value
            self.__gear_position_vd = 0
        except AttributeError:
            print("AttributeError on gear_position_status")

    def encode(self):
        # Gear Position + Gear Position VD
        self._msg_data[0] = hex((self.__gear_position_status << 0) |
                                (self.__gear_position_vd << 4))
        # IND Fault Status
        self._msg_data[2] = hex(self.__ind_fault_status << (17 % 8))
        return self._msg_data

    def dump(self):
        super(Tcu328, self).dump()


@unique
class EnumPepsPowerMode(Enum):
    Default = 0
    Off = 1
    Acc = 2
    On = 3
    Start = 4
    InvalidValue1 = 5
    InvalidValue2 = 6
    Invalid = 7


class Peps341(CanMsgBasic):
    """ 无钥匙进入和启动系统 """
    def __init__(self):
        super(Peps341, self).__init__('PEPS_341',
                                      EnumMsgType.Normal,
                                      0x341,
                                      EnumMsgTransmitType.Cycle,
                                      EnumMsgSignalType.Cycle,
                                      100,
                                      8,
                                      ['0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00', '0x00'])
        # 电源分配状态
        self.__power_mode = 0
        # 智能钥匙电池电量低提示
        self.__fob_low_bat_warning = 0
        # 远程模式
        self.__remote_mode = 0
        # ECU故障类型指示
        self.__escl_ecu_fail_warning = 0
        # ECU故障提示
        self.__ecu_fail_warning = 0
        # 发动机启动请求
        self.__engine_start_request = 0
        # 防盗认证结果
        self.__release_sig = 0

    @property
    def power_mode(self):
        """ PEPS电源分配状态 """
        return self.__power_mode

    @power_mode.setter
    def power_mode(self, status):
        """ PEPS电源分配状态 """
        try:
            if status not in EnumPepsPowerMode:
                raise AttributeError
            self.__power_mode = status.value
        except AttributeError:
            print("AttributeError on power_mode")

    def encode(self):
        # 电源分配状态　+ 智能钥匙电池电量低提示 + 远程模式
        self._msg_data[0] = hex((self.__power_mode << 0) |
                                (self.__fob_low_bat_warning << 5) |
                                (self.__remote_mode << 6))
        # ESCL ECU故障类型指示
        self._msg_data[1] = hex(self.__escl_ecu_fail_warning << (8 % 8))
        # ECU故障提示
        self._msg_data[2] = hex(self.__ecu_fail_warning << (22 % 8))
        # 发动机启动请求
        self._msg_data[3] = hex(self.__engine_start_request << (24 % 8))
        # 防盗认证结果
        self._msg_data[4] = hex(self.__release_sig << (35 % 8))
        return self._msg_data

    def dump(self):
        super(Peps341, self).dump()


if __name__ == '__main__':
    pass
    # ac = Ac378()
    # print(ac.encode())
    # ac.rear_defrost_request = EnumAcOnOffStatus.On
    # print(ac.encode())
    # ac.dump()
