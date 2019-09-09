# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy_splash import SplashRequest
# from urllib.parse import quote
# import pandas as pd

# class LixingerSpider(scrapy.Spider):
#     name = 'lixinger'
#     allowed_domains = ['lixinger.com']
#     start_urls = ['http://www.lixinger.com/']

#     def start_requests(self):
#         script = """
#                     function main(splash, args)
#                       splash:set_custom_headers({
#                         ["Cookie"] = "jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDVhYjZmZTYxNjBkMzU0YWUxNjNiZTYiLCJpYXQiOjE1NjYyMzA2NjksImV4cCI6MTU2NjgzNTQ2OX0.HkU4_nypFeYMEKuEjhsJ-fo0bYaNbHQ4YxH8rzfNGFs; Hm_lvt_ec0ee7e5c8bed46d4fdf3f338afc08f5=1566229950,1566230670; Hm_lpvt_ec0ee7e5c8bed46d4fdf3f338afc08f5=1566230670"
#                       })
#                       splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
#                       splash:go(args.url)
#                       splash:wait(10)
#                       return {html=splash:html()}
#                     end
#                 """
#         # stock_code = ["600167","600167","600167","600887"]
#         # url = "https://www.lixinger.com/analytics/company/sz/"+"600167"+"/detail/custom-fs"
        
#         url = "https://www.lixinger.com/analytics/company/sz/000848/detail/custom-fs?start-date=2014-08-19&end-date=2019-08-19&page-index=0&granularity=y&fs-display-type=number&fs-metrics-data-types=t,c,c2y,yoy,coc"
#         # keywords = "2012年到2018年roe大于等于15%，2019年3月31日roe大于等于3.75%，上市时间大于5年，行业2018年营收增长率，2018年净利润增长率，2019年3月31日营收增长率，2019年3月31日净利润增长率"
#         # url = url1 +quote(keywords,'utf-8')
#         yield SplashRequest(url,self.parse,endpoint="execute",args={'lua_source': script, 'url': url}
#         # cookies={"Hm_ck_1566229019904":"","Hm_lpvt_ec0ee7e5c8bed46d4fdf3f338afc08f5":"1566229953",
#         # "Hm_lvt_ec0ee7e5c8bed46d4fdf3f338afc08f5":"1566229950",
#         # "jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDVhYjZmZTYxNjBkMzU0YWUxNjNiZTYiLCJpYXQiOjE1NjYyMjk5NDksImV4cCI6MTU2NjgzNDc0OX0.swAT803DisSfHEFFfkW-gd-Rpu5SLDH75dmkTrTORzg"}
#         )
#     def cookie_to_dic(cookie):
#         return {item.split('=')[0]: item.split('=')[1] for item in cookie.split('; ')}
        
#     def parse(self, response):
#         filename = response.url.split("/")[-2] + '.html'
#         with open(filename,'wb') as f:
#             f.write(response.body)

#     {"_id": "5d5aba9d18cd7469a6e462f7", "areaCode": "cn", "fsTableType": "normal", "type": "s_fs_custom", "userId": "5d5ab6fe6160d354ae163be6", "metricsIds": [
#         "cn.normal.profitStatement.oi", "cn.normal.balanceSheet.ar", "cn.normal.balanceSheet.i", "cn.normal.balanceSheet.tca_tcl_r"], "updateDate": "2019-08-19T15:05:01.456Z"}
