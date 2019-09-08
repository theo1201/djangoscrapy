# import requests
from urllib.parse import quote
from requests_html import HTMLSession
session = HTMLSession()
cookies = {
    'cid': '806090c27227e8811ea0a04772f2c8ac1565133752',
    'ComputerID': '806090c27227e8811ea0a04772f2c8ac1565133752',
    'guideState': '1',
    'PHPSESSID': '3d88cba27db2e7630daa09a92c63e6e5',
    'user': 'MDp0aGVvbGl1OjpOb25lOjUwMDo1MDUxNTI5NTE6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOzUsMSw0MDs4LDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxLDQwOjo6OjQ5NTE1Mjk1MToxNTY1ODc3NjkyOjo6MTU2NTg3NzY2MDo1NTAwNzA4OjA6MTc5MjU5Njk0Yzk1NmU4ZjkxODVjNjgxMDBkOTI1NTI2OmRlZmF1bHRfMjow',
    'userid': '495152951',
    'u_name': 'theoliu',
    'escapename': 'theoliu',
    'ticket': 'cb4eabb7d6e0eea46c79a11bd2d68069',
    'v': 'Am4iIj_5vzmJcstcyLnon5M2uc8zbzJpRDPmTZg32nEsewB5AP-CeRTDNl9r',
}

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'hexin-v': 'Am4iIj_5vzmJcstcyLnon5M2uc8zbzJpRDPmTZg32nEsewB5AP-CeRTDNl9r',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Proxy-Connection': 'keep-alive',
}
url1 = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=3&qs=pc_%7Esoniu%7Estock%7Estock%7Ehistory%7Equery&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w="
keywords = "2012年到2018年roe大于等于15%，2019年3月31日roe大于等于3.75%，上市时间大于5年，行业2018年营收增长率，2018年净利润增长率，2019年3月31日营收增长率，2019年3月31日净利润增长率"
url = url1 + quote(keywords, 'utf-8')

r = session.get(url,headers=headers, cookies=cookies)
html = r.html
header = html.find(".static_con table", first=True).html
dfhead = pd.read_html(str(header))[0][[2, 3]].rename(
    columns={2: "stock_code", 3: "stock_name"})
tablebody = html.find('.scroll_tbody_con table', first=True).html
