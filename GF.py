import sys
import time
import random

num ="0123456789"



def menu():
	print(" 1. Genarate Group UID")
	print(" 2. Add with group link.")
	
	velox = int(input("Enter: "))
	
	
	if velox == 1:
		genarate()
	elif velox == 2:
		work()

def genarate():
	
	file =open("/sdcard/Group_UID.txt","w")
	lim = int(input("Limit: "))	
	for x in range(lim):
		
		ww = "".join(random.choice(num) for i in range(16))
		print(ww)
		
		file.write(ww+"\n")
		
	file.close()
		

def work():
	nm = input(" Enter File Name: ")
	g = ""
	id = []
	for line in open(nm,"r").readlines():
   	 id.append(line.strip())
   	 
   	 words = line.split(". ")
   	 if words[0].isnumeric():
  	      sys.stdout.write(g+words[1])
  	      time.sleep(0.01)
  	      open("/sdcard/G_file/done.txt","a").write(g+words[1])


if __name__=='__main__':
	menu()
