#!/usr/bin/env python3
import os
import re
import sys
import time
import random
import pyexiv2
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#By BC van Zuiden -- Leiden, November 2016 */
#Probably very buggy USE AT OWN RISK this will brick everything you own */
#NOBODY but YOU is liable for anything that happened in result of using this */
#WARNING: DON'T RUN THIS PROGRAM THIS WILL DESTROY YOUR COMPUTER AND/OR HOUSE */
#Any copyrighted piece of code within this code is NOT mine */
#Inclusion of that code is forced upon me by a scary anonymous guy with a gun*/

def printf(format, *args):
    sys.stdout.write(format % args)

def url_proccessor(url):
    ua=UserAgent()
    req=Request(url,data=None,headers={'User-Agent': ua.random})
    if(url[-1]!='/'):
        url+='/'
    printf("Crawling over: %s\n",url)
    try:
        page=urlopen(req)
    except:
        return [],[]
    else:
        html=BeautifulSoup(page.read(),"html.parser")
        links=[urljoin(url,link['href']) for link in html.find_all('a',href=re.compile(r"^(?!mailto:|javascript:)",re.IGNORECASE))]
        imgs=[urljoin(url,img['src']) for img in html.find_all('img',src=True)]
        return links,imgs

def get_exif(url):
    datafile=""
    try:
        datafile=urlretrieve(url)[0]
        metadata=pyexiv2.ImageMetadata(datafile)
        metadata.read()
        md=dict(metadata.items())
        printf("GPS Coordinates of %s found:\t%s %s %s %s\n",url,md['Exif.GPSInfo.GPSLatitude'].human_value.replace("deg","°"),md['Exif.GPSInfo.GPSLatitudeRef'].human_value[0],md['Exif.GPSInfo.GPSLongitude'].human_value.replace("deg","°"),md['Exif.GPSInfo.GPSLongitudeRef'].human_value[0])
    except:
        pass
    if(len(datafile)>0):
        os.remove(datafile)

start_url="http://www.randomwebsite.com/cgi-bin/random.pl"
depth=1
if(len(sys.argv)>1):
    depth=int(sys.argv[1])
    if(len(sys.argv)>2):
        start_url=sys.argv[2]
urlset=set({start_url})
urlsdone=set({})
imgsdone=set({})
for i in range(depth):
    url=set(random.sample(urlset,1))
    urlset=urlset-url
    urlsdone=urlsdone.union(url)
    links,imgs=url_proccessor(next(iter(url)))
    for img in imgs:
        if(not img in imgsdone):
            get_exif(img)
    imgsdone=imgsdone.union(set(imgs))
    urlset=urlset.union(set(links)-urlsdone)
