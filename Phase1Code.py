#Contributors:
#Alex, Galo, Joseph

prog_num=input("""What program would you like to run?
	(1) Unit converter
	(2) Blinking LED
	(3) Pygame demonstration
	? """)
prog_num=prog_num.strip()
print()

#----------------
# Unit Converter
#----------------
if prog_num=="1":
	decision = input("Would you like to convert units? yes or no: ")
	while(decision.lower() == "yes"):
		print("What unit would you like to convert?")
		unit = input("time(1), temperature(2), distance(3): ")

		if(unit == "1"):
			time_one = int(input("From: Hours(1), Seconds(2): "))
			time_two = int(input("To: Hours(1), Seconds(2): "))
			number = int(input("Choose a number: "))
			if(time_one == 1 and time_two == 2):
				number = number * 3600
				print(number)
				break
			elif(time_one == 2 and time_two == 1):
				number = round(number/3600,2)
				print(number)
				break
			else:
				print("You gabba gool, you ruined it.")
				print()


		if(unit == "2"):
			temperature_one = int(input("From: Fahrenheit(1), Celsius(2): "))
			temperature_two = int(input("To: Fahrenheit(1), Celsius(2): "))
			number = int(input("Choose a number: "))
			if(temperature_one == 1 and temperature_two == 2):
				number = round((number - 32)/1.8,2)
				print(number)
				break
			elif(temperature_one == 2 and temperature_two == 1):
				number = round(number*1.8 +32,2)
				print(number)
				break
			else:
				print("How did you possibly mess this up?")
				print()


		if(unit == "3"):
			distance_one = int(input("From: Feet(1), Meters(2): "))
			distance_two = int(input("To: Feet(1), Meters(2): "))
			number = int(input("Choose a number: "))
			if(distance_one == 1 and distance_two == 2):
				number = round(number/3.281,2)
				print(number)
				break
			elif(distance_one == 2 and distance_two == 1):
				number = round(number*3.281,2)
				print(number)
				break
			else:
				print("OHHHHH NOOOOO")
				print()
	else:
		print("Oh ok :(")

#--------------
# Blinking LED
#--------------
elif prog_num=="2":
	import RPi.GPIO as GPIO
	import time
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(19,GPIO.OUT)
	while 1:
		GPIO.output(19,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(19,GPIO.LOW)
		time.sleep(1)

#----------------------
# Pygame Demonstration
#----------------------
elif prog_num=="3":
	import pygame
	import random
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	BLUE = (0,0,255)
	screen_width = 600
	screen_height = 480
	screen=pygame.display.set_mode( (screen_width,screen_height) )


	#rectangle
	rectx = random.randint(200,360)
	recty = random.randint(120,360)
	rectw = random.randint(20,100)
	recth = random.randint(20,50)
	pygame.draw.rect(screen, WHITE, [rectx, recty, rectw, recth])


	#circle
	circler = random.randint(25,100)
	pygame.draw.circle(screen, BLUE, [circler,circler], circler)

	#text
	pygame.init()
	font = pygame.font.SysFont("freesans", 72)
	text = font.render('"Snowman"',True,WHITE)
	tw = text.get_width()
	screen.blit(text, [screen_width-tw, 5])

	pygame.display.flip()
