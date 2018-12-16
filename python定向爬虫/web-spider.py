#-*-coding:utf8-*-

# 使用requests获取网页源代码，再使用正则表达式匹配出感兴趣的内容
# 这是单线程简单爬虫的基本原理
# 需求：爬取极客学院大数据课程的相关图片保存在当前目录的pic文件夹下
import re
import requests
# 手动设置headers预防反爬虫机制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}

# 爬12页
img_no = 1
for page in range(12):
    url = "https://www.jikexueyuan.com/course/clouddata/?pageNum=%d"%(page + 1)
    html = requests.get(url)
    html = html.content.decode('utf8')

    img_box = re.findall('<div class="lessonimg-box">(.*?)</div>', html, re.S)
    # 获取所有课程图片的url
    print('now download url:' + url)
    for item in img_box:
        img_url = re.search('<img src="(.*?)" class="lessonimg"', item, re.S).group(1)
        img = requests.get(img_url)
        file_name = 'pic/' + str(img_no)
        fp = open(file_name + '.jpg', 'wb')
        print('download ' + file_name + 'of page ' + str(page + 1) + ', url:' + img_url)
        fp.write(img.content)
        fp.close()
        img_no += 1



