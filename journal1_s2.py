#Session 2 Prompt: 
#Write a Python that prints the sum of two floating point numbers
#the difference between two integers
#and the product of a floating point number and an integer. 
#In each case, have the program print out the data type of the resulting answer.

#functions:add,subctract,and multiply which will take the values from main, 
#then print the results
def add(a,b):
	s = a+b 
	print("Addition result: ", s)

def subtract(a,b):
	s = a-b
	print("Subtraction result: ", s)

def multiply(a,b):
	s = a*b
	print("Multiplication result: ", s)

def main():
	a = 1.37 #float
	b = 4.63 #float
	c = 6 	 #int

	#callign functions with values
	add(a,b) 
	subtract(a,b)
	multiply(a,c)

if __name__=="__main__":
	main()

