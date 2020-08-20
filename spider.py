# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    base_url = "https://movie.douban.com/top250?start="
    # 1-Scrap website
    datalist = get_data(base_url)
    # 2-Analyze data
    # 3-Save Data
    # savepath = '.\\doubanTop250.xls'
    # save_data(savepath)
    get_url(base_url)


get_movie_href = re.compile(r'<a class="" href="(.*?)">')
get_movie_img = re.compile(r'<img .* src="(.*?)" .*>', re.S)
get_movie_name = re.compile(r'<span class="title">(.*)</span>')
get_movie_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
get_movie_rating_people = re.compile(r'<span>(\d*)人评价</span>')
get_movie_intro = re.compile(r'<span class="inq">(.*)</span>')
get_movie_info = re.compile(r'<p class="">(.*?)</p>',re.S)


def get_data(base_url):
    datalist = []
    for i in range(0, 10):
        url = base_url + str(i * 25)
        web_content = get_url(url)

        soup = BeautifulSoup(web_content, "html.parser")
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)

            # Get all related info for each movie
            movie_link = re.findall(get_movie_href, item)[0]
            movie_img = re.findall(get_movie_img, item)[0]
            movie_name = re.findall(get_movie_name, item)
            movie_rating = re.findall(get_movie_rating, item)[0]
            movie_rating_people = re.findall(get_movie_rating_people, item)[0]
            movie_intro = re.findall(get_movie_intro, item)
            movie_info = re.findall(get_movie_info, item)[0]

            # Format movie info as needed
            # Append empty string if movie doesn't have title in other language
            if len(movie_name) == 2:
                chinese_title = movie_name[0]
                other_title = movie_name[1].replace("/", "")
            else:
                chinese_title = movie_name[0]
                other_title = ''

            # Remove dot
            if len(movie_intro) != 0:
                movie_intro = movie_intro[0].replace("。", "")
            else:
                movie_intro = ""

            # Remove <br/>
            movie_info = re.sub('<br(\s+)?/>(\s+)?', " ", movie_info).strip()

            # Save info to data
            data.extend((movie_link, movie_img, chinese_title, other_title, movie_rating, movie_rating_people,
                         movie_intro, movie_info))

            datalist.append(data)
    print(datalist)
    return datalist


# Get website content from url
def get_url(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.135 Safari/537.36"
    }

    req = urllib.request.Request(url, headers=head)
    html = ""
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')

    except urllib.error.URLError as err:
        if hasattr(err, "code"):
            print(err.code)
        if hasattr(err, "reason"):
            print(err.reason)

    return html


def save_data(savepath):
    return "111"


if __name__ == "__main__":
    main()
