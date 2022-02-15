import random
from colorama import Fore

#Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    #print(currentGasLevel)
    return currentGasLevel

#Create IF-ELIF-ELSE statements using Comparative Operators to display gas level messages
def gasLevelAlert():
    if gasLevelGauge() == "Empty":
        print(Fore.RED+"     ***WARNING***\nYou have run out of gas"+Fore.RESET)


#gasLevelGauge()
gasLevelAlert()