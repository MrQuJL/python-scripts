class Student(object):
	pass

s = Student()
s.name = 'qujianlei'

print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)

s.set_age(25)

print(s.age)

s2 = Student() # 创建新的实例
#s2.set_age(12)

def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score(100)
print('s.score:', s.score)

s2.set_score(99)
print('s2.score:', s2.score)

class Student(object):
	__slots__ = ('name', 'age')

s = Student()
s.name = 'MrQuJL'
s.age = 21
#s.score = 99

class GraduateStudent(Student):
	pass

g = GraduateStudent()
g.score = 999

class Test(object):
	__slots__ = ('name', 'age')

t = Test()

def test1(self):
	print('hello perms')

t.name = MethodType(test1, t)

t.name()




