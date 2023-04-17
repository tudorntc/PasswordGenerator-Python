import random
import string

print("How many characters do you want the password to have? ")
lenght = int(input("Enter the number: "))

def passwordGenerator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = passwordGenerator(lenght)
print("Your password is: " + password)  
