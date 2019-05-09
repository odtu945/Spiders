#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created Date: 2019-04-09
# Project     : init db for spiders

import sqlite3

conn = sqlite3.connect('bid_datas.db')
cur = conn.cursor()
#create table
cur.execute('''
            CREATE TABLE bid_info(
            bid_md5_url TEXT PRIMARY KEY   -- 'url md5'
            ,bid_title TEXT -- '标题'
            ,bid_prov TEXT -- '省份'
            ,bid_create_date TEXT -- '招标网创建日期'
            ,bid_url TEXT -- 'url 地址'
            ,baidu_urls TEXT -- '百度检索后的地址'
            ,bid_content TEXT -- 'bid网站详细内容content'
            ,src_url TEXT -- '数据来源主页'
            ,bid_data_status TEXT --'数据状态'
            ,crawl_time TEXT -- '爬取时间'
            ,baidu_time TEXT -- '百度时间'
            ,email_time TEXT -- 'email时间'
            )
          ''')

conn.commit()
cur.close()
conn.close()
