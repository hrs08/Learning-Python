#polymorphism
#"duck typing"
# if it looks like a duck , quack like a duck -> must be a duck

class Animal:
	alive = True

class Dog(Animal):
	def speak(self):
		print("Woof!")

class cat(Animal):
	def speak(self):
		print("Meow!")

animals = [Dog() , cat()]

for ani in animals:
	ani.speak()

#instance v/s static method
class Emp:
	def __init__(self , name ,position):
		self.name = name
		self.position = position

	#instance method
	def get_info(self):
		return f"{self.name} = {self.position}"

	@staticmethod
	def is_valid_position(position):
		valid = ["Manager" , "cook" , "cashier"]
		return position in valid
print(Emp.is_valid_position("Dishwasher"))

#class method (cls) instead of (self)
#too much class in this repo btw
#but it was only thing left for me ;)

#so a new class lol

class Student:
	count = 0

	def __init__(self , name , gpa):
		self.name = name
		self.gpa = gpa
		Student.count += 1

	#instance method
	def get_info(self):
		return f"{self.name} -> {self.gpa}"

	@classmethod
	def get_count(cls):
		return f"Total # of stud : {cls.count}"

#magic / dunder method !!

class Book:
	def __init__(self, title, author, num_pages):
		self.title = title
		self.author = author
		self.num_pages = num_pages

	#this customise print() behaviour .. hmm
	def __str__(self):
		return f"{self.title} by {self.author}"

	#this is for equality
	def __eq__(self, other):
		return self.title == other.title and self.author == other.autho

	#for less than
	def __lt__(self, other):
		return self.num_pages < other.num_pages
	#for greater than
	def __lt__(self, other):
		return self.num_pages > other.num_pages

	#for adding
	def __add__(self, other):
		return f"{self.num_pages + other.num_pages} pages"

	#for iteration type shi
	def __contains__(self, keyword):
		return keyword in self.title or keyword in self.author

	#using key
	def __getitem__(self, key):
		if key == "title":
			return self.title
		elif key == "author":
			return self.author
		elif key == "num_pages":
			return self.num_pages
		else:
			return f"key '{key}' was not found"

