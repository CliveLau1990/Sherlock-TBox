*** Settings ***
Documentation     CAN 0(Body)测试套件
Test Setup        Initialize
Test Teardown     Uninitialize
Library           TBoxLibrary.py
Resource          R.RemoteConfigRequest/IRemoteConfig.robot
Resource          R.System/IMqttSystem.robot
Resource          R.CAN/CAN.robot

*** Test Cases ***
Demo
    等待连接成功
    设置Vehicle上传频率    10
    设置左前门状态    Open
    设置左后门状态    Open
    设置右前门状态    Open
    设置右后门状态    Open
    设置门锁状态    Locked
    设置手刹状态    Up
    设置空调状态    On
    设置前除霜状态    On
    设置后除霜状态    On
    设置空调温度    35.0
    设置发动机状态    Running
    设置雨刷状态    Interrupt
    设置变速箱状态    N
    Sleep    30
    获取右前门状态    expected=Open
    获取左后门状态    expected=Open
    获取左前门状态    expected=Open
    获取右后门状态    expected=Open
    获取门锁状态    expected=Locked
    获取手刹状态    expected=Up
    获取空调状态    expected=On
    获取前除霜状态    expected=On
    获取后除霜状态    expected=On
    获取空调温度    expected=35.0
    获取发动机状态    expected=Running
    获取雨刷状态    expected=On
    获取变速箱状态    expected=N

发动机状态
    等待连接成功
    设置Vehicle上传频率    5
    Run Keyword And Continue On Failure    设置发动机状态    KeyOff
    Sleep    10
    Run Keyword And Continue On Failure    获取发动机状态    expected=KeyOff
    Sleep    1
    Run Keyword And Continue On Failure    设置发动机状态    KeyOn
    Sleep    10
    Run Keyword And Continue On Failure    获取发动机状态    expected=KeyOn
    Sleep    1
    Run Keyword And Continue On Failure    设置发动机状态    Cranking
    Sleep    10
    Run Keyword And Continue On Failure    获取发动机状态    expected=Cranking
    Sleep    1
    Run Keyword And Continue On Failure    设置发动机状态    Running
    Sleep    10
    Run Keyword And Continue On Failure    获取发动机状态    expected=Running

雨刷状态
    等待连接成功
    设置Vehicle上传频率    5
    Run Keyword And Continue On Failure    设置雨刷状态    Stop
    Sleep    10
    Run Keyword And Continue On Failure    获取雨刷状态    expected=Off
    Sleep    1
    Run Keyword And Continue On Failure    设置雨刷状态    LowSpeed
    Sleep    10
    Run Keyword And Continue On Failure    获取雨刷状态    expected=On
    Sleep    1
    Run Keyword And Continue On Failure    设置雨刷状态    HighSpeed
    Sleep    10
    Run Keyword And Continue On Failure    获取雨刷状态    expected=On
    Sleep    1
    Run Keyword And Continue On Failure    设置雨刷状态    Interrupt
    Sleep    10
    Run Keyword And Continue On Failure    获取雨刷状态    expected=On
    Sleep    1
    Run Keyword And Continue On Failure    设置雨刷状态    Wash
    Sleep    10
    Run Keyword And Continue On Failure    获取雨刷状态    expected=On

变速箱状态
    等待连接成功
    设置Vehicle上传频率    5
    Run Keyword And Continue On Failure    设置变速箱状态    P
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=P
    Sleep    1
    Run Keyword And Continue On Failure    设置变速箱状态    R
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=R
    Sleep    1
    Run Keyword And Continue On Failure    设置变速箱状态    N
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=N
    Sleep    1
    Run Keyword And Continue On Failure    设置变速箱状态    D
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=D
    Sleep    1
    Run Keyword And Continue On Failure    设置变速箱状态    ManualGear1
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=ManualGear1
    Sleep    1
    Run Keyword And Continue On Failure    设置变速箱状态    ManualGear2
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=ManualGear2
    Sleep    1
    Run Keyword And Continue On Failure    设置变速箱状态    ManualGear3
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=ManualGear3
    Sleep    1
    Run Keyword And Continue On Failure    设置变速箱状态    S
    Sleep    10
    Run Keyword And Continue On Failure    获取变速箱状态    expected=S

车门状态
    等待连接成功
    设置Vehicle上传频率    5
    Run Keyword And Continue On Failure    设置左前门状态    Open
    Sleep    10
    Run Keyword And Continue On Failure    获取左前门状态    expected=Open
    Sleep    1
    Run Keyword And Continue On Failure    设置左前门状态    Close
    Sleep    10
    Run Keyword And Continue On Failure    获取左前门状态    expected=Close
    Sleep    1
    Run Keyword And Continue On Failure    设置右前门状态    Open
    Sleep    10
    Run Keyword And Continue On Failure    获取右前门状态    expected=Open
    Sleep    1
    Run Keyword And Continue On Failure    设置右前门状态    Close
    Sleep    10
    Run Keyword And Continue On Failure    获取右前门状态    expected=Close
    Sleep    1
    Run Keyword And Continue On Failure    设置左后门状态    Open
    Sleep    10
    Run Keyword And Continue On Failure    获取左后门状态    expected=Open
    Sleep    1
    Run Keyword And Continue On Failure    设置左后门状态    Close
    Sleep    10
    Run Keyword And Continue On Failure    获取左后门状态    expected=Close
    Sleep    1
    Run Keyword And Continue On Failure    设置右后门状态    Open
    Sleep    10
    Run Keyword And Continue On Failure    获取右后门状态    expected=Open
    Sleep    1
    Run Keyword And Continue On Failure    设置右后门状态    Close
    Sleep    10
    Run Keyword And Continue On Failure    获取右后门状态    expected=Close
    Sleep    1
    Run Keyword And Continue On Failure    设置后备箱状态    Open
    Sleep    10
    Run Keyword And Continue On Failure    获取后备箱状态    expected=Open
    Sleep    1
    Run Keyword And Continue On Failure    设置后备箱状态    Close
    Sleep    10
    Run Keyword And Continue On Failure    获取后备箱状态    expected=Close
    Sleep    1
    Run Keyword And Continue On Failure    设置门锁状态    Locked
    Sleep    10
    Run Keyword And Continue On Failure    获取门锁状态    expected=Locked
    Sleep    1
    Run Keyword And Continue On Failure    设置门锁状态    Unlock
    Sleep    10
    Run Keyword And Continue On Failure    获取门锁状态    expected=Unlock

空调状态
    等待连接成功
    设置Vehicle上传频率    5
    Run Keyword And Continue On Failure    设置空调状态    On
    Sleep    10
    Run Keyword And Continue On Failure    获取空调状态    expected=On
    Sleep    1
    Run Keyword And Continue On Failure    设置空调状态    Off
    Sleep    10
    Run Keyword And Continue On Failure    获取空调状态    expected=Off
    Sleep    1
    Run Keyword And Continue On Failure    设置前除霜状态    On
    Sleep    10
    Run Keyword And Continue On Failure    获取前除霜状态    expected=On
    Sleep    1
    Run Keyword And Continue On Failure    设置前除霜状态    Off
    Sleep    10
    Run Keyword And Continue On Failure    获取前除霜状态    expected=Off
    Sleep    1
    Run Keyword And Continue On Failure    设置后除霜状态    On
    Sleep    10
    Run Keyword And Continue On Failure    获取后除霜状态    expected=On
    Sleep    1
    Run Keyword And Continue On Failure    设置后除霜状态    Off
    Sleep    10
    Run Keyword And Continue On Failure    获取后除霜状态    expected=Off
    Sleep    1
    Run Keyword And Continue On Failure    设置空调温度    10.5
    Sleep    10
    Run Keyword And Continue On Failure    获取空调温度    expected=17.0
    Sleep    1
    Run Keyword And Continue On Failure    设置空调温度    25.5
    Sleep    10
    Run Keyword And Continue On Failure    获取空调温度    expected=25.5
    Sleep    1
    Run Keyword And Continue On Failure    设置空调温度    35.5
    Sleep    10
    Run Keyword And Continue On Failure    获取空调温度    expected=32.0

手刹状态
    等待连接成功
    设置Vehicle上传频率    5
    Run Keyword And Continue On Failure    设置手刹状态    Up
    Sleep    10
    Run Keyword And Continue On Failure    获取手刹状态    expected=Up
    Sleep    1
    Run Keyword And Continue On Failure    设置手刹状态    Down
    Sleep    10
    Run Keyword And Continue On Failure    获取手刹状态    expected=Down
