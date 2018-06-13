import requests
r = requests.get('https://www.douban.com/')
m = r.status_code
#print(m)
t = r.text
#print(t)


r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})

#print(r.url)

#print(r.encoding)

#print(r.content)







