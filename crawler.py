import time
import requests
import csv
from selenium import webdriver

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
    chrome = webdriver.Chrome(r'chromedriver.exe')
    chrome.get(url)
    script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
    chrome.execute_script(script)
    time.sleep(2)
    for i in range(1, 11):
        for j in range(1, 51):
            # selenium通过xpath定位获取数据
            rank = chrome.find_element_by_xpath('//*[@id="table1"]/tbody/tr[{}]/td[1]'.format(j)).text
            company = chrome.find_element_by_xpath('//*[@id="table1"]/tbody/tr[{}]/td[2]/a'.format(j)).text
            income = chrome.find_element_by_xpath('//*[@id="table1"]/tbody/tr[{}]/td[3]'.format(j)).text
            profit = chrome.find_element_by_xpath('//*[@id="table1"]/tbody/tr[{}]/td[4]'.format(j)).text
            nation = chrome.find_element_by_xpath('//*[@id="table1"]/tbody/tr[{}]/td[5]'.format(j)).text
            # 追加写入csv
            with open(r'Fortune500.csv', 'a+', encoding='utf-8') as f:
                row = [rank, company, income, profit, nation]
                writer = csv.writer(f)
                writer.writerow(row)
                print(row)
        nextPage = chrome.find_element_by_xpath('//*[@id="table1_next"]')
        nextPage.click()


if __name__ == '__main__':
    crawler()
