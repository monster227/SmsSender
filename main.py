import os, logo

from sender import sender

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear()

    print(logo.logo)

    while True:
        phone = input("Введите номер (без '+'): ")
        if phone.isdigit():
            phone = int(phone)
            break

    text = input("Введите текст: ")

    sender(phone, text)

if __name__ == "__main__":
    main()


