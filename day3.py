#format specifiers
#this one is interesting

p1 = -3892794889.14159
p2 = 7319

print(f"price 1 is {p1:.2f}")
print(f"price 1 is {p1:10}")
print(f"price 1 is {p1:010}")
print(f"price 1 is {p1:<10}")
print(f"price 1 is {p1:>10}")
print(f"price 1 is {p1:^10}")
print(f"price 2 is {p2:+}")
print(f"price 2 is {p2: }")
print(f"price 1 is {p1:,}")
print(f"price 1 is {p1:+,.2f}")

#while loop
#for loop
#continue break
#kinda weird timer
#nested loop
#list tuple set
#shopping card program
#2d list
#a quiz game... yeah
#dictionary
#working with dict
#random func
#rock paper scissor
#dice rolling stuff?
#def functions

#!! , list comprehension
#expression for value in interable if condition

double = [x * 2 for x in range(1,11)]
print(double)

num = [1,2,-3,-4,5,-6]
pnum = [i for i in num if i >=0]
print(pnum)


#match case statement [works as switch]
def day_ofweek(day):
	match day:
		case 1:
			print("Monday")
		case 2:
			print("Tuesday")
		case 3:
			print("Wednesday")
		case 4:
			print("Thursday")	
		case 5:
			print("Friday")				
		case 6:
			print("Saturday")						
		case 7:
			print("Sunday")
		case _:
			print(f"{day} is not valid")
			
			  

#so now what even is __name__ = __main__
#ok understood it

#banking program
#slot machine type

#day4  encryption stuff , basic string module
#hangman game

#finally made it to oop , onto the day5
