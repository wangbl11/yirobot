import traceback
import time
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC#具体介绍参考：https://blog.csdn.net/kelanmomo/article/details/82886718
from selenium.webdriver.support.wait import WebDriverWait
import json
from urllib.parse import quote


browser = webdriver.Chrome()
browser.implicitly_wait(100)
wait = WebDriverWait(browser,10)
url="https://lxdxb.tmall.com/search.htm"
flds=[ "name","value","path", "domain", "secure", "expiry"]
def add_cookies():
    with open('chrome_cookie.json','rb') as f:
        cookies=json.load(f)
        for item in cookies:
            _keys=list(item.keys())
            for key in _keys:
                if key not in flds:
                    del item[key]
            # print(item)
            browser.add_cookie(item)
def one_page():
    html=browser.page_source
    doc=7pq(html)

def loop_page():
    products=[]
    try:
       while True:
           _next=browser.find_element_by_xpath("//a[contains(@class,'ui-page-s-next')]")
           if _next.is_enabled():
               _next.click()
               time.sleep(15)
           else:
               break
    except Exception as e:
        traceback.print_exc()

if __name__=="__main__":
    browser.maximize_window()
    browser.get("https://www.taobao.com")
    add_cookies()
    # input = browser.find_element_by_id('q')
    # input.send_keys("ipad")
    # button = browser.find_element_by_class_name('btn-search')
    # button.click()
    browser.get(url)
    time.sleep(10)
    browser.refresh()
    time.sleep(10)
    loop_page()