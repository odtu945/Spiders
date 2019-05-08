#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created Date: 2019-04-09
# Project     : crawl data of bidcenter.com.cn 

import sys
import requests
from lxml import etree
import urllib

def get_baidu_urls_by_keyword(vkeyword):
    vkeyword=vkeyword
    
    #wd 为查询关键字，lm代表搜索结果时间限制)以天为单位，例如搜索最近一个月的网页，lm=30.默认值为0,表示没有时间限制。 
    url = 'https://www.baidu.com/s?ie=utf-8&wd=' + urllib.parse.quote(vkeyword)# + '&lm=3' 

    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
             'Accept-Encoding': 'gzip, deflate, br',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Cookie': 'bidguid=09d0ae31-90e9-4d91-bae3-6a0a4cd44bdc; _uab_collina=155287009327192506718305; _umdata=G5D18F32E82CECF330D494AB726F58604B97D70; BIDCTER_USERNAME=UserName=13810757300; bidguidnew=5ed59a72-79db-4ecb-ae6a-faa09ae4c0b9; bidcurrKwdDiqu=kwd=èªç©º&diqu=35; Hm_lvt_9954aa2d605277c3e24cb76809e2f856=1552889439,1553218279,1553218350,1553758161; keywords==%e5%9b%bd%e7%94%b5; Hm_lpvt_9954aa2d605277c3e24cb76809e2f856=1554970538',
             'Referer': 'https://search.bidcenter.com.cn/',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    #url = "https://search.bidcenter.com.cn/search?keywords=%E6%B8%AF%E5%8A%A1%20%E5%8F%AF%E8%A7%86%E5%8C%96&type=1"
    #print(url)
    req = requests.get(url,headers=headers)
    #print(req.text)
    etree_data = etree.HTML(req.content)
    baidu_urls = etree_data.xpath("//h3/a/@href")
    return [requests.get(baidu_url,headers=headers,allow_redirects=False).headers['Location'] for baidu_url in baidu_urls]

if __name__ == '__main__':
    vkeyword='石浦一冷文化创意园中央空调设备（含安装）招标公告'
    print(get_baidu_urls_by_keyword(vkeyword))