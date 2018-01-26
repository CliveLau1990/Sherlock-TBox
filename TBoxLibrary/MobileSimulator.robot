*** Settings ***
Documentation     手机模拟测试套件
Test Setup        initialize
Test Teardown     uninitialize
Library           TBoxLibrary.py
Resource          R.System/IMqttSystem.robot
Resource          R.RemoteControlCommand/IAircondition.robot

*** Test Cases ***
Aircondition
    [Documentation]    空调
    Log    Aircondition

CentralLocking
    [Documentation]    中控锁
    Log    CentralLocking

FindVehicle
    [Documentation]    寻车
    Log    FindVehicle

Engine
    [Documentation]    发动机
    Log    Engine
