*** Settings ***
Library           ../TBoxLibrary.py

*** Keywords ***
开关发动机
    [Arguments]    ${switch}    ${expected}=True
    [Documentation]    :param switch: 是否开启
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | Comment | 开启发动机 |
    ...    | 开关发动机 | True |
    ...    | Comment | 关闭发动机 |
    ...    | 开关发动机 | False | expected=True |
    ${retval}=    Request Remote Control    ENGINE    ${switch}
    Should Be Equal As Strings    ${retval}    ${expected}
