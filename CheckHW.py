# -*- coding: utf-8 -*-
import requests
import sys
import re
from mechanize import Browser
import Cookie
import cookielib
from bs4 import BeautifulSoup
student_page = requests.get("http://kish.sharif.edu/bs_email_tic.php")



#print student_page.text
cookiejar =cookielib.LWPCookieJar()
br = Browser()
br.set_handle_robots(False)
br.set_cookiejar(cookiejar)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
sign_in = br.open("http://cw.sharif.ir/login/index.php")
br.select_form(nr=0)
br["username"]= sys.argv[1]
br["password"]= sys.argv[1]
logged_in = br.submit()
br2 = Browser()
br2.set_handle_robots(False)
br2.set_cookiejar(cookiejar)
br2.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
sign_in2 = br2.open("http://cw.sharif.ir/mod/assign/view.php?id=68716")
page = sign_in2.read()
soup = BeautifulSoup(page,"html.parser")
if ".pdf" in page:
    print "Uploaded !"
    for link in br2.links(url_regex=".pdf"):
        br2.retrieve(link.url,"hw_{}.pdf".format(sys.argv[1]))

else:
    print "not Uploaded yet"
