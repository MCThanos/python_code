import requests
import re
import csv
import time


def douban(a):
    rl = "https://movie.douban.com/top250?start="
    url = rl + str(a)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }
    req = requests.get(url, headers=headers)
    html = req.text

    move = re.compile(
        r' <div class="item">.*?<em class="">(?P<number>.*?)</em>.*?<span class="title">(?P<name>.*?)</span>.*?<span class="rating_num" property="v:average">(?P<num>.*?)</span>',
        re.S)
    result = move.finditer(html)
    print(result)
    f = open("豆瓣.csv", "a",encoding="GBK")
    for i in result:
        dic = i.groupdict()
        writer = csv.writer(f)
        writer.writerows([dic.values()])
    f.close()
    time.sleep(1)


for i in range(0, 1):
    a = i * 25
    douban(a)
