*** Settings ***
Documentation     远程配置请求
Library           ../TBoxLibrary.py

*** Keywords ***
设置MQTT服务器
    [Arguments]    ${host}    ${port}    ${expected}=True
    [Documentation]    设置MQTT服务器
    ...
    ...    :param host: 主机名
    ...
    ...    :param port: 端口号
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置MQTT服务器 | test.mosquitto.org:8883 | expected=True |
    ${retval}=    Request Remote Config    MQTT_SERVER_ADDR    ${host}:${port}
    Should Be Equal As Strings    ${retval}    ${expected}

设置MQTT主题
    [Arguments]    ${topic}    ${expected}=True
    [Documentation]    设置MQTT主题
    ...
    ...    :param topic: \ 主题
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置MQTT主题 | device/gate/bussiness | expected=True |
    ${retval}=    Request Remote Config    MQTT_SERVER_TOPIC    ${topic}
    Should Be Equal As Strings    ${retval}    ${expected}

设置备用MQTT服务器
    [Arguments]    ${host}    ${port}    ${expected}=True
    [Documentation]    设置备用MQTT服务器
    ...
    ...    :param host: \ 主机名
    ...
    ...    :param port: \ 端口号
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置备用MQTT服务器 | test.mosquitto.org:8883 | expected=True |
    ${retval}=    Request Remote Config    MQTT_KEY_BUSINESS_SERVER_ADDR    ${host}:${port}
    Should Be Equal As Strings    ${retval}    ${expected}

设置备用MQTT主题
    [Arguments]    ${topic}    ${expected}=True
    [Documentation]    设置备用MQTT主题
    ...
    ...    :param topic: \ 主题
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置备用MQTT主题 | device/gate/bussiness | expected=True |
    ${retval}=    Request Remote Config    MQTT_KEY_BUSINESS_SERVER_TOPIC    ${topic}
    Should Be Equal As Strings    ${retval}    ${expected}

设置ECall号码
    [Arguments]    ${number}    ${expected}=True
    [Documentation]    设置E-Call号码
    ...
    ...    :param number: \ 号码
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置ECall号码 | 13012345678 | expected=True |
    ${retval}=    Request Remote Config    ECALL_NUMBER    ${number}
    Should Be Equal As Strings    ${retval}    ${expected}

设置BCall号码
    [Arguments]    ${number}    ${expected}=True
    [Documentation]    设置B-Call号码
    ...
    ...    :param number: \ 号码
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置BCall号码 | 13012345678 | expected=True |
    ${retval}=    Request Remote Config    BCALL_NUMBER    ${number}
    Should Be Equal As Strings    ${retval}    ${expected}

设置ICall号码
    [Arguments]    ${number}    ${expected}=True
    [Documentation]    设置I-Call号码
    ...
    ...    :param number: \ 号码
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置ICall号码 | 13012345678 | expected=True |
    ${retval}=    Request Remote Config    ICALL_NUMBER    ${number}
    Should Be Equal As Strings    ${retval}    ${expected}

设置ECall使能
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置E-Call使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置ECall使能 | True | expected=True |
    ${retval}=    Request Remote Config    ECALL_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置BCall使能
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置B-Call使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 设置BCall使能 | True | expected=True |
    ${retval}=    Request Remote Config    BCALL_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置ICall使能
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置I-Call使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置ICall使能 | True | expected=True |
    ${retval}=    Request Remote Config    ICALL_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置上行短信网关
    [Arguments]    ${host}    ${port}    ${expected}=True
    [Documentation]    设置上行短信网关
    ...
    ...    :param host: \ 主机名
    ...
    ...    :param port: \ 端口号
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置上行短信网关 | test.mosquitto.org:8883 | expected=True |
    ${retval}=    Request Remote Config    SMS_GATE_NUMBER_UPLOAD    ${host}:${port}
    Should Be Equal As Strings    ${retval}    ${expected}

设置下行短信网关
    [Arguments]    ${host}    ${port}    ${expected}=True
    [Documentation]    设置下行短信网关
    ...
    ...    :param host: \ 主机名
    ...
    ...    :param port: 端口号
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置下行短信网关 | test.mosquitto.org:8883 | expected=True |
    ${retval}=    Request Remote Config    SMS_GATE_NUMBER_DOWNLOAD    ${host}:${port}
    Should Be Equal As Strings    ${retval}    ${expected}

设置Datamining上传频率
    [Arguments]    ${freq}    ${expected}=True
    [Documentation]    设置Datamining上传频率
    ...
    ...    :param freq: \ 上传频率
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置Datamining上传频率 | 30 | expected=True |
    ${retval}=    Request Remote Config    DATAMINING_UPLOAD_FREQUENCY    ${freq}
    Should Be Equal As Strings    ${retval}    ${expected}

设置Vehicle上传频率
    [Arguments]    ${freq}    ${expected}=True
    [Documentation]    设置Vehicle上传频率
    ...
    ...    :param freq: \ 上传频率
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置Vehicle上传频率 | 30 | expected=True |
    ${retval}=    Request Remote Config    VEHICLE_STATUS_UPLOAD_FREQUENCY    ${freq}
    Should Be Equal As Strings    ${retval}    ${expected}

设置发动机状态上传使能
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置点火熄火上传状态使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置发动机状态上传使能 | True | expected=True |
    ${retval}=    Request Remote Config    IGNITION_BLOWOUT_UPLOAD_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置上报告警信息使能
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置上传告警信息使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置上传告警信息使能 | True | expected=True |
    ${retval}=    Request Remote Config    UPLOAD_ALERT_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置Datamining使能
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置Datamining使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置Datamining使能 | True | expected=True |
    ${retval}=    Request Remote Config    DATAMING_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置追踪功能使能
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置追踪功能使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置追踪功能使能 | True | expected=True |
    ${retval}=    Request Remote Config    SVT_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置电子围栏功能使能
    [Arguments]    ${status}    ${expected}
    [Documentation]    设置电子围栏功能使能
    ...
    ...    :param status: \ 是否使能
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置电子围栏功能使能 | True | expected=True |
    ${retval}=    Request Remote Config    ELETRONIC_DEFENSE_ENABLE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}

设置异动拖车触发阀值
    [Arguments]    ${status}    ${expected}=True
    [Documentation]    设置异动拖车G-Sensor触发阀值
    ...
    ...    :param threshold: \ 触发阀值
    ...
    ...    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 设置异动拖车触发阀值 | threshold | expected=True |
    ${retval}=    Request Remote Config    ABNORMAL_MOVE_THRESHOLD_VALUE    ${status}
    Should Be Equal As Strings    ${retval}    ${expected}
