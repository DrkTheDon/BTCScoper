#!/usr/bin/python3

#####################################################
## BTCScoper                                       ##
## For the Memes                                   ##
## https://drkbro.ml                               ##
## Coded by: drk                                   ##
#####################################################

# Imports
import random
import time
import os
from colorama import Fore
import requests
import pyfade
import json
from pystyle import Colorate, Colors

# Important Defines
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')

# Code
def credits():
    print(Colorate.Horizontal(Colors.green_to_red, """
   BTCScoper (May 22 2022) BY DRK#1337
  ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗
 ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
 ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗
 ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║
 ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║
  ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝            


DISCORD: https://discord.gg/CU53pZTA7e
Author: drk#1337
GITHUB: https://github.com/DrkTheDon
Language: Python

                                                                          """))
    input("\n Press enter to go back.")
    clearcmd()
    home()

def price():
    print(Colorate.Horizontal(Colors.green_to_red, """
   BTCScoper (May 22 2022)
  ██████╗ ████████╗ ██████╗    ██████╗ ██████╗ ██╗ ██████╗███████╗
  ██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██║██╔════╝██╔════╝
  ██████╔╝   ██║   ██║         ██████╔╝██████╔╝██║██║     █████╗  
  ██╔══██╗   ██║   ██║         ██╔═══╝ ██╔══██╗██║██║     ██╔══╝  
  ██████╔╝   ██║   ╚██████╗    ██║     ██║  ██║██║╚██████╗███████╗
  ╚═════╝    ╚═╝    ╚═════╝    ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝
                                                                                     
                                                                          """))
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    print(f"The current price of {Colors.yellow}1 BTC {Fore.LIGHTWHITE_EX}is{Colors.yellow}", f"${price}", Fore.LIGHTWHITE_EX)
    
    print("""
    [1] Convert USD to BTC
    [2] Go back
    
    
    """)
    USER_OPTION = input(f"Option\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        response = requests.get("https://blockchain.info/tobtc?currency=USD&value=1")
        print
        
    elif USER_OPTION == "2":
        clearcmd()
        home()

    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not reckognize input {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Try again.")
        time.sleep(1)
        input("\n Press enter to go back.")
        clearcmd()
        price()


def scoper():
    pass

def home():
    print(Colorate.Horizontal(Colors.green_to_red, """
   Version MEME (May 22 2022)
  ██████╗ ████████╗ ██████╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
  ██╔══██╗╚══██╔══╝██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
  ██████╔╝   ██║   ██║     ███████╗██║     ██║   ██║██████╔╝█████╗  ██████╔╝
  ██╔══██╗   ██║   ██║     ╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗
  ██████╔╝   ██║   ╚██████╗███████║╚██████╗╚██████╔╝██║     ███████╗██║  ██║
  ╚═════╝    ╚═╝    ╚═════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝                      
                                                                          """))
    print(f'''{Fore.LIGHTWHITE_EX}                    [ Made by {Colors.red}drk#1337 {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print("""
    [1] Scope BTC
    [2] Check BTC Price

    [3] Credits
    [4] Quit
    
    
    """)
    USER_OPTION = input(f"Option\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        
    elif USER_OPTION == "2":
        clearcmd()
        price()
    elif USER_OPTION == "3":
        clearcmd()
        credits()
    elif USER_OPTION == "4":
        clearcmd()
        quit()
    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not reckognize input {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Try again.")
        time.sleep(1)
        input("\n Press enter to go back.")
        clearcmd()
        home()

# Main Code
if __name__ == "__main__":
    clearcmd()
    home()
else:
    print("[-] Error: This file is not meant to be imported.")

