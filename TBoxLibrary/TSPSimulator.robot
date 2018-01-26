*** Settings ***
Documentation     TSP模拟测试套件
Suite Teardown    Log Collection
Test Setup        initialize
Test Teardown     uninitialize
Library           TBoxLibrary.py
Resource          R.System/IMqttSystem.robot
Resource          R.RemoteConfigRequest/IRemoteConfig.robot

*** Test Cases ***
Demo
    等待连接成功
    Sleep    5
    设置Datamining上传频率    5
    Sleep    5
    设置Vehicle上传频率    10
