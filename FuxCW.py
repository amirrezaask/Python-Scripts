import sys
import re
from mechanize import Browser
import Cookie
import cookielib
import requests


def main():
    cookiejar = cookielib.LWPCookieJar()
    br = Browser()
    br.set_handle_robots(False)
    br.set_cookiejar(cookiejar)
    br.addheaders = [
        ("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
    sign_in = br.open("http://cw.sharif.ir/login/index.php")
    br.select_form(nr=0)
    br["username"] = sys.argv[1]
    br["password"] = sys.argv[2]
    logged_in = br.submit()
    print("Logged In Successfully")
    print("Starting Phase 2")

    br2 = Browser()
    br2.set_handle_robots(False)
    br2.set_cookiejar(cookiejar)
    br2.addheaders = [
        ("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
    sign_in2 = br2.open("http://cw.sharif.ir/login/change_password.php")
    br2.select_form(nr=0)
    br2["password"] = sys.argv[2]
    br2["newpassword1"] = sys.argv[3]
    br2["newpassword2"] = sys.argv[3]
    logged_in2 = br2.submit()
    logincheck = logged_in2.read()


if __name__ == '__main__':
    main()
