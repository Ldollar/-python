#!usr/bin/env python
# -*- coding:utf-8 -*-
import json
import re

import logging

from define_log import LogDefine
from test_case.public.decorated_learn import logged


def find_code(text=None,rex_str=None):
    #page = '{"res":[{"creator":"search","name":"微风往事","type":2,"description":"感谢各位的收听和关注。 《微风往事》为线下多个调频广播的音乐情感伴随类节目的精编版，所有歌曲按音乐类电台的要求全部完整播放。 《微风往事》每日在地面频率播出的时间如下： 【深圳优悦FM105.7】 22:00-23:00， 【湖南优悦FM94.5】/【海口音乐FM91.6】/【 贵阳音乐FM90.9】/ 【石家庄优悦FM106.2】以上四台均为 20:00-21:00 唐山FM98.4 17：00-18：00","iconUrl":"http://fdfs.xmcdn.com/group4/M02/3C/6F/wKgDtFNHoCrAOFbbAAE2PrXoY9E149_mobile_meduim.jpg","sourceId":"249163","announcerId":"1450037"},{"creator":"search","name":"王健林 马云 周星驰 雷军 刘德华 梁凯恩 成功经验","type":2,"description":"专辑罗列 成功名人 创业 经商 销售经验 帮助同僚获得经验少走弯路","iconUrl":"http://fdfs.xmcdn.com/group19/M0A/D1/9C/wKgJJlfHvYSzvKyUAAOmsfvF7ZY514_mobile_meduim.jpg","sourceId":"5154639","announcerId":"55665669"},{"creator":"search","name":"世界童话","type":2,"description":"每天读一个","iconUrl":"","sourceId":"3244006","announcerId":"16930537"}],"message":"success","code":0}'
    #text = '{"code":-1000,"message":"Unknown Error","ch":"未知错误"}'
    rule = '"'+rex_str+'":(\D?\d+)'
    pattern = re.compile(rule,re.I)
    result = re.findall(pattern,text)
    code_find = result[0]
    #print code_find
    return code_find
#find_code()
@logged
def find_message(res=None,res_str_zhongwen=None):
    rule = '"'+res_str_zhongwen+'":"([\S\s]+?)","'  # CSV文件是否添加双引号问题
    #rule = "u'" + res_str_zhongwen + "':u'([\S\s]{0,25})',"  #单双引号
    #rule = res_str_zhongwen + ':([\S\s]{0,25}),'  #匹配长度需要定义，可能匹配的长度为多少，此rule匹配csv文件的assert_message 不用再添加“"”
    pattern = re.compile(rule,re.I)
    result = re.findall(pattern, res)
    if len(result)>0:
        return result[0]
        print "find_message:",result
    else:
        return None
#返回一个list
@logged
def match_string(rules=None,text=None):
    try:
        pattern = re.compile(rules,re.I)
        result = re.match(pattern,text)
        get_type_MM=result.group(1)
        return get_type_MM.split(",")
    except Exception,e:
        logging.warning("warning %s",e)
        return None


#page = '{"res":[{"creator":"search","version":"1.1.1","type":2,"description":"感谢各位的收听和关注。 《微风往事》为线下多个调频广播的音乐情感伴随类节目的精编版，所有歌曲按音乐类电台的要求全部完整播放。 《微风往事》每日在地面频率播出的时间如下： 【深圳优悦FM105.7】 22:00-23:00， 【湖南优悦FM94.5】/【海口音乐FM91.6】/【 贵阳音乐FM90.9】/ 【石家庄优悦FM106.2】以上四台均为 20:00-21:00 唐山FM98.4 17：00-18：00","iconUrl":"http://fdfs.xmcdn.com/group4/M02/3C/6F/wKgDtFNHoCrAOFbbAAE2PrXoY9E149_mobile_meduim.jpg","sourceId":"249163","announcerId":"1450037"},{"creator":"search","name":"王健林 马云 周星驰 雷军 刘德华 梁凯恩 成功经验","type":2,"description":"专辑罗列 成功名人 创业 经商 销售经验 帮助同僚获得经验少走弯路","iconUrl":"http://fdfs.xmcdn.com/group19/M0A/D1/9C/wKgJJlfHvYSzvKyUAAOmsfvF7ZY514_mobile_meduim.jpg","sourceId":"5154639","announcerId":"55665669"},{"creator":"search","name":"世界童话","type":2,"description":"每天读一个","iconUrl":"","sourceId":"3244006","announcerId":"16930537"}],"message":"success","code":0}'
#page1 ='{"res": [],"message": "success","code": 0}'
#page2 ='{"code": -916,"message": "no available ota","ch": "无可用更新"}'
#page3 = "{u'ch': u'\u6210\u529f', u'res': {u'unzip': [{u'checksum': u'1f41ec310d01602dc2d50b6549fa546a', u'packageName': u'com.tuyou.tsd.bluetooth', u'size': 14374, u'fileName': u'01_bluetooth_1507548138.patch'}, {u'checksum': u'd3dbd752f12a252a9353c5435f2a5ed0', u'packageName': u'com.tuyou.tsd.audio', u'size': 151818, u'fileName': u'02_audio_1507548172.patch'}, {u'checksum': u'01692869460188779f7016aa7361eb36', u'packageName': u'com.tuyou.tsd.cardvr', u'size': 64237, u'fileName': u'03_cardvr_1507548146.patch'}, {u'checksum': u'778302d4334f329cd2b69db7e5d95f78', u'packageName': u'com.tuyou.tsd.collector', u'size': 14406, u'fileName': u'04_collector_1507548153.patch'}, {u'checksum': u'8d25b6e839278155495a78f86b7477b5', u'packageName': u'com.tuyou.tsd.dday.mediaserver', u'size': 54975, u'fileName': u'05_mediaserver_1507548161.patch'}, {u'checksum': u'f87ea6a01c88a03e43acb0668d02287e', u'packageName': u'com.tuyou.tsd.podcast', u'size': 56890, u'fileName': u'10_podcast_1507548182.patch'}, {u'checksum': u'1ebf0fb62725a5be53bab95eaeed1aea', u'packageName': u'com.tuyou.tsd.settings', u'size': 66059, u'fileName': u'11_settings_1507548192.patch'}, {u'checksum': u'12c5c4400f5c2e81da8a58a76ec3cfa2', u'packageName': u'com.tuyou.tsd.voice', u'size': 55628, u'fileName': u'13_voice_1507548204.patch'}, {u'checksum': u'ea9bc5ff06abd4485fc4b0bfc5ffd981', u'packageName': u'com.tuyou.tsd', u'size': 8273316, u'fileName': u'98_tsd_1507548244.patch'}, {u'checksum': u'b895326e27061d1167848a54116ed9ca', u'packageName': u'com.tuyou.tsd.updatesoft', u'size': 60451, u'fileName': u'99_updatesoft_1507548260.patch'}], u'apkVersion': u'1.2.5', u'description': u'i am a patch', u'installMode': [u'accoff'], u'url': u'http://otzljax03.bkt.clouddn.com/patch_1.2.5_0.1.2_20171011000050.zip?a=1', u'checksum': u'c8111c36004d3d359a52d8bb56be8d60', u'strategy': {u'retryCount': 3, u'mode': {u'accon': {u'cancel': [u'accoff', u'user'], u'delayTime': 30}, u'accoff': {u'cancel': [u'accon', u'user'], u'delayTime': 30}, u'instant': {u'cancel': [u'accoff', u'user'], u'delayTime': 5}, u'manual': {u'cancel': [u'accoff', u'user'], u'delayTime': 0}}, u'space': {u'signal': u'com.tuyou.tsd.size.warning', u'limit': 524288000}}, 'deviceAppVersion': '1.2.5', 'version': '0.1.2', 'installDoneOperator': 'reboot', 'size': 8794690, 'type': 'patch', 'name': 'patch update'}, 'message': 'success', 'code': 0}"
#page4 = page3.encode("utf-8")
#print str(page4)
#z=find_message(res=page4,res_str_zhongwen="version" )
#print z
#a=match_string(rules="random\\((\S+)\\)",text="random(1,2,3)")
#print a



