import re,time
import requests
from bs4 import BeautifulSoup

url = r"http://www.eastmoney.com"
name_node = "601117"
url_zjlx = "http://data.eastmoney.com/zjlx/{}.html".format(name_node)

# contentBox
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'},
r = requests.get(url_zjlx)
time.sleep(1)
soup = BeautifulSoup(r.text, "lxml")
rep = re.compile(r'<div class="tit">(.*?)</div>')
gpname1 = soup.find_all(".tit")

list=[]
for k in gpname1:
    i=0
    print(k)
    list.append(k.string)
    #print(k.text)
    i += 1


# gpname2=soup.find_all("div",class_:"contentBox tit")    #获取股票名字
