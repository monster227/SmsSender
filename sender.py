import requests, traceback

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

        print(f"\nSMS SENDEND!\n")
    except Exception as e:
        print(f"\n[*] ERROR: {e}\n")
        traceback.print_exc()


