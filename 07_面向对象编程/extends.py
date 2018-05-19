class Animal(object):
	def run(self):
		print('animal is running...')

class Dog(Animal):
	def run(self):
		print('dog is running..')

class Cat(Animal):
	def run(self):
		print('cat is running')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()


print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))

def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())

run_twice(Dog())

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

run_twice(Tortoise())

class Timer(object):
	def run(self):
		print('duck class...gaga...')


run_twice(Timer())

