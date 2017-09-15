#!usr/bin/env python
# -*- coding:utf-8 -*-
import re


def find_code(text=None):
    #page = '{"res":[{"creator":"search","name":"微风往事","type":2,"description":"感谢各位的收听和关注。 《微风往事》为线下多个调频广播的音乐情感伴随类节目的精编版，所有歌曲按音乐类电台的要求全部完整播放。 《微风往事》每日在地面频率播出的时间如下： 【深圳优悦FM105.7】 22:00-23:00， 【湖南优悦FM94.5】/【海口音乐FM91.6】/【 贵阳音乐FM90.9】/ 【石家庄优悦FM106.2】以上四台均为 20:00-21:00 唐山FM98.4 17：00-18：00","iconUrl":"http://fdfs.xmcdn.com/group4/M02/3C/6F/wKgDtFNHoCrAOFbbAAE2PrXoY9E149_mobile_meduim.jpg","sourceId":"249163","announcerId":"1450037"},{"creator":"search","name":"王健林 马云 周星驰 雷军 刘德华 梁凯恩 成功经验","type":2,"description":"专辑罗列 成功名人 创业 经商 销售经验 帮助同僚获得经验少走弯路","iconUrl":"http://fdfs.xmcdn.com/group19/M0A/D1/9C/wKgJJlfHvYSzvKyUAAOmsfvF7ZY514_mobile_meduim.jpg","sourceId":"5154639","announcerId":"55665669"},{"creator":"search","name":"世界童话","type":2,"description":"每天读一个","iconUrl":"","sourceId":"3244006","announcerId":"16930537"}],"message":"success","code":0}'
    #text = '{"code":-1000,"message":"Unknown Error","ch":"未知错误"}'
    rule = '"code":(\D?\d+)'
    pattern = re.compile(rule)
    result = re.findall(pattern,text)
    code_find = result[0]
    #print code_find
    return code_find
#find_code()