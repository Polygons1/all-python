import pyttsx3
import time

brk = "y"
run = 0

main = pyttsx3.init()
while True:
	run = run + 1 
	main.say("p")
	time.sleep(2)
	main.say("e")
	time.sleep(2)
	main.say("g")
	time.sleep(2)
	main.say("e")
	time.sleep(2)
	main.say("r")
	if run == 1:
		main.runAndWait()
	if brk == "y":
		break