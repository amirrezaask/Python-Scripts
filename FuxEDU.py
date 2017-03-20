# -*- coding: utf-8 -*-

import requests
import re

from mechanize import Browser
import Cookie

import cookielib
import urllib
import urllib2
from bs4 import BeautifulSoup
from sys import argv as arg
from PIL import Image
from cStringIO import StringIO
from pytesser import *

URL = 'https://edu.sharif.edu:3743/'
USER = arg[1]
PWD = arg[2]

cookiejar =cookielib.LWPCookieJar()
br = Browser()
br.set_cookiejar(cookiejar)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
login_page = br.open(URL + 'login.jsp')
login_soup = BeautifulSoup(login_page,'lxml')
captcha = login_soup.find('img')['src']


#OCR
img_file=urllib2.urlopen(URL + captcha)
img= StringIO(img_file.read())
checkImg= Image.open(img)
ocr_str= image_to_string(checkImg).lower()
CODE=''.join(ocr_str.split())
#End OF OCR
print 'Captcha Code Cracked ==> {}'.format(CODE)
print 'Please Don\'t Use Java It Sucks'
br.select_form(nr=0)
br['username'] = USER
br['password'] = PWD
br['jcaptcha'] = CODE
res = br.submit()
print 'Logged In Successfully'
print str(res.code) + ' <== Response Code'
