#!/usr/bin/env bash

# Copyright (C) 2015-2018 Shenzhen Auto-link world Information Technology Co., Ltd.
# All Rights Reserved
#
# Name: Config.py
# Purpose:
#
# Created By:    Clive Lau <liuxusheng@auto-link.com.cn>
# Created Date:  2017-02-02
#
# Changelog:
# Date         Desc
# 2017-02-02   Created by Clive Lau

DESKTOP_DIR=$HOME/Desktop
LIBRARY_DIR=`pwd`/TBoxLibrary
OUTPUT_DIR=${DESKTOP_DIR}/`date +%Y%m%d`_Sherlock-TBox
DEV_OUTPUT_DIR=${OUTPUT_DIR}/dev_log

########################################

function info () {
	echo -e "\033[0;31;1mInfo:\033[0m $1"
}

function error () {
	echo -e "\033[0;31;1mError:\033[0m $1"
	exit 255
}

########################################

info "Starting to stress test......"

mkdir -p ${DEV_OUTPUT_DIR}

count=1

while [ $? -eq 0 ]; do
	info ${count}......$?
	count=$((count + 1))
	#retval=`robot -d ${OUTPUT_DIR} ${LIBRARY_DIR}/TSPSimulator.robot 2>&1 | tee ${OUTPUT_DIR}/console.log`
	robot -d ${OUTPUT_DIR} ${LIBRARY_DIR}/
done

# DevLog Collection
#adb logcat -d -b mcu -f ${DEV_OUTPUT_DIR}/mcu.log
#adb logcat -d -b mpu -f ${DEV_OUTPUT_DIR}/mpu.log
#adb logcat -d -b system -f ${DEV_OUTPUT_DIR}/system.log
#adb logcat -d -b tsp -f ${DEV_OUTPUT_DIR}/tsp.log

error "Failed to stress test!!!"
