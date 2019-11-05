##find word
###import START

import time
import sys
import os 
from Cust_Exes import CustomException as err

###import END

#global variables START
BaseFolder=os.getcwd() #To get location where the file / program is stored to fetch the database
word_set1=set()        #to store values after comparison [compare_value()]
Final_word_set=set()#
count_dict = {} #

#global variables END



##will tell the prog whether the program is running continuously or is restarted, if restarted, count goes to 0, and count increases for rach run without restart 
countt = 0

##input letters form user
def input_letters():#checked
	print("enter letters  without giving space")
	letters = (input(">>"))
	print("below are leters")
	print(letters)
	return letters


def count_elem(letters):#checked
	"""This funciton counts occurance each letter in the given input and stores in to """
	global count_dict
	for i in letters:
			cc = letters.count(i)
			count_dict[i] = cc
	#return count_dict

##input length that is needed
def input_no():#checked
	print("enter the lenght you want")
	lenn = int(input(">>"))
	lenn += 1
	return str(lenn)

def get_value_from_db(size):#checked
	noss=size
	ff = open(BaseFolder+"\\database\\" + noss + ".txt", 'r')
	time.sleep(1)
	print("fetching value from databse ")
	time.sleep(1)
	#print("opening file:E:\py_prog\py_prog\word_puzzle\database\\" + noss + ".txt")
	rd = ff.readlines()
	return rd



def optimize_input(ip1,ip2): #--checked
	"""This function removes all the elements from ip1 that  do not match criteria
	 ip2 is fixed input which  dictionary[count_dict] that contain count of each letter given by user form count_elem function
	 we match this count with each element if ip1 and remove which does not match the criteria
	 eg: letters by user:alkd so count_dict will be {a:1,l:1,k:1,d:1}
	 
	 """
	##get count of each letter

	comp_dict = {}
	set1=set()
	for i in ip1:
		for j in i:
			cc=i.count(j)
			comp_dict[j]=cc
		#print(comp_dict)
		#compare with count_dict
		l = len(comp_dict)
		#print("l:",l)
		#print("our dict:",len(ip2))
		ccount=0
		flag=0
		for k in comp_dict:
			if k=='\n':
				flag=1
				ccount += 1
				#print(flag)

			if flag==1:
				pass

			else:

				if comp_dict[k]==ip2[k]:
						ccount+=1

				else:
						pass

		flag = 0
		#if pass add to set
		#print(ccount,l)
		if ccount>=l:
			set1.add(i)
		else:
			pass
		comp_dict.clear()

	#print(set1)
	return set1

def optimize_input_from_DB(list_from_db,letters,length):#--checked
	""" to filter the list form DB to reduce size of the list. This fun takes 3 values
		1.list form DataBase
		2.letters given by user
		3.size given by user
		
		eg letters gvn: ball; len=4; 
		word from DB: ball,bail,bakl....
		now this function will take only those words who have given lettes and length will be equal to len,and will reject other inp as: bail,balk etc
		sortlisted inputs are then inserted into a set and returned.
	"""

	ccc=0
	temp_set=set() # set is used as it avoid duplicate values  
	length=(int(length))-1
	for i in list_from_db:
		i=i.lower()

		for j in i:
			#print(j)
			if (j in letters)==True:
				ccc+=1
				#print(ccc)
			else:
				pass
		#print(ccc)

		if ccc==int(length):
			temp_set.add(i)
		ccc=0
	#print(temp_set)
	return temp_set



#main function
def main():
	#--user input starts
	try:
		lett=input_letters()
		number=input_no()
		if lett.isalpha()==False:
			
			raise err.ValueNotStringError()
		#print(len(lett))
		#print(int(number)>len(lett))
		if int(number)>(len(lett)+1):
			raise err.ValueExceedsLimitError()


	except Exception as e:
		print (e)
		main()
	else:
		pass

	# --user input ends


	
	count_elem(lett)

	#
	
        #this program have database that have alphabets arranged in sepatate files  according to length and not alphabeticall
	#input no will be let us know which file to open . 
	temp_list=get_value_from_db(number)

	#--optimization start
	
	#optimizing list retrived from database to only those words that contain lettes given by the use in input.
	w_set = optimize_input_from_DB(temp_list, lett,number) 
	
	#optimizing list further retrived optimize_input_from_DB() to only those words who containg lettes with exact count that was given by uses in the input
	#eg: letters: aabkcd; below funciton will only select the functions that will have a twice, b,k,c and d once. 
 
	w_set1=optimize_input(w_set,count_dict)  #
	# --optimization ends

	
	time.sleep(1)
	print("search complete")
	time.sleep(1)
	print("following is/are possible combination(s) ")
	
	time.sleep(1)
	
	#print the result
	
	

	
		
	print()
	
	#converting set into list for indexing 
	l_w_set=list(w_set1)
	
	## @printing_neatly_block_start 
	# following code will arrange the final_List into group of 5-5 and print on console
	for i in range(5):
		print("=",end=" ")
	counter=0
	while(counter<len(l_w_set)):
		w_word=l_w_set[counter]
		remove_new_line_char=(w_word[0:-1])
		print(remove_new_line_char,end=" ")
		counter+=1

		if (counter%5)==0:
			print()
		else:
			pass

	print()
	for i in range(5):
		print("=", end=" ")
	
	## @printing_neatly_block_end 
	#to print on next line
	print()
	

	#code to exit or re-run the prog. 
	print("to exit press enter, to continue press any key")
	chh = input(" >>")
	if chh == "":
		print("Thankyou fot Playing ")
		sys.exit(0)
	else:
		main()
#preliminaryCheck()
main()
