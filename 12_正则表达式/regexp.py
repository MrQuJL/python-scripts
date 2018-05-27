import re

#s = r'ABC\-001'

#f = re.match(r'\d{3}-\d{3,8}$', '010-12345')

#f2 = re.match(r'\d{3}-\d{3,8}$', '010 12345')

#print(f)

#print('f2:', f2)

#test = '用户输入的字符串'

#if re.match(r'\w{7}$', test):
#	print('ok')
#else:
#	print('failed')

#m = 'a b c  d'.split(' ')
#print(m)

#m = re.split(r'[\s\,\;]+', 'a, b,; ;,  c')

#print(m)

m = re.match(r'^(\d{3})-(\d{3,8})', '010-12345')

#print(m)

#print(m.group(0))
#print(m.group(1))
#print(m.group(2))

f = re.match(r'^(\d+)(0*)$', '102300').groups()

f = re.match(r'^(\d+?)(0*)$', '102300').groups()

#print(f)


re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

f = re_telephone.match('010-12345').groups()

f = re_telephone.match('010-8086').groups()

#print(f)

def is_valid_email(addr):
	e = re.compile(r'([\w]+\.?[\w]+)@([\w]+\.?[\w]+)')
	if e.match(addr) != None:
		return True
	else:
		return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

