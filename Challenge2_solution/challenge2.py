#solution by Rhimesh 
#run in terminal $python challenge2.py

#!/usr/bin/env python3

import requests as req 
import time
import re
import json
import os

def testWords(jumbles):
	toBeReturn=''
	temp = open("temp.txt","r")
	jumbles = list(jumbles.split('\n'))

	print(((jumbles)))
	print(jumbles[9])
	for i in range(0, len(jumbles)):
		jumble = str(jumbles[i])
		# print(jumble)
		length = len(jumble)
		# print(len(jumble))
		jumble.strip(' ')
		jumble.strip('\n')
		temp.seek(0)
		for word in temp.readlines():
			word = word.strip('\n')
			word = word.strip(' ')
			word = word.strip('  ')
			# print("[*] equating with word "+word)
			correctness = 0
			match = 0
			if(len(word)== length):
				for x in range(0,length):
					# if (jumble.find(jumble[x],jumble.find(jumble[x])+1) != -1)
					temper = word
					if jumble[x] in word:
						# temper = temper[]
						correctness += 1
						# print(jumble[x])
						# print("in correctness of "+ jumble)
					if (correctness == length):
						# if( word == jumble):
							# print("[+] found word of "+jumble)
							match = 1
							toBeReturn = str(toBeReturn )+ str(word) + str(" ")
							break
			if(match == 1):
				temp.seek(0)
				match = 0
				break

		# print("[-] Word not found")

	temp.close()
	return toBeReturn	



def main():
	print(req.__version__)
	print(req.__copyright__)




	with req.Session() as s:
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'}
		res = s.get("http://secretmsg.6te.net/wordlist.txt")
		# print(resp.text)
		f = open("temp.txt","w+")
		f.write(res.text)
		f.close()
		
		startTime = time.time()

		res = s.get('http://secretmsg.6te.net/chpage.php')
		# print(resp.text)
		content = res.text
		refined = content[content.find('<ol>'):content.find('</ol>')]
		refined = re.sub('<[^<]+?>','',refined)
		refined = refined[2:-1]
		refined = refined.replace('  ', '\n') 
		correct = (testWords(refined))
		print(correct)
		correct = str('{') + str(correct[:-1]) + str('}')
		print(correct)
		val = {"ans": str(correct),'name' : 'kaladon' , 'roll' : 'THA075BEX303'}
		# val = [('ans',correct),('name','kaladon'),('roll','THA075BEX303')]
		res = s.post("http://secretmsg.6te.net/result.php", params=val, json = (val))
		print("the time for execution was "+ str(time.time()- startTime ))
		print(res.text)
	
	os.remove("temp.txt")
	print("clearing temporary file")

if __name__ == "__main__":
	main()
