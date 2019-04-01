from bs4 import BeautifulSoup
import re
import sys
import urllib.request
import urllib.parse

def getSearchURL_1(keyword):
    return str("http://www.csrc.gov.cn/wcm/govsearch/simp_gov_list.jsp?sword="+urllib.parse.quote(str(keyword+" 首次公开发行股票招股说明书"))+"&searchColumn=all&searchYear=all&pubwebsite=/zjhpublic/&SType=1&page=1")
def getSearchURL_2(keyword):
    return str("http://www.csrc.gov.cn/wcm/govsearch/simp_gov_list.jsp?sword="+urllib.parse.quote(str(keyword+" 创业板首发招股说明书"))+"&searchColumn=all&searchYear=all&pubwebsite=/zjhpublic/&SType=1&page=1")

print("请输入待查找的公司名称（尽可能完整），按回车键确认。\n输入“exit”以退出。")
keyword = str(input())
if keyword == 'exit':
    sys.exit()

donecnt = 0

_soup = BeautifulSoup(urllib.request.urlopen(getSearchURL_1(keyword)), "html.parser")
linklist = []
for x in _soup.find_all('a', href=re.compile('pub')):
    link = x.get('href')
    if link:
        linklist.append('http://www.csrc.gov.cn'+link[0:link.find('?')])
for _link in linklist:
    if donecnt == 0:
        original = urllib.request.urlopen(_link)
        soup = BeautifulSoup(original, "html.parser")
        for x in soup.find_all('a', string=re.compile('首次公开发行股票招股说明书')):
            dlink = x.get('href')
            string = x.get_text()
            downloadlink = str((_link[0:_link.rfind('/')])+dlink[1:])
            print("已经找到说明书，正在下载。")
            urllib.request.urlretrieve(downloadlink, string)
            print("下载完成。")
            donecnt = donecnt + 1

if donecnt == 0:
    _soup = BeautifulSoup(urllib.request.urlopen(getSearchURL_2(keyword)), "html.parser")
    linklist = []
    for x in _soup.find_all('a', href=re.compile('pub')):
        link = x.get('href')
        if link:
            linklist.append('http://www.csrc.gov.cn' + link[0:link.find('?')])
    for _link in linklist:
        if donecnt == 0:
            original = urllib.request.urlopen(_link)
            soup = BeautifulSoup(original, "html.parser")
            for x in soup.find_all('a', string=re.compile('创业板首发招股说明书')):
                dlink = x.get('href')
                string = x.get_text()
                downloadlink = str((_link[0:_link.rfind('/')]) + dlink[1:])
                print("已经找到说明书，正在下载。")
                urllib.request.urlretrieve(downloadlink, string)
                print("下载完成。")
                donecnt = donecnt + 1

if donecnt == 0:
    print("没有找到说明书。")