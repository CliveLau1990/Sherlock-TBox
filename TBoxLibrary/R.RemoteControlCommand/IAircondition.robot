*** Settings ***
Library           ../TBoxLibrary.py

*** Keywords ***
开关空调
    [Arguments]    ${switch}    ${expected}=True
    [Documentation]    :param switch: 是否开启
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | Comment | 开启空调 |
    ...    | 开关空调 | True |
    ...    | Comment | 关闭空调 |
    ...    | 开关空调 | False | expected=True |
    ${retval}=    Request Remote Control    AIRCONDITION_AC    ${switch}
    Should Be Equal As Strings    ${retval}    ${expected}

调节空调温度
    [Arguments]    ${temperature}    ${expected}=True
    [Documentation]    :param temperature: AC温度 (精度为0.5)
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | Comment | 调节空调温度 |
    ...    | 调节空调温度 | 12.5 | expected=True |
    ${retval}=    Request Remote Control    AIRCONDITION_TEMPERATURE    ${temperature}
    Should Be Equal As Strings    ${retval}    ${expected}

开关前除霜
    [Arguments]    ${switch}    ${expected}=True
    [Documentation]    :param switch: 是否开启
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | Comment | 开启前除霜 |
    ...    | 开关前除霜 | True |
    ...    | Comment | 关闭前除霜 |
    ...    | 开关前除霜 | False | expected=True |
    ${retval}=    Request Remote Control    AIRCONDITION_FRONT_DEFROST    ${switch}
    Should Be Equal As Strings    ${retval}    ${expected}

开关后除霜
    [Arguments]    ${switch}    ${expected}=True
    [Documentation]    :param switch: 是否开启
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | Comment | 开启后除霜 |
    ...    | 开启后除霜 | True |
    ...    | Comment | 开启后除霜 |
    ...    | 开启后除霜 | False | expected=True |
    ${retval}=    Request Remote Control    AIRCONDITION_REAR_DEFROST    ${switch}
    Should Be Equal As Strings    ${retval}    ${expected}
