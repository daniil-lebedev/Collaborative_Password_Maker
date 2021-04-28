import random
import string
#Словарь
letters_low = string.ascii_lowercase
letters_up = string.ascii_uppercase
password = []
#Функция для первого случая
def choice1():
	for number in range(8):
		password.append(random.randrange(9))
	for upletter in range(4):
		password.append(random.choice(letters_up))
	for lowletter in range(4):
		password.append(random.choice(letters_low))

def choice2():
	number = int(input("Enter amound of numbers:\n"))
	upletter = int(input("Enter amound of uppercase letters:\n"))
	lowletter = int(input("Enter amound of lowercase letters:\n"))
	if number + upletter + lowletter <8:
		print("This password is too short try another one")
		choice2()
	elif number + upletter + lowletter == 8:
		print("This password is easy")
	elif number + upletter + lowletter >=8 and number + upletter + lowletter <12:
		print("This password is medium")
	else:
		print("This password is good")
	for number in range(number):
		password.append(random.randrange(9))
	for upletter in range(upletter):
		password.append(random.choice(letters_up))
	for lowletter in range(lowletter):
		password.append(random.choice(letters_low))

#Функция начала приложения
def start():
    print("Hello") #приветствие
    choice = int(input("Enter 1 if you wanna 16 integer password or 2 if you wanna generate it yourself:\n"))
    if choice == 1:
        choice1()
    elif choice ==2:
        choice2()
    else: 
    	print("This is wrong")
    	start()
start()
random.shuffle(password)
print("Your password is: ", password)