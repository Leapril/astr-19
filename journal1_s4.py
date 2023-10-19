#Session 4 Prompt: 
#Write a Python program that declares a class describing your favorite animal.
#Have the data members of the class represent the following physical parameters of the animal: 
#length of the arms (float), 
#length of the legs (float), 
#number of eyes (int), 
#does it have a tail? (bool), 
#is it furry? (bool). 
#Write an initialization function that sets the values of the data members when an instance of the class is created. 
#Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.

#declare a class called favorite animal
class Animal:
	def __init__(self, name, arm_length, leg_length, number_of_eyes, tail, fur): #list of features
		#initialization function sets the values of the data memebers when the instance of the class is called/created
		self.n= name
		self.al = arm_length
		self.ll = leg_length
		self.ne = number_of_eyes
		self.t = tail
		self.f = fur

	#member function of the class prints out ans describes the physical characteristics of the animal 
	def printAnimal(self):
		print("My favorite animal is a " + self.n, ". It's arm length is ", self.al, " inches. It's leg length is ", self.ll, " inches. ")
		print("It has ", self.ne, " eyes. ", end="")
		#tetsing the boolen values 
		if  self.t == True:
			print("It also has a tail. ", end="")
		else: 
			print("It doesn't have a tail.", end="")
		if  self.f == True:
			print("It also has fur!")
		else: 
			print("It does not have fur.")

def main():

	#test class
	a = Animal("Dog", 5.0, 6.0, 2, True, False)
	a.printAnimal()


#failsafe execution 
if __name__=="__main__":
	main()