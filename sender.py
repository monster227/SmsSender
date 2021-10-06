import requests, traceback

from colorama import Fore, Style
from fake_useragent import UserAgent

ua = UserAgent()

def sender(phone, text):
    try:
        r = requests.post(
                "https://textbelt.com/text",
                data = {
                    'phone': f'+{phone}',
                    'message': f'{text}',
                    'key': 'textbelt',
                },
                headers = {
                        "User-Agent": ua.random,
                    },
            )

        print(Fore.GREEN + f"\nSMS SENDEND!\n" + Style.RESET_ALL)
        print(Fore.GREEN + f"Request Status:\n{r}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\n[*] ERROR: {e}\n" + Style.RESET_ALL)
        traceback.print_exc()


