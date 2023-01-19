import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary
import time
import pandas as pd
import requests
import csv
import os
import datetime
import slackweb

def data_update():
    url = 'https://www.ibm.com/docs/ja/szs/2.2?topic=release-notes'
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)


    driver.get(url)

    time.sleep(10)


    html = driver.page_source

    values = driver.find_element_by_id("lastModifiedDate")
    current_value = values.text
    return current_value

def output_txt(result):
    with open('last_log.txt', 'w',encoding='utf_8') as f:
        print(result, file=f)

def read_txt():
    if not os.path.exists('last_log.txt'):
        result = data_update() # 新規のニュースを取得
        output_txt(result) # 保存データを更新
        raise Exception('ファイルがありません。')
    if os.path.getsize('last_log.txt') == 0:
        result = data_update() # 新規のニュースを取得
        output_txt(result) # 保存データを更新
        raise Exception('ファイルの中身が空です。')
    with open('last_log.txt', 'r' ,encoding='utf_8') as f:
      result = f.readlines()
    return result[0]

def send_to_slack():
    now = datetime.datetime.now()
    now = now.strftime("%Y/%m/%d %H:%M:%S")
    text = now + '\n' + "リリースノートに更新がありました"
    slack  = slackweb.Slack(url='https://hooks.slack.com/services/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')
    slack.notify(text=text)

# main
if __name__ == '__main__':
    last_result = read_txt() # 以前の保存データを参照
    result = data_update() # 新規のニュースを取得
    last_result = last_result.split("\n")[0]
    if last_result != result:
      output_txt(result) # 保存データを更新
      send_to_slack() # 差異があればSLACKに通知する