#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print (f"Numero {nr_numbers}")
password =[]

passwordchar=""



for i in range(1,nr_letters+1):
    password.append(random.choice(letters))
  #  print(f"estive aqui {i}")

for i  in range(1,nr_symbols+1):
    password.append(random.choice(symbols))
   # print(f"estive aqui {i}")

for i in  range(1, nr_numbers+1):
    password.append(random.choice(numbers))
   # print(f"estive aqui {i}")

random.shuffle(password)
print (password)
for char in password:
      passwordchar += char


print(passwordchar)