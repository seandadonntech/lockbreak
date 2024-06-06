import random
import string
import colorama
from pyfiglet import figlet_format

colorama.init()

def generate_captial_code():
    letters = string.ascii_uppercase
    code = ''.join(random.choice(letters) for i in range(4))
   
    green_code = colorama.Fore.GREEN + code + colorama.Fore.RESET
    return green_code

banner = figlet_format("lock break", font="slant")
print(colorama.Fore.GREEN + banner + colorama.Fore.RESET)
print("Welcome to lock break a program designed to help you with your lock ")

option = input("Enter your option: \n")

if option == "1":
    print(generate_captial_code())

colorama.deinit()