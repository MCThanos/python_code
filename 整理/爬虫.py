import requests

url = 'http://www.baidu.com'
html = requests.get(url)
print(html.text)
# ��������������'gbk' codec can't encode character '\xe7'�Ľ���취
url = 'http://www.baidu.com'
html = requests.get(url)
print(html.text.encode('GBK', 'ignore').decode('GBk'))
