#if statements
age = 23

if(age>=80):
	print("Verified gramps")
elif (age<0):
	print("not possible dude")
elif (age>18 and age<80):
	print("Verified adult")
else:
	print("Lol minor ?")

for_sale = True
if for_sale:
	print("Welcome to the sale")
	print("would u like to sell your life ?")

#so.. using this u can make a good enough calculator , weight convertor
#temp convertor or anything u want
#it's upto u what to do , imma skip rn
#this python repo will not be as good as the C repo :(

#logical operator , or; and; not;
#dang.. i'm used to c syntac right now

temp = 25
rain = False
sun = True

if temp >= 30 and sun:
	print("it is hot outside")
elif temp > 35 or temp < 0 or rain:
	print("The outdoor event is cancelled..")
else:
	print("Go outside and have fun")

print(not(sun)) #invert the boolean

#conditional operation , also called ternary operator
#liked this in c , let's see here

num = 5
print("positive" if num > 0 else "negative")
result = "even" if num % 2 == 0 else "odd"
print(result)

#a if a>b else b --> for max min stuff

##	Working on string..
name = "yoo junghook"
print(len(name))
x = name.find(" ")
print(x)

x = name.rfind("o")
print(x)

name = name.capitalize()
print(name)

name = name.upper()
print(name)

print(name.lower())
print(name.isdigit())
print(name.isalpha()) #as it contain <space> , result would be false
print(name.count("O"))  #checking for "O" as did name.upper before :(
name = name.replace(" " , "䡖")
print(name)

#print(help(srt))
# this shows all stuff u can do
# with the use of string

# indexing[start : end : step]

print(f"your name was {name}")
print(name[:5:2])
#just revised this , good eno imo

