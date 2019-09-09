# # import requests

# from requests_html import HTMLSession
# session = HTMLSession()
# url  = 'https://www.lixinger.com/api/user/users/current'
# cookies = {
#     'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDVhYjZmZTYxNjBkMzU0YWUxNjNiZTYiLCJpYXQiOjE1NjYyMzA2NjksImV4cCI6MTU2NjgzNTQ2OX0.HkU4_nypFeYMEKuEjhsJ-fo0bYaNbHQ4YxH8rzfNGFs',
#     'Hm_lvt_ec0ee7e5c8bed46d4fdf3f338afc08f5': '1566229950,1566230670,1566254685',
#     'Hm_lpvt_ec0ee7e5c8bed46d4fdf3f338afc08f5': '1566254766',
# }

# headers = {
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#     'Accept': 'application/json, text/plain, */*',
#     'Referer': 'https://www.lixinger.com/analytics/company/sh/600167/detail',
#     'Connection': 'keep-alive',
# }

# # r = session.post(url, data={'username': 'yitian', 'passwd': 123456})

# response = session.get('https://www.lixinger.com/api/user/users/current', headers=headers, cookies=cookies)

# filename = response.html.base_url.split("/")[-2] + '.html'
# with open(filename,'wb') as f:
#     f.write(response.html.raw_html)



# import requests

# cookies = {
#     'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDVhYjZmZTYxNjBkMzU0YWUxNjNiZTYiLCJpYXQiOjE1NjYyMzA2NjksImV4cCI6MTU2NjgzNTQ2OX0.HkU4_nypFeYMEKuEjhsJ-fo0bYaNbHQ4YxH8rzfNGFs',
#     'Hm_lvt_ec0ee7e5c8bed46d4fdf3f338afc08f5': '1566229950,1566230670,1566254685',
#     'Hm_lpvt_ec0ee7e5c8bed46d4fdf3f338afc08f5': '1566254799',
# }

# headers = {
#     'Origin': 'https://www.lixinger.com',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#     'Content-Type': 'application/json;charset=UTF-8',
#     'Accept': 'application/json, text/plain, */*',
#     'Referer': 'https://www.lixinger.com/analytics/company/sh/600167/detail/custom-fs',
#     'Connection': 'keep-alive',
# }

# data = '{"stockIds":[600167],"startDate":"2014-08-19T22:46:54.545Z","endDate":"2019-03-30T16:00:00.000Z","granularities":["y"],"metricNames":["profitStatement.oi","balanceSheet.ar","balanceSheet.i","balanceSheet.tca_tcl_r","reportLink"],"expressionCaculateTypes":["t","c","c_2y","t_y2y","c_y2y","t_c2c","c_c2c"]}'

# response = requests.post('https://www.lixinger.com/api/analyt/company/fs-metrics/list-info', headers=headers, cookies=cookies, data=data)



