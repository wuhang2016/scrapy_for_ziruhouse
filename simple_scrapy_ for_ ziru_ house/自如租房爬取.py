from bs4 import BeautifulSoup
import requests
import time
import pickle
import os
import sys
import re  
import urllib

#报文头部，能够增大权限，
headers={
    'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    'Cookies':"CURRENT_CITY_CODE=110000; gr_user_id=3ef647eb-7b49-42a7-a3e2-ea1b65bfeb82; __utma=18275762.1448208101.1525262809.1525262809.1525262809.1; __utmz=18275762.1525262809.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); search_history=%5B%22%5Cu547c%5Cu5bb6%5Cu697c%5Cu65b0%5Cu82d13%5Cu5c45%5Cu5ba4%22%2C%22%5Cu547c%5Cu5bb6%5Cu697c%5Cu65b0%5Cu82d13%5Cu5c45%5Cu5ba4%5Cu5357%5Cu5367%22%5D; gr_session_id_8da2730aaedd7628=fb3da463-f4a8-463f-ba49-dbee8c50e521_true; Hm_lvt_038002b56790c097b74c818a80e3a68e=1525261923,1525269460,1525419066; PHPSESSID=q01s3ru877e8mrgq6gfehi40c3; CURRENT_CITY_NAME=%E5%8C%97%E4%BA%AC; passport_token=98c9e2c8-024e-4442-a268-75b79625652c; uid=6c2d1a26-1374-41c4-9229-c48522083b0e; Hm_lpvt_038002b56790c097b74c818a80e3a68e=1525420700"
}

url='http://www.ziroom.com/z/vr/61208265.html'
#用lxml包读取html元素
wb_data=requests.get(url,headers=headers)  
soup=BeautifulSoup(wb_data.text,'lxml')
title=soup.select('body > div.area.clearfix > div.room_detail_left > div.greatRoommate > ul > li:nth-of-type(1) > div > div.user_top.clearfix > span')
a = "".join('%s' %id for id in title)
print(a)
#刷新页面，不断判断是否状态更新
while(True):
  if ("配置中" in a):
       time.sleep(1)
  else:
       os.system("自如爬虫.py")
       break
       time.sleep(1)

       
    
      

    


