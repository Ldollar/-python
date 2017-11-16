#!/user/bin/env python
#coding=utf8
import os
import re
import subprocess

import time


class CmdContext():

    def __init__(self,cmd):
        self.cmd = cmd
    def __enter__(self):
        os.popen("adb wait-for-device")
        r = os.popen(self.cmd)
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
text = "11-14 21:05:19.749  1482  15"
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

command_push(cmd = 'some cmd ')