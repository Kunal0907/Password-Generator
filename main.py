#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#------------------------------------------------------#
#random password
password = " "
for i in range(1,nr_letters + 1):
  password += random.choice(letters)
for i in range(1,nr_symbols + 1):
  password += random.choice(symbols)
for i in range(1,nr_numbers + 1):
  password += random.choice(numbers)
print(f"Random password is: {password}")

#------------------------------------------------------#
#strong password
password_list = []
for i in range(1,nr_letters + 1):
  password_list += random.choice(letters[0:nr_letters])
for i in range(1,nr_symbols + 1):
  password_list += random.choice(symbols[0:nr_symbols])
for i in range(1,nr_numbers + 1):
  password_list += random.choice(numbers[0:nr_numbers])
random.shuffle(password_list)
password = ""
for char in password_list:
  password += char
print(f"Your strong password is: {password}")

