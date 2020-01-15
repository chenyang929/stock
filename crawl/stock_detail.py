import time
import csv
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def req_detail(driver,u):
    rows = list()
    driver.get(u)
    time.sleep(3)
    rows.extend(detail_table_info(driver))
    next_page = get_next_page(driver)
    while len(next_page) > 0:
        next_page[0].click()
        time.sleep(3)
        rows.extend(detail_table_info(driver))
        next_page = get_next_page(driver)
    return rows


def detail_table_info(driver):
    page_rows = list()
    tr_lst = driver.find_elements_by_xpath('//div[@id="maincont"]/table/tbody//tr')
    for tr in tr_lst:
        xuhao = tr.find_element_by_xpath('.//td[1]').text
        if xuhao == "暂无成份股数据":
            break
        daima = tr.find_element_by_xpath('.//td[2]/a').text
        mingchen = tr.find_element_by_xpath('.//td[3]/a').text
        xianjia = tr.find_element_by_xpath('.//td[4]').text
        zhangdiefu = tr.find_element_by_xpath('.//td[5]').text
        zhangdie = tr.find_element_by_xpath('.//td[6]').text
        zhangsu = tr.find_element_by_xpath('.//td[7]').text
        huanshou = tr.find_element_by_xpath('.//td[8]').text
        liangbi = tr.find_element_by_xpath('.//td[9]').text
        zhengfu = tr.find_element_by_xpath('.//td[10]').text
        chengjiaoe = tr.find_element_by_xpath('.//td[11]').text
        liutonggu = tr.find_element_by_xpath('.//td[12]').text
        liutongshizhi = tr.find_element_by_xpath('.//td[13]').text
        shiyinlv = tr.find_element_by_xpath('.//td[14]').text

        lianjie = tr.find_element_by_xpath('.//td[3]/a').get_attribute('href')
        page_rows.append([xuhao,daima,mingchen,xianjia,zhangdiefu,zhangdie,zhangsu,huanshou,liangbi,zhengfu,chengjiaoe,liutonggu,liutongshizhi,shiyinlv,lianjie])
        print(xuhao,daima,mingchen,xianjia,zhangdiefu,zhangdie,zhangsu,huanshou,liangbi,zhengfu,chengjiaoe,liutonggu,liutongshizhi,shiyinlv)
    return page_rows


def get_next_page(driver):
    next_page = driver.find_elements_by_xpath('//a[text()="下一页"]')
    return next_page


if __name__ == "__main__":
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=opt)
    url_lst = list()
    with open("urls.csv", "r", encoding="utf-8") as f:
        r = csv.reader(f)
        for row in r:
            url_lst.append(row)
    try:
        for idx, item in enumerate(url_lst):
            if idx < 0:
                continue
            print(idx, item[0])
            rows = req_detail(driver, item[1])
            print("num:", len(rows))
            if len(rows) == 0:
                break
            d = str(datetime.now().date())
            with open("d:/stock/{}/{}_{}.csv".format(d, item[0], d), "w", encoding="utf-8", newline='') as f:
                w = csv.writer(f)
                w.writerow(["序号","代码","名称","现价","涨跌幅%","涨跌","涨速%","换手%","量比","振幅%","成交额","流通股","流通市值","市盈率","链接"])
                w.writerows(rows)
    except Exception as e:
        print("err", e)
    finally:
        driver.close()

    