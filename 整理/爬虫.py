import requests

url = 'http://www.baidu.com'
html = requests.get(url)
print(html.text)
# 上面代码出现问题'gbk' codec can't encode character '\xe7'的解决办法
url = 'http://www.baidu.com'
html = requests.get(url)
print(html.text.encode('GBK', 'ignore').decode('GBk'))
