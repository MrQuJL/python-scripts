d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : True}

print(d)

print(d['Tracy'])

d['Hello'] = 88
d['Hello'] = 99

print(d)

if 'dfd' in d:
	print(d['dfd'])
else:
	print('不存在该key')

print(d.get('Tracy1'))

d.pop('Tracy')

print(d)











