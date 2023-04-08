# coding=gbk

'''
思路
请求url,拿到第一个m3u8
请求第一个m3u8,拿到第二个m3u8
下载视频
'''
import asyncio
import requests
import re
import anyio
import aiohttp
import aiofiles
import time
from Crypto.Cipher import AES
import os


def first_url(url, headers):
    url = 'https://www.88ysw.org/play/?454-2-0.html'
    rep = requests.get(url, headers=headers)
    a = re.compile(
        r'<script>var vid="454";var vfrom="2";var vpart="0";var now="(?P<first_m3u8_url>.*?)";var pn="wjm3u8"; var next="',
        re.S)
    b = a.finditer(rep.text)
    for i in b:
        return i.group('first_m3u8_url')


def second_url(url, headers):
    rep = requests.get(url, headers=headers)
    return "https://v4.cdtlas.com/" + rep.text.split('\n')[2]


def download_m3u8(url, headers):
    rep = requests.get(url, headers=headers)
    with open('a.text', 'w', encoding='utf-8') as f:
        f.write(rep.text)


async def download_ts(url, i, session, headers):
    async with session.get(url, headers=headers) as resp:
        async with aiofiles.open(f"爬虫/{i}", "wb") as f:
            await f.write(await resp.content.read())
            jiemi(i)
    print('over')


async def download_mp4():
    tasks = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"}
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('a.text', 'r', encoding='utf-8') as f:
            i = 0
            async for line in f:
                if line.startswith("#"):
                    continue
                url = line.strip()
                i = i + 1
                task = asyncio.create_task(download_ts(url, i, session, headers))
                tasks.append(task)
            await asyncio.wait(tasks)



def jiemi(i):
    keys='177e5e4aafdadd9d'
    key1 = str.encode(keys)
    aes=AES.new(key=key1,IV=b'0000000000000000',mode=AES.MODE_CBC)
    with open(f'爬虫/{i}','rb') as f1 , open(f'爬虫/{i}.mp4','wb') as f2:
        bs=f1.read()
        f2.write(aes.decrypt(bs))

if __name__ == '__main__':
    for number in range(0, 1):
        url = f'https://www.88ysw.org/play/?454-2-{number}.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"}
        first_m3u8_url = first_url(url, headers)
        second_m3u8_url = second_url(first_m3u8_url, headers)
        download_m3u8(second_m3u8_url, headers)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download_mp4())


