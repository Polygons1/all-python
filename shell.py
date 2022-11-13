import platform
import random
import os

def nt():
	# cmd
	print(f"Microsoft Windows [Version {platform.version()}.{random.randint(800, 2000)}]")
	print("(c) Microsoft Corporation. All rights reserved.\n")

	fcwd = os.getcwd()

	while True:
		command = input(os.getcwd() + ">")
		if command == "cd.." or command == "cd ..":
			os.chdir("..")
		else:
			os.system(command)

def phosix():
	# sh
	while True:
		command = input("$ ")
		if command == "sh" or "/bin/sh" or "/usr/bin/sh":
			continue
		else:
			os.system(command)

if os.name == "nt":
	nt()
elif os.name == "phosix":
	phosix()
else:
	pass