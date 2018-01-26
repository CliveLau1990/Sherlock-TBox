*** Settings ***
Library           ../TBoxLibrary.py

*** Keywords ***
等待连接成功
    [Arguments]    ${expected}=True
    [Documentation]    :param expected: 返回期望值
    ...
    ...    Example:
    ...    | 等待连接成功 | expected=True |
    ${retval}=    Wait Until Ready
    Should Be Equal As Strings    ${retval}    ${expected}
