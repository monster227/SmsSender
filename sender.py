# https://github.com/KrasProject-2021                           # Copyright (C) 2021  KrasProject-2021                                                                                          # This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
                                                                # You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

import requests

from colorama import Fore, Style
from fake_useragent import UserAgent
from proxy import proxy

ua = UserAgent()

def sender(phone, text):
    try:
        r = requests.post(
                "https://textbelt.com/text",
                {
                    'phone': f'+{phone}',
                    'message': f'{text}',
                    'key': 'textbelt',
                },
                proxies = {
                    "http": f"http://{proxy()}",
                    "https": f"http://{proxy()}"
                },
                headers = {
                        "User-Agent": ua.random,
                    },
            )

        print(Fore.GREEN + f"\nSMS SENDEND!\nRequest Status:\n{r}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\n[*] ERROR: {e}\n" + Style.RESET_ALL)
