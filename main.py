import random
import string
import colorama
from pyfiglet import figlet_format

colorama.init()

def generate_capital_code(num_words):
    letters = string.ascii_uppercase
    codes = []

    for _ in range(num_words):
        code = ''.join(random.choice(letters) for _ in range(4))
        green_code = colorama.Fore.GREEN + code + colorama.Fore.RESET
        codes.append(green_code)

    return '\n'.join(codes)

banner = figlet_format("lock break", font="slant")
print(colorama.Fore.GREEN + banner + colorama.Fore.RESET)
print("Welcome to lock break, a program designed to help you with your lock.")

try:
    num_words = int(input("Enter the number of codes you want: "))
    if num_words <= 0:
        raise ValueError("The number of codes must be a positive integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    print(generate_capital_code(num_words))

colorama.deinit()
