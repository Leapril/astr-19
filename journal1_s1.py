#Session 1 Prompt: 
#Write a Python program to print out your full name
#your preferred pronouns (optional)
#and two sentences about your favorite movie 
#and your favorite food.

def aboutMe():
	#print out sentences
	print("April Le\n(she\\they)")
	print("My favorite movie is The Prince of Egypt by Dreamworks.")
	print("My favorite food is the Vietnamese noodle soup called Pho.\n")

def main():
	aboutMe() #calls the function

#failsafe executable
if __name__=="__main__":
	main()
