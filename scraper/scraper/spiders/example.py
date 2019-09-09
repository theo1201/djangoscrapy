# # import requests
# from requests_html import HTMLSession
# session = HTMLSession()

# stockid = 600887
# cookies = {
#     'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDVhYjZmZTYxNjBkMzU0YWUxNjNiZTYiLCJpYXQiOjE1NjYyMzA2NjksImV4cCI6MTU2NjgzNTQ2OX0.HkU4_nypFeYMEKuEjhsJ-fo0bYaNbHQ4YxH8rzfNGFs',
#     'Hm_lvt_ec0ee7e5c8bed46d4fdf3f338afc08f5': '1566229950,1566230670,1566254685,1566614875',
#     'Hm_lpvt_ec0ee7e5c8bed46d4fdf3f338afc08f5': '1566615253',
# }

# headers = {
#     'Origin': 'https://www.lixinger.com',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#     'Content-Type': 'application/json;charset=UTF-8',
#     'Accept': 'application/json, text/plain, */*',
#     'Referer': 'https://www.lixinger.com/analytics/company/sh/600887/detail/custom-fs',
#     'Connection': 'keep-alive',
# }

# data = '{"stockIds":[600887],"startDate":"2014-08-24T02:57:08.293Z","endDate":"2019-03-30T16:00:00.000Z","granularities":["y"],"metricNames":["profitStatement.oi","balanceSheet.ar","balanceSheet.i","balanceSheet.tca_tcl_r","reportLink"],"expressionCaculateTypes":["t","c","c_2y","t_y2y","c_y2y","t_c2c","c_c2c"]}'

# r = session.post('https://www.lixinger.com/api/analyt/company/fs-metrics/list-info',
#                          headers=headers, cookies=cookies, data=data)

# data = json.loads(r.html.text)
# y_list = []
# for value in data["fsMetricsList"]:
#     for v in value.get('y', {}).values():
#          for k, v in v.items():
#             value.update({k: v['t']})
#     for k in ['y', 'reportLink']:
#         if value[k]:
#             value.pop(k)
#     y_list.append(value)
# df = pd.DataFrame(y_list)
# # 判断状态
# df['state1'] = (df['oi']-df['ar']).apply(lambda x: x > 0)
# df['state2'] = (df['oi']-df['i']).apply(lambda x: x > 0)
# df['state3'] = df['tca_tcl_r'].apply(lambda x: x > 1)
# # 小熊定理判断,stockidlist是不合格股票
# stockidlist = []
# for index, row in df.iterrows():
#     if not row['state1'] and (index != len(df)-1) and not df.loc[index+1, 'state1']:
#         stockidlist.append(row['stockId'])
#         break
#     if not row['state2'] and (index != len(df)-1) and not df.loc[index+1, 'state2']:
#         stockidlist.append(row['stockId'])
#         break
#     if not row['state3']:
#         stockidlist.append(row['stockId'])
#         break
# print(stockidlist)
