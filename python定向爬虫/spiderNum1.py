# -*- coding: utf-8 -*-
import re
import requests

# 需求:爬取极客学院官网上前20页的课程信息
# 包括课程标题，课程介绍，课时，，等级，多少人学习

# 1.获取极客学院的官方网站网址

# 2.爬取网页数据

# 3.利用正则筛选出我们想要的课程相关信息

# 4.把想要的数据封装成到Course对象中存入list保存

# 5.将list中的数据写入文本文件


class Course(object):

    def __init__(self, title, desc, time, grade, count):
        self.title = title
        self.desc = desc
        self.time = time
        self.grade = grade
        self.count = count

    def to_string(self):
        return '课程标题: ' + self.title + '\n' + '课程描述: ' + self.desc + '\n' + '课时: ' + self.time + '\n' + '课程等级: ' + self.grade + '\n' + '学习人数: ' + self.count + "\n"


class JKSpider(object):

    def __init__(self, html_url, total_page):
        self.html_url = html_url
        self.total_page = total_page
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }
        self.courses = []

    def get_lesson(self):

        for page in range(self.total_page):
            page += 1
            url = re.sub('\d+', str(page), html_url)
            html = requests.get(url, headers = self.headers)
            html = html.content.decode('utf-8')
            ul_content = re.search('<ul class="cf" style="display: block;">(.*?)</ul>', html, re.S).group(1)
            lis = re.findall('<li id="\d+" test="\d+" deg="\d+" >(.*?)</li>', ul_content, re.S)
            for li in lis:
                lesson_info = re.search('<div class="lesson-infor" style="height: 88px;">(.*?)</div>', li, re.S).group(1)
                lesson_info_h2 = re.search('<h2 class="lesson-info-h2">(.*?)</h2>', lesson_info, re.S).group(1)
                # 1.课程标题
                lesson_title = re.search('>(.*?)</a>', lesson_info_h2, re.S).group(1)
                # 2.课程介绍
                lesson_desc = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>', lesson_info, re.S).group(1)
                lesson_desc = lesson_desc.strip()
                # 3.课时
                time_grade = re.findall('<em>(.*?)</em>', lesson_info, re.S)
                time = time_grade[0]
                time = time.replace('\n', '')
                time = time.replace('\t', '')
                # 4.课程等级
                grade = time_grade[1]
                # 5.学习人数
                learn_number = re.search('<em class="learn-number">(.*?)</em>', lesson_info, re.S).group(1)

                # 组装对象
                course = Course(lesson_title, lesson_desc, time, grade, learn_number)
                self.courses.append(course)


html_url = 'https://www.jikexueyuan.com/course/?pageNum=1'
total_page = 10
spider = JKSpider(html_url, total_page)
spider.get_lesson()

file_name = 'D:/python_workspace/test/course/course.txt'
for course in spider.courses:
    print(course.to_string())
    fp = open(file_name, 'a+', encoding='utf8')
    fp.write(course.to_string() + '\n')
    fp.close()


