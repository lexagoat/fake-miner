from colorama import Fore
import time
import secrets
from random import randint

continuing = True

btcval = 31643.79

while True:
    if continuing == True:
        time.sleep(.01)
        ranInt = randint(0,2500)
        if ranInt <= 1:
            randomBTC = randint(1,100)/100
            print(Fore.WHITE + "> 0x" + secrets.token_hex(20))
            answer = input("> Would you like to continue? (Y/N) ")
            if answer.lower() == "y":
                continuing = True
            else:
                continuing = False
        else:
            print(Fore.WHITE + "> 0x" + secrets.token_hex(20) + Fore.RED + " > 0.00 BTC ($0.00)" )
    else:
        break
