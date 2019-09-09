# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy_splash import SplashRequest
# from urllib.parse import quote
# import pandas as pd

# class TaobaoCommentSpider(scrapy.Spider):
#     name = 'iwencai'
#     allowed_domains = ['iwencai.com']
#     start_urls = ['http://www.iwencai.com/']

#     def start_requests(self):
#         script = """
#                     function main(splash, args)
#                       splash:set_user_agent("Mozilla/5.0  Chrome/69.0.3497.100 Safari/537.36")
#                       splash:go(args.url)
#                       splash:wait(10)
#                       return {html=splash:html()}
#                     end
#                 """
#         url1 = "http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=3&qs=pc_%7Esoniu%7Estock%7Estock%7Ehistory%7Equery&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w="
#         keywords = "2012年到2018年roe大于等于15%，2019年3月31日roe大于等于3.75%，上市时间大于5年，行业2018年营收增长率，2018年净利润增长率，2019年3月31日营收增长率，2019年3月31日净利润增长率"
#         url = url1 +quote(keywords,'utf-8')
#         yield SplashRequest(url,self.parse,endpoint="execute",args={'lua_source': script, 'url': url})
    
#     def parse(self, response):
#         filename = response.url.split("/")[-2] + '.html'
#         with open(filename,'wb') as f:
#             f.write(response.body)
#         # 获取股票信息
#         #  获取股票头信息
#         tablehead = response.css(".static_con table").extract_first()
#         # 获取第二列和第三列的信息2/股票代码，3、股票名称
#         # dfhead = pd.read_html(str(tablehead))[0][[2,3]].rename(columns={2:"股票代码",3:"股票名称"})
#         dfhead = pd.read_html(str(tablehead))[0][[2,3]].rename(columns={2:"stock_code",3:"stock_name"})
#         # 获取主体股票信息
#         tablebody =  response.css('.scroll_tbody_con table').extract_first()
#         # 0、现价，1、涨跌幅。11、所属行业、12、13营业收入，14、15净利润
#         # dfbody = pd.read_html(str(tablebody))[0][[0,1,11,12,13,14,15]].rename(columns={0:"现价",1:"涨跌幅",11:"所属行业",12:"当前季度营业收入",13:"上一季度营业收入",14:"当前季度净利润",15:"上一季度净利润"})
#         dfbody = pd.read_html(str(tablebody))[0][[0,1,11,12,13,14,15]].rename(columns={0:"current_price",1:"rate",11:"company_selector",12:"revenue",13:"last_revenue",14:"profi",15:"last_profi"})
#         # 合并结果
#         res = pd.merge(dfhead, dfbody, left_index=True, right_index=True, how='outer')
#         # 筛选行业数据
#         shift_list = ["房地产开发","化学制品","建筑装饰","汽车零部件","汽车整车","保险及其他"]
#         res['state'] = res['company_selector'].str.split('-').apply(lambda x:x[1] if x[1] else '').isin(shift_list)
#         res = res.loc[res['state']==False]
#         # 判断是否大于0
#         res['state'] = True
#         res[res[['revenue','last_revenue','profi','last_profi']]<0]['state'] = False
#         res = res.loc[res['state']==True]
        
#         # yield {
#             # 'price': price,
#             # 'title':title
#         # }