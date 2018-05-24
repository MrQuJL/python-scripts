from io import StringIO
from io import BytesIO

#f = StringIO()
#print(f.write('hello'))

#print(f.write(' '))

#print(f.write('world!'))

#print(f.getvalue())

#f = StringIO('Hello!\nHi\nGoodbye!')

#while True:
#	s = f.readline()
#	if s == '':
#		break
#	print(s.strip())

#f = BytesIO()
#l = f.write('中文'.encode('utf-8'))
#print(l)

#print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

print(f.read())

