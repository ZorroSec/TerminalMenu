import requests
from colorama import Fore, Style
from os import system
from time import sleep

class Default:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def time(self):
        sleep(4)
        print(f"{Fore.LIGHTGREEN_EX}[i] Espere @{self.name}")
    
    def clean(self):
        print(f"@{self.name}{Fore.LIGHTMAGENTA_EX}[i] Limppando a tela em 4 seg.")