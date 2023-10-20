#Session 5 Prompt: Write a Python program that writes out a table of the function sin(x) vs. x, 
#where x is tabulated between 0 and 2 with a thousand entries. 
#Follow the basic Python program structure, including a main program function.

import numpy as np 
from astropy.table import Table #import the Table class
from astropy.io import ascii # ascii plain text io
from astropy.io import fits # FITS format io



def main():
	x = np.linspace(0,2*np.pi,1000) #0 to 2pi in 1000 entries
	y = np.sin(x) #function

	#np.savetxt('test.txt', np.transpose((x,y)), fmt='%4.3f %4.3f')

	data = Table([x,y],names=['x','sin(x)']) #create a talbe
	ascii.write(data, 'table.txt', format='commented_header') # write the table to file
	data_in = ascii.read('table.txt') #read the data in
	print(data_in) #print table

#failsafe executable
if __name__=="__main__":
	main()