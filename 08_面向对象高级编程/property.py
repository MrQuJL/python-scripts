
class Student(object):

	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

#s.set_score(9999)

print('-------装饰器@property--把一个方法变成一个属性----')

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

s = Student()
s.score = 60

print(s.score)

#s.score = 1000

print('---------只读属性：---------')

class Student(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	#只读属性
	@property
	def age(self):
		return 2018 - self._birth

s = Student()
s.birth = 1996

print(s.birth)
print(s.age)
#s.age = 10

class Screen(object):
	
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value
	
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

sc = Screen()
sc.width = 10
sc.height = 20
print('width:', sc.width)
print('height:', sc.height)
print(sc.resolution)

#sc.resolution = 10

