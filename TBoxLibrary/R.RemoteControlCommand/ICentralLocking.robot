*** Settings ***
Library           ../TBoxLibrary.py

*** Keywords ***
开关中控锁
    [Arguments]    ${switch}    ${excepted}=True
    [Documentation]    :param switch: 是否开启
    ...
    ...    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | Comment | 开启中控锁 |
    ...    | 开关中控锁 | True |
    ...    | Comment | 关闭中控锁 |
    ...    | 开关中控锁 | False | expected=True |
    ${retval}=    Request Remote Control    CENTRAL_LOCKING    ${switch}
    Should Be Equal As Strings    ${retval}    ${expected}
