*** Settings ***
Library           ../TBoxLibrary.py

*** Keywords ***
设置左前门状态
    [Arguments]    ${status}
    [Documentation]    :param status: 车门状态
    ...
    ...    Example:
    ...    | Comment | 打开左前门 |
    ...    | 设置左前门状态 | Open |
    ...    | Comment | 关闭左前门 |
    ...    | 设置左前门状态 | Close |
    Request Can Config    DRIVER_DOOR_STS    ${status}

获取左前门状态
    [Arguments]    ${expected}=Open
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取左前门状态 | expected=Open |
    ${retval}    Request Can Data    DRIVER_DOOR_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置右前门状态
    [Arguments]    ${status}
    [Documentation]    :param status: 车门状态
    ...
    ...    Example:
    ...    | Comment | 打开右前门 |
    ...    | 设置右前门状态 | Open |
    ...    | Comment | 关闭右前门 |
    ...    | 设置右前门状态 | Close |
    Request Can Config    PASSENGER_DOOR_STS    ${status}

获取右前门状态
    [Arguments]    ${expected}=Open
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取右前门状态 | expected=Open |
    ${retval}    Request Can Data    PASSENGER_DOOR_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置左后门状态
    [Arguments]    ${status}
    [Documentation]    :param status: 车门状态
    ...
    ...    Example:
    ...    | Comment | 打开左后门 |
    ...    | 设置左后门状态 | Open |
    ...    | Comment | 关闭左后门 |
    ...    | 设置左后门状态 | Close |
    Request Can Config    LEFTREAR_DOOR_STS    ${status}

获取左后门状态
    [Arguments]    ${expected}=Open
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取左后门状态 | expected=Open |
    ${retval}    Request Can Data    LEFTREAR_DOOR_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置右后门状态
    [Arguments]    ${status}
    [Documentation]    :param status: 车门状态
    ...
    ...    Example:
    ...    | Comment | 打开右后门 |
    ...    | 设置右后门状态 | Open |
    ...    | Comment | 关闭右后门 |
    ...    | 设置右后门状态 | Close |
    Request Can Config    RIGHTREAR_DOOR_STS    ${status}

获取右后门状态
    [Arguments]    ${expected}=Open
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取右后门状态 | expected=Open |
    ${retval}    Request Can Data    RIGHTREAR_DOOR_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置后备箱状态
    [Arguments]    ${status}
    [Documentation]    :param status: 车门状态
    ...
    ...    Example:
    ...    | Comment | 打开后备箱 |
    ...    | 设置后备箱状态 | Open |
    ...    | Comment | 关闭后备箱 |
    ...    | 设置后备箱状态 | Close |
    Request Can Config    TAILGATE_STS    ${status}

获取后备箱状态
    [Arguments]    ${expected}=Open
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取后备箱状态 | expected=Open |
    ${retval}    Request Can Data    TAILGATE_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置门锁状态
    [Arguments]    ${status}
    [Documentation]    :param status: 车门锁状态
    ...
    ...    Example:
    ...    | Comment | 车门上锁 |
    ...    | 设置门锁状态 | Locked |
    ...    | Comment | 车门解锁 |
    ...    | 设置门锁状态 | Unlock |
    Request Can Config    DRIVER_DOOR_LOCK_STS    ${status}

获取门锁状态
    [Arguments]    ${expected}=Locked
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取门锁状态 | expected=Locked |
    ${retval}    Request Can Data    DRIVER_DOOR_LOCK_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置手刹状态
    [Arguments]    ${status}
    [Documentation]    :param status: 手刹状态
    ...
    ...    Example:
    ...    | Comment | 拉起手刹 |
    ...    | 设置手刹状态 | Up |
    ...    | Comment | 放下手刹 |
    ...    | 设置手刹状态 | Down |
    Request Can Config    HANDBRAKE_SIGNAL    ${status}

获取手刹状态
    [Arguments]    ${expected}=Up
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取手刹状态 | expected=Up |
    ${retval}    Request Can Data    HANDBRAKE_SIGNAL
    Should Be Equal As Strings    ${retval}    ${expected}

设置空调状态
    [Arguments]    ${status}
    [Documentation]    :param status: 状态
    ...
    ...    Example:
    ...    | Comment | 开启空调 |
    ...    | 设置空调状态 | On |
    ...    | Comment | 关闭空调 |
    ...    | 设置空调状态 | Off |
    Request Can Config    AC_STS    ${status}

获取空调状态
    [Arguments]    ${expected}=On
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取空调状态 | expected=On |
    ${retval}    Request Can Data    AC_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置前除霜状态
    [Arguments]    ${status}
    [Documentation]    :param status: 状态
    ...
    ...    Example:
    ...    | Comment | 开启前除霜 |
    ...    | 设置前除霜状态 | On |
    ...    | Comment | 关闭前除霜 |
    ...    | 设置前除霜状态 | Off |
    Request Can Config    FRONT_DEFROST_STS    ${status}

获取前除霜状态
    [Arguments]    ${expected}=On
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取前除霜状态 | expected=On |
    ${retval}    Request Can Data    FRONT_DEFROST_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置后除霜状态
    [Arguments]    ${status}
    [Documentation]    :param status: 状态
    ...
    ...    Example:
    ...    | Comment | 开启后除霜 |
    ...    | 设置后除霜状态 | On |
    ...    | Comment | 关闭后除霜 |
    ...    | 设置后除霜状态 | Off |
    Request Can Config    REAR_DEFROST_STS    ${status}

获取后除霜状态
    [Arguments]    ${expected}=On
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取后除霜状态 | expected=On |
    ${retval}    Request Can Data    REAR_DEFROST_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置空调温度
    [Arguments]    ${status}
    [Documentation]    :param temperature: 温度
    ...
    ...    Example:
    ...    | Comment | 设置空调温度 |
    ...    | 设置空调温度 | 25.5 |
    Request Can Config    AC_TEMPERATURE    ${status}

获取空调温度
    [Arguments]    ${expected}=25.5
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取空调温度 | expected=25.5 |
    ${retval}    Request Can Data    AC_TEMPERATURE
    Should Be Equal As Strings    ${retval}    ${expected}

设置发动机状态
    [Arguments]    ${status}
    [Documentation]    :param status: 状态
    ...
    ...    Example:
    ...    | Comment | ON档位 |
    ...    | 设置发动机状态 | KeyOn |
    ...    | Comment | OFF档位 |
    ...    | 设置发动机状态 | KeyOff |
    ...    | Comment | 点火中 |
    ...    | 设置发动机状态 | Cranking |
    ...    | Comment | 运行中 |
    ...    | 设置发动机状态 | Running |
    Request Can Config    ENGINE_STS    ${status}

获取发动机状态
    [Arguments]    ${expected}=KeyOff
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取发动机状态 | expected=KeyOff |
    ${retval}    Request Can Data    ENGINE_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置雨刷状态
    [Arguments]    ${status}
    [Documentation]    :param status: 状态
    ...
    ...    Example:
    ...    | Comment | 停止档位 |
    ...    | 设置雨刷状态 | Stop |
    ...    | Comment | 低速档位 |
    ...    | 设置雨刷状态 | LowSpeed |
    ...    | Comment | 高速档位 |
    ...    | 设置雨刷状态 | HighSpeed |
    ...    | Comment | 触发档位 |
    ...    | 设置雨刷状态 | Interrupt |
    ...    | Comment | 喷水档位 |
    ...    | 设置雨刷状态 | Wash |
    Request Can Config    WIPER_STS    ${status}

获取雨刷状态
    [Arguments]    ${expected}=On
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取雨刷状态 | expected=On |
    ${retval}    Request Can Data    WIPER_STS
    Should Be Equal As Strings    ${retval}    ${expected}

设置变速箱状态
    [Arguments]    ${status}
    [Documentation]    :param status: 状态
    ...
    ...    Example:
    ...    | Comment | P档位 |
    ...    | 设置变速箱状态 | P |
    ...    | Comment | R档位 |
    ...    | 设置变速箱状态 | R |
    ...    | Comment | N档位 |
    ...    | 设置变速箱状态 | N |
    ...    | Comment | D档位 |
    ...    | 设置变速箱状态 | D |
    ...    | Comment | 手动1档位 |
    ...    | 设置变速箱状态 | ManualGear1 |
    ...    | Comment | 手动2档位 |
    ...    | 设置变速箱状态 | ManualGear2 |
    ...    | Comment | 手动3档位 |
    ...    | 设置变速箱状态 | ManualGear3 |
    ...    | Comment | 手动4档位 |
    ...    | 设置变速箱状态 | ManualGear4 |
    ...    | Comment | 手动5档位 |
    ...    | 设置变速箱状态 | ManualGear5 |
    ...    | Comment | 手动6档位 |
    ...    | 设置变速箱状态 | ManualGear6 |
    ...    | Comment | S档位 |
    ...    | 设置变速箱状态 | S |
    Request Can Config    GEAR_STS    ${status}

获取变速箱状态
    [Arguments]    ${expected}=On
    [Documentation]    :param expected: 期望返回值
    ...
    ...    Example:
    ...    | 获取变速箱状态 | expected=P |
    ${retval}    Request Can Data    GEAR_STS
    Should Be Equal As Strings    ${retval}    ${expected}
