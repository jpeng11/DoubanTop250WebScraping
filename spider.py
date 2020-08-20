# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    baseURL = "https://movie.douban.com/top250?start="
    #baseURL = 'https://www.hommi.jp/cn/product/64284'
    # 1-Scrap website
    datalist = getData(baseURL)
    # 2-Analyze data
    # 3-Save Data
    # savepath = '.\\doubanTop250.xls'
    # saveData(savepath)
    getURL(baseURL)


def getData(baseURL):
    datalist = []
    for i in range(0, 10):
        url = baseURL + str(i * 25)
        html = getURL(url)
    return datalist


# Get website content from url
def getURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.135 Safari/537.36"
    }

    req = urllib.request.Request(url, headers=head)
    html = ""
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as err:
        if hasattr(err, "code"):
            print(err.code)
        if hasattr(err, "reason"):
            print(err.reason)

    return html


def saveData(savepath):
    return "111"


if __name__ == "__main__":
    main()
