# 复制图片

origin = r'D:\picture\1.jpg'

dest = r'D:\picture\copy.jpg'

try:
	s = open(origin, 'rb')
	d = open(dest, 'wb')
	for line in s.readlines():
		d.write(line)

finally:
	s.close()
	d.close()

