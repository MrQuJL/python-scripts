age = 20
if age >= 18:
	print('your age is', age)
	print('adult')
	print('看看你能写多少行')
	print('en')

print('''--------- 我是分割线 ----------''')

age = 3
if age >= 18:
	print('adult')
	print('hello')
elif age >= 6:
	print('teenager')
else:
	print('kid')

# 不支持 else if 只支持elif

x = (1,2)
if x:
	print('这是一个', "True")

birth = input('please input birth:')
if int(birth) < 2000:
	print('00前')
else:
	print('00后')


bmi = 53.5 / (1.68 * 1.68)
if bmi > 32:
	print('严重肥胖')
elif bmi >= 28:
	print('肥胖')
elif bmi >= 25:
	print('过重')
elif bmi >= 18.5:
	print('正常')
else:
	print('过轻')

