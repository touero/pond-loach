import select
import time
import requests
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 目标网址，构造头部信息
url = 'https://www.fortunechina.com/fortune500/c/2021-08/02/content_394571.htm'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.71 '
                  'Safari/537.36 Edg/97.0.1072.55 '
}


def crawler():
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('access failed')
        return
    chrome = webdriver.Chrome(r'./chromedriver')
    chrome.maximize_window()
    chrome.get(url)
    script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
    chrome.execute_script(script)
    time.sleep(2)
    select_element = chrome.find_element(By.XPATH, '//select[@name="table1_length"]')
    Select(select_element).select_by_value('-1')
    time.sleep(1)
    rows = chrome.find_elements(By.XPATH, '//tbody/tr[@role="row"]')
    for row in rows:
        rank = row.find_element(By.XPATH, './td[1]').text
        company = row.find_element(By.XPATH, f'./td[2]/a').text
        income = row.find_element(By.XPATH, './td[3]').text
        profit = row.find_element(By.XPATH, './td[4]').text
        nation = row.find_element(By.XPATH, './td[5]').text

        with open(r'Fortune500.csv', 'a+', encoding='utf-8') as f:
            row = [rank, company, income, profit, nation]
            writer = csv.writer(f)
            writer.writerow(row)
            print(row)

if __name__ == '__main__':
    crawler()
