#property decorator :

class Rectangle:
	def __init__(self, width, height):
		self._width = width
		self._height = height

	@property
	def width(self):
		return f"{self._width:.1f}cm"

	@property
	def height(self):
		return f"{self._height:.1f}cm"

	@width.setter
	def width(self, new_w):
		if new_w > 0:
			self._width = new_w
		else:
			print("Width must be > than 0")

	@height.setter
	def height(self, new_h):
		if new_h > 0:
			self._height = new_h
		else:
			print("Height must be > than 0")

	@width.deleter
	def width(self):
		del self._width
		print("Width has been deleted")

	@height.deleter
	def height(self):
		del self._height
		print("Height has been deleted")
	
rectangle = Rectangle(3 ,4)

del rectangle.width
del rectangle.height

print(f"{rectangle.width} = width , {rectangle.height} = height")


# well to answer the ques
# what is a decorator L
# func that extend behavior of other func w/o modify base fun

#basic formula 
def add_sprinkles(func):
	def wrapper(*args , **kwargs):
		print("** You added sprinkles ꈴ **")
		func(*args , **kwargs)
	return wrapper   

@add_sprinkles
def get_icream():
	print("Here is your ice cream 🍦")
	
get_icream()

#exception handling , now !!
#file handling

#so except oops i had most of stuff done
#now i just need to revise and create good projects
#so that i can remember it

#ok so now moving on to a project
#tui based music player some shi

#datetime module
#its good shi , can use thi

