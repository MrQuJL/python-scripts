import os

#print(os.name)

#print(os.uname())

#print(os.environ)

#print(os.environ.get('PATH'))

#print('当前路径:', os.path.abspath('.'))

#print(os.path.join(r'D:\file !important\study-python\10_IO编程', 'testdir'))

#os.mkdir('D:\\file !important\\study-python\\10_IO编程\\testdir')

#os.rmdir(r'D:\file !important\study-python\10_IO编程\testdir')

#s = os.path.split('D:\\file !important\\study-python\\10_IO编程\\testdir\\file.txt')

#print(s)

#m = os.path.splitext('D:\\file !important\\study-python\\10_IO编程\\testdir\\file.txt')

#print(m)

#os.rename('test.txt', 'test.py')

#os.remove('test.py')

#s = [x for x in os.listdir('.') if os.path.isdir(x)]

#print(s)

s = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

print(s)


