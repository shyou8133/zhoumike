from flask import Flask
import requests
import json
url = r"http://www.eastmoney.com"
name_node = "601117"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
url_zjlx = r"http://data.eastmoney.com/zjlx/{}.html".format(name_node)

r=requests.get(url_zjlx,headers=headers)
res=r.text
print(url_zjlx)
