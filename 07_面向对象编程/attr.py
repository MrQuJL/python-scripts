class Student(object):
	def __init__(self, name):
		self.name = name

s = Student('Bob')
s.score = 90

print(s.score)

class Student(object):
	name = 'Student'

s = Student()

print(s.name)

print(Student.name)

print('--------修改Michae后--------')

s.name = 'Michael'
print(s.name)
print(Student.name)

del s.name
print('删除实例的name属性后', s.name)

class Student(object):
	count = 0

	def __init__(self, name):
		Student.count = Student.count + 1
		self.name = name

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')




