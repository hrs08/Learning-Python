#object oriented programming
#classes and stuff

class Car:
	wheel = 4 #class variable
	def __init__(self, model, year, color, for_sale):
		self.model = model
		self.year = year
		self.color = color
		self.for_sale = for_sale

	def drive(self):
		print(f"You drive the {self.model}")
	def stop(self):
		print(f"You stop the {self.model}")

	
c1 = Car("Mustang" , 1863 , "red" , False)

c1.drive()
print(Car.wheel)  #using class name instead of c1 = better read + it is class var

#to save line of code , and maybe better reading
#save the class block into a different file and import it 	
#this is the main stuff behind oop


#inheritance in classes
#using animal as example

class Animal:
	def __init__(self , name):
		self.name = name
		self.is_alive = True

	def eat(self):
		print(f"{self.name} is eating")
	def sleep(self):
		print(f"{self.name} is sleeping")

class Dog(Animal):
	def speak(self):
		print("Woof!")

class Cat(Animal):
	def speak(self):
		print("meow!")

dog = Dog("bark")
cat = Cat("meow")
 
cat.eat()
dog.sleep()
cat.speak()
dog.speak()

#so now multiple inheritance
#and multilevel inheritance

class prey(Animal):
	def flee(self):
		print("The animal is fleeing")

class predator(Animal):
	def hunt(self):
		print("The animal is hunting")

class rabbit(prey):
	pass

class hawk(predator):
	pass

class fish(prey , predator):
	pass

rab = rabbit("rab")
hak = hawk("huh")
nemo = fish("neom")

rab.flee()
hak.hunt()

nemo.flee()
nemo.hunt()


#using super(	) , used to call method from parent class ? weird idk

class Shape:
	def __init__(self , color , filled ):
		self.color = color
		self.filled = filled

class Circle(Shape):
	def __init__(self , color , filled , radius):
		super.__init__(color , filled)
		self.radius = radius

class Square(Shape):
	def __init__(self , color , filled , side):
		super.__init__(color , filled)
		self.side = side

class Trianlge(Shape):
	def __init__(self , color , filled , width , height):
		super.__init__(color , filled)
		self.width = width
		self.height = height 

#polymorphism
#many forms : a greek word

#so its like inheritance give polymorphism
#also duck typing ??

#so like if it look duck , quack like duck -> must be a duck



