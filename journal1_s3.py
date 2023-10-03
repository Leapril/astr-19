#Session 3 Prompt: 
#Write a Python program that defines a function f(x) that returns x**3 + 8. 
#In the main function of the program, call f(x) with x = 9 and print the result.  
#Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
def f(x):

	n = x**3+8
	if n > 27:
		print("YAY!")
	else:
		return n

def main():
	x = 9
	f(x) #will be greater therefore print YAY

	y = 1 #will be less so print out result
	print(f(y))


if __name__=="__main__":
	main()
