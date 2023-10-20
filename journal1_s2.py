#Session 2 Prompt: 
#Write a Python that prints the sum of two floating point numbers
#the difference between two integers
#and the product of a floating point number and an integer. 
#In each case, have the program print out the data type of the resulting answer.

#functions:add,subctract,and multiply which will take the values from main, 
#then print the results
def add(a,b): #addition
	s = a+b 
	print("Addition result: ", s) #prints results

def subtract(a,b): #subtraction
	s = a-b
	print("Subtraction result: ", s)

def multiply(a,b): #multiplication
	s = a*b
	print("Multiplication result: ", s)

def main():
	#create values a,d,c
	a = 1.37 #float
	b = 4.63 #float
	c = 6 	 #int

	#calling functions with values
	add(a,b) 
	subtract(a,b)
	multiply(a,c)

#failsafe executable
if __name__=="__main__":
	main()

