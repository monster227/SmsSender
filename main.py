import os, logo, random, time

from colorama import Fore, Style
from sender import sender

def color():
    return random.choice([Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.CYAN, Fore.BLUE])

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear()

    print(color() + logo.logo + Style.RESET_ALL)
    print(color() + logo.p + Style.RESET_ALL)
    time.sleep(5)

    while True:
        phone = input(color() + "\nВведите номер (без '+'): " + Style.RESET_ALL)
        if phone.isdigit():
            phone = int(phone)
            break

    text = input(color() + "Введите текст: " + Style.RESET_ALL)

    sender(phone, text)

if __name__ == "__main__":
    main()


