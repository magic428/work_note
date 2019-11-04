<<<<<<< Updated upstream
#coding=utf-8

import os
import sys
import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from lxml import etree
import requests
import time

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        }

def save_img(image_url_list):
    for i, image_url in enumerate(image_url_list):
        ext = os.path.splitext(image_url)[1]   # .jpg/ .png
        image_name = "{}_{:>05}{}".format(key_word, (i), ext)
        with open(save_dir + image_name, "wb") as f:
            content = requests.get(image_url, headers=headers).content
            f.write(content)


# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
key_word = "beauty"
kw = "陈钰琪"

home_dir = os.getenv("HOME")
save_dir = "{}/work/spider/{}/".format(home_dir, key_word) 
print(save_dir)

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

url = "https://image.baidu.com/search/index?tn=baiduimage&word="

kw = urllib.parse.quote(kw)

driver.get(url + kw)
# 执行JS语句
# js = "document.body.scrollTop=10000"
# js = "var q=document.documentElement.scrollTop=100000"
# driver.execute_script(js)
# 拖动到顶部
# driver.execute_script("window.scrollTo(0,0)")
# 调用JS代码拖动滚动条
# driver.execute_script("window.scrollTo(0,1680)")
# 直接拖动到底部
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

image_url_list = []
pre_len = 0
length = 0
print ('press Ctrl+c to quit')

while True:

    try:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        selector = etree.HTML(driver.page_source)
        # already failed
        image_url_list = selector.xpath('//div[@class="imgbox"]//@data-imgurl')
        print(pre_len, len(image_url_list), sep=', ')
        length = pre_len
        pre_len += len(image_url_list)
        # print(image_url_list)
        if (length == pre_len):
            #save_img(image_url_list)
            break
        else: 
            pre_len = len(image_url_list)

        # 保存到本地文件
    except KeyboardInterrupt:
        print(len(image_url_list))
        # 退出
        breaks
    save_img(image_url_list)
=======
#coding=utf-8

import os
import sys
import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from lxml import etree
import requests
import time

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        }

def save_img(image_url_list):
    for i, image_url in enumerate(image_url_list):
        ext = os.path.splitext(image_url)[1]   # .jpg/ .png
        image_name = "{}_{:>05}{}".format(key_word, (i), ext)
        with open(save_dir + image_name, "wb") as f:
            content = requests.get(image_url, headers=headers).content
            f.write(content)


# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
key_word = "beauty"
kw = "佟丽娅"

home_dir = os.getenv("HOME")
save_dir = "{}/work/spider/{}/".format(home_dir, key_word) 
print(save_dir)

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

url = "https://image.baidu.com/search/index?tn=baiduimage&word="

kw = urllib.parse.quote(kw)

driver.get(url + kw)
# 执行JS语句
# js = "document.body.scrollTop=10000"
# js = "var q=document.documentElement.scrollTop=100000"
# driver.execute_script(js)
# 拖动到顶部
# driver.execute_script("window.scrollTo(0,0)")
# 调用JS代码拖动滚动条
# driver.execute_script("window.scrollTo(0,1680)")
# 直接拖动到底部
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

image_url_list = []
pre_len = 0
print ('press Ctrl+c to quit')

while True:

    try:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        selector = etree.HTML(driver.page_source)
        image_url_list = selector.xpath('//div[@class="imgbox"]//@data-imgurl')
        print(pre_len, len(image_url_list), sep=', ')
        # print(image_url_list)
        if (len(image_url_list) == pre_len):
            save_img(image_url_list)
            break
        else: 
            pre_len = len(image_url_list)

        # 保存到本地文件
    except KeyboardInterrupt:
        print(len(image_url_list))
        save_img(image_url_list)
        # 退出
        break
>>>>>>> Stashed changes
