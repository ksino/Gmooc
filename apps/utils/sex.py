# -*- coding: utf-8 -*-


import requests, re, random, time, os, csv
from bs4 import BeautifulSoup as bs
from parsel import Selector
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')
#print sys.getdefaultencoding()
file = open('sex_real.txt','a+')

def download_urls(filename):
    file_object = open(filename)
    try:
         html = file_object.read( )
    finally:
         file_object.close( )
    obj = bs(html, 'html.parser')
    lists = obj.find_all('div', {'class': re.compile('post.*?')})
    d={}
    listurl=[]
    x = 0

    for i in lists:
        try:
            x += 1
            a = i.find('a')
            video_url = a.attrs['href']
            img_url = a.find('img').attrs['src']
            title = a.find('img').attrs['alt']
            mp4url = download_mp4(video_url)
            # c = i.find('div')
            # divid = c.attrs['id']
            # print(video_url, img_url, title, divid)
            dicturl = d.copy()
            dicturl['video']=video_url
            dicturl['image']=img_url
            dicturl['title']='{0}. {1}'.format(str(x),title)
            dicturl['mp4']=mp4url

            # dicturl['id']=divid
            listurl.append(dicturl)

            print x
            # file.write(json_str)



        except:
            continue
    json.dump(listurl,file, indent = 4)


def download_mp4(url):
    r = requests.get(url, timeout=30)
    r.encoding = 'utf-8'
    html = r.text
    obj = bs(html, 'html.parser')
    lists = obj.find_all('video')
    for i in lists:
        try:
            a = i.find('a')
            video_url = a.attrs['href']

            print(video_url)


        except:
            continue


    return (video_url)

download_urls('sex.html')


file.close()
