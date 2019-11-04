from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

from pyquery import PyQuery as pq
import pymongo
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.implicitly_wait(50) 

# browser = webdriver.Chrome()
wait = WebDriverWait(browser, 50)
KEY_WORD = '白板'

def index_page(page):
    '''
    抓取索引页
    :param page: 待抓取步骤。
    '''
    if page < 0:
        return
    print('正在爬取第 ', page, '页')

    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEY_WORD)
        browser.get(url)

        # <input class="input J_Input" type="number" value="2" min="1" max="100" aria-label="页码输入框">
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page)
        submit.click()

        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))

        get_products()

    except TimeoutException:
        index_page(page)


def get_products():
    '''
    get products details

    '''
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'deal':item.find('.deal-cnt').text(),
            'price':item.find('.price').text().replace('\n', ' '),
            'title':item.find('.title').text().replace('\n', ' '),
            'image':item.find('.pic .img').attr('data-src'),
            'location':item.find('.location').text(),
            'href':item.find('.pic .a').attr('href'),
            'shop':item.find('.shop').text()
        }
        print(product)
        save_to_mongo(product)

MONGO_URL = 'mongodb://127.0.0.1:27018/'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert_one(result):
            print('Save to MongoDb successfully.')
        for item in db[MONGO_COLLECTION].find():
            print("item-info: ",item)
    except Exception:
        print('Failed to save MongoDb.')

def main():
    MAX_PAGE = 100
    for i in range(1, 1+MAX_PAGE):
        index_page(i)

        print('完成爬取第 ', i, '页...')
        time.sleep(30)

if __name__ == '__main__':
    # main()
    i = 0
    for item in db[MONGO_COLLECTION].find():
        print("item-info: ",item)
        i += 1
    print(i)