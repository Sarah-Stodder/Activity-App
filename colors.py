
import os
from colorama import Fore, Style, init


#init for colorama to fixed windows wierdness
init()
 
 
def print_yellow(s):
        print(Fore.YELLOW, Style.BRIGHT, s, Style.RESET_ALL)
def print_red(s):
        print(Fore.RED, Style.BRIGHT, s, Style.RESET_ALL)
def print_blue(s):
        print(Fore.BLUE, Style.BRIGHT, s, Style.RESET_ALL)
def print_green(s):
        print(Fore.GREEN, Style.BRIGHT, s, Style.RESET_ALL)