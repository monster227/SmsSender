# https://github.com/KrasProject-2021
# Copyright (C) 2021  KrasProject-2021

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

import requests

def proxy():
    request = requests.get(
            "https://www.proxyscan.io/api/proxy?format=json&type=http&country=us&Anonymity=elite"
        ).json()

    proxy = request[0]
    ip = proxy["Ip"]
    port = proxy["Port"]

    return (f"{ip}:{port}")
