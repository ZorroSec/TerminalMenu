import requests
from colorama import Fore, Style
from os import system
from time import sleep
from app.controllers import Default

def bank1():
    code = input(f"{Fore.LIGHTBLUE_EX}[*] code => {Style.RESET_ALL}")
    api = f"https://brasilapi.com.br/api/banks/v1/{code}"
    api = requests.get(api).json()
    for key, value in api.items():
        print(key, value)