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
import pytesser


def read_captcha(url, captcha):
    img_file = urllib2.urlopen(url + captcha)
    img = StringIO(img_file.read())
    checkImg = Image.open(img)
    ocr_str = pytesser.image_to_string(checkImg).lower()
    return ''.join(ocr_str.split())


def main():
    URL = 'https://edu.sharif.edu:3743/'
    USER = arg[1]
    PWD = arg[2]

    cookiejar = cookielib.LWPCookieJar()
    br = Browser()
    br.set_cookiejar(cookiejar)
    br.addheaders = [
        ("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
    login_page = br.open(URL + 'login.jsp')
    login_soup = BeautifulSoup(login_page, 'lxml')
    captcha = login_soup.find('img')['src']
    # OCR read
    code = read_captcha(URL, captcha)
    print('Captcha Code Cracked ==> {}'.format(code))
    br.select_form(nr=0)
    br['username'] = USER
    br['password'] = PWD
    br['jcaptcha'] = code
    res = br.submit()
    print('Logged In Successfully')
    print(str(res.code) + ' <== Response Code')


if __name__ == '__main__':
    main()
