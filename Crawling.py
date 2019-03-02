import requests
from bs4 import BeautifulSoup
import xlwt
import xlrd
from xlutils.copy import copy

headers = {"user-agent": "Mizilla/5.0"}

class_0_title = []
class_0_val = []
url_0 = "https://www.wdzj.com/dangan/"
res_0 = requests.get(url_0, headers=headers)
res_0.encoding = "utf-8"
class_0 = BeautifulSoup(res_0.text, "html.parser").select("[data-tar='businessTypeOr'] .searchFontN a[class!='unlimitedN on']")
for zz in range(0, len(class_0)):
    class_0_title.append(class_0[zz].text)
    class_0_val.append(class_0[zz].attrs["data-val"])
print(class_0_title)
print(class_0_val)
data = xlrd.open_workbook("data1.xls")
data_new = copy(data)
ws = data_new.get_sheet(0)
_a = 0
for i in class_0_title:
    ws.write(0, _a, i)
    _a += 4



for cwx in range(0, len(class_0_val)):
    final1 = []
    final2 = []
    final3 = []
    for i in range(1, 20):  # 根据因子迭代
        url = '%s%s%s%s' % ("https://www.wdzj.com/dangan/search?filter=e1-", class_0_val[cwx], "&show=1&currentPage=", i)
        res = requests.get(url, headers=headers)
        res.encoding = "utf-8"
        soup1 = BeautifulSoup(res.text, "html.parser").select("h2 a")
        soup2 = BeautifulSoup(res.text, "html.parser").select("label em")
        soup3 = BeautifulSoup(res.text, "html.parser").select(".itemConLeft .itemConBox:nth-child(3)")

        for m in range(0, len(soup1) - 2):
            final1.append(soup1[m].text)
        for n in range(0, len(soup2)):
            final2.append(soup2[n].text)
        for p in range(0, len(soup3)):
            final3.append(soup3[p].text.strip("注册地："))

    index1 = 1
    index2 = 1
    index3 = 1
    for i in final1:
        ws.write(index1, 4*cwx, i)
        index1 += 1
    for j in final2:
        ws.write(index2, 4*cwx+1, j)
        index2 += 1
    for k in final3:
        ws.write(index3, 4*cwx+2, k)
        index3 += 1




data_new.save("data1.xls")

