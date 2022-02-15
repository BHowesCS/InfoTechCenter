import random
from colorama import Fore
#Gas Level Function

def gasLevelGauge():
    gasLevelList = [Fore.BLACK+"Empty",Fore.RED+"Low",Fore.YELLOW+"Quarter Tank",Fore.LIGHTGREEN_EX+"Half Tank",Fore.GREEN+"Three Quarter Tank",Fore.GREEN+"Full"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)

gasLevelGauge()