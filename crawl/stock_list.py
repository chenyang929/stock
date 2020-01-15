import time
import csv
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DETAIL_URLS = list()

def req_list(driver):
    d = str(datetime.now().date())
    dr = "d:/stock/{}".format(d)
    os.mkdir(dr)
    with open("{}/list_{}.csv".format(dr,d), "w", encoding="utf-8", newline='') as f:
        w = csv.writer(f)
        w.writerow(["序号","行业","行业指数","涨跌幅","流入资金(亿)","流出资金(亿)","净额(亿)","公司家数","领涨股","涨跌幅","当前价","链接"])
        driver.get("http://data.10jqka.com.cn/funds/hyzjl/")
        time.sleep(5)
        list_table_info(driver,w)
        next_page = get_next_page(driver)
        while len(next_page) > 0:
            next_page[0].click()
            time.sleep(5)
            list_table_info(driver,w)
            next_page = get_next_page(driver)


# def list_table_head(driver):
#     tr = driver.find_element_by_xpath('//table[contains(@class,"J-ajax-table")]/thead/tr')
#     xuhao = tr.find_element_by_xpath('.//th[1]').text
#     hangye = tr.find_element_by_xpath('.//th[2]/a').text
#     zhishu = tr.find_element_by_xpath('.//th[3]/a').text
#     zs_zhangdie = tr.find_element_by_xpath('.//th[4]/a').text
#     liuru = tr.find_element_by_xpath('.//th[5]/a').text
#     liuchu = tr.find_element_by_xpath('.//th[6]/a').text
#     jine = tr.find_element_by_xpath('.//th[7]/a').text
#     gongsi = tr.find_element_by_xpath('.//th[8]/a').text
#     lingzhang = tr.find_element_by_xpath('.//th[9]/a').text
#     lz_zhangdie = tr.find_element_by_xpath('.//th[10]/a').text
#     lz_price = tr.find_element_by_xpath('.//th[11]/a').text

#     print(xuhao,hangye,zhishu,zs_zhangdie,liuru,liuchu,jine,gongsi,lingzhang,lz_zhangdie,lz_price)


def list_table_info(driver,w):
    tr_lst = driver.find_elements_by_xpath('//table[contains(@class,"J-ajax-table")]/tbody//tr')
    for tr in tr_lst:
        a = tr.find_element_by_xpath('.//td[1]').text
        b = tr.find_element_by_xpath('.//td[2]/a').text
        c = tr.find_element_by_xpath('.//td[3]').text
        d = tr.find_element_by_xpath('.//td[4]').text
        e = tr.find_element_by_xpath('.//td[5]').text
        f = tr.find_element_by_xpath('.//td[6]').text
        g = tr.find_element_by_xpath('.//td[7]').text
        h = tr.find_element_by_xpath('.//td[8]').text
        i = tr.find_element_by_xpath('.//td[9]/a').text
        j = tr.find_element_by_xpath('.//td[10]').text
        k = tr.find_element_by_xpath('.//td[11]').text
        lianjie = tr.find_element_by_xpath('.//td[2]/a').get_attribute('href')
        #print(a,b,c,d,e,f,g,h,i,j,k)
        w.writerow([a,b,c,d,e,f,g,h,i,j,k,lianjie])
        DETAIL_URLS.append([b, lianjie])


def get_next_page(driver):
    next_page = driver.find_elements_by_xpath('//a[text()="下一页"]')
    return next_page


if __name__ == "__main__":
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=opt)
    try:
        req_list(driver)
        print("num: ", len(DETAIL_URLS))
        with open("urls.csv", "w", encoding="utf-8", newline='') as f:
            w = csv.writer(f)
            for u in DETAIL_URLS:
                w.writerow(u)
                
    except Exception as e:
        print("err", e)
    finally:
        driver.close()

    