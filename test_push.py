#!/user/bin/env python
#coding=utf8
import os
import re
import subprocess

import time


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
    try:

        os.popen("adb wait-for-device")
        output = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        #time.sleep(5)

        while True:

            data = output.stdout.readline()
            #os.popen("adb wait-for-device")
            #r = os.system('adb -s 192.168.0.154:6555 logcat -v threadtime -s ZhixingDZVoltageMonitor')
            #time.sleep(5)
            #print data
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

#os.system('adb logcat -v threadtime -s ZhixingDZTemperatureMonitor')
#a= minus(timestamp="2017-11-15 11:52:50.449")-minus(timestamp="2017-11-15 11:52:48.429")
#print a
command_push(cmd = 'adb -s 192.168.0.154:6555 logcat -v threadtime -s ZhixingDZVoltageMonitor')
#match_string(rules=re1,text=text)
#2017-11-15 11:52:48.429
#2017-11-15 11:52:50.449