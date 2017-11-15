#!/user/bin/env python
#coding=utf8
import os
import re
import subprocess

import time

import requests


class CmdContext():

    def __init__(self):
        pass
    def __enter__(self):
        os.popen("adb wait-for-device")
        r = os.popen('adb -s 192.168.0.154:6555 logcat -v threadtime -s ZhixingDZVoltageMonitor')
        return r

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "__exit__ zhixingla"
        #return True
def command_push(cmd):
    # aaaa = CmdContext()
    # with aaaa as output:
    #     print output.newlines
    tmp = ""
    count =1
    stop = 0
    try:

        os.popen("adb wait-for-device")
        output = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        #time.sleep(5)

        while True:
            stop = stop +1
            data = output.stdout.readline()
            aaa = match_string(rules=re1,text=data)
            bbb = ite11(itera=aaa)
            print bbb
            if bbb:
                if count == 1:
                    tmp=bbb
                    count = 0
                else:
                    xxx=minus(timestamp=bbb) - minus(timestamp=tmp)
                    tmp=bbb
                    print xxx
            if stop > 60 :
                break
        time.sleep(5)
    except Exception,e:
        print e

re1 = "\d*-\d*\s[\d+:]+.\d{0,3}"
text = "11-14 21:05:19.749  1482  1518 E ZhixingDZVoltageMonitor: voltage :null (NOT main thread) 11-14 21:05:39.799  1482  "
def match_string(rules,text):
    try:
        pattern = re.compile(pattern=rules)
        #print pattern
        result = re.findall(pattern,text)
        #print result
        return result
        #return get_type_MM.split(",")
    except Exception,e:
        print e

def minus(timestamp='2017-11-15 11:20:47.579'):
    a = time.mktime(time.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f'))
    #print a
    return a
def  ite11(itera):
    for i in itera:
        #print i
        time123 = "2017-"+i
        return time123
def push_mqtt(data1):
    res = requests.post(url="http://www.aituyou.com:12112/api/v1/push/mqtt",json=data1,)
    print res.content

#command_push(cmd = 'adb -s 192.168.0.154:6555 logcat -v threadtime -s ZhixingDZVoltageMonitor')

def make_json_data(interval):
    json_data = {   "key": "xb.dz.device.unique.354008079843400",
        "messageId": "25b2fa5a-affe-4992-830c-838befd18c40",
        "timestamp": 1509606294000,
        "expire": 0,
        "type": "push",
        "content": "{\"action\":\"com.tuyou.tsd.coeus.os.voltage.interval\",\"dataLongs\":{\"interval\":\""+interval+"\"}}",
        "ack": "true",
        "ackTopic": "feedback",
        "ch": "终端推送消息"
    }
    return json_data

def main():
    cmd1 = 'adb -s 192.168.0.154:6555 logcat -v threadtime -s ZhixingDZVoltageMonitor'
    for i in ["2000","5000","1000","3000","10000"]:
        json1 = make_json_data(interval=i)
        push_mqtt(data1=json1)
        print u"现在 Voltage %s 毫秒 更新一次"%i
        command_push(cmd=cmd1)
        print "over over over over "

main()