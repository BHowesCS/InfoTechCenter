import random
from colorama import Fore

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = gasLevelGauge()

# Create IF-ELIF-ELSE statements using Comparative Operators == Equal To in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell", "BP", "Citgo", "Circle K", "Mobil", "Speedway", "Marathon", "Love's", "Meijer", "Costco"]
    if gasLevelIndicator == "Empty":
        print(Fore.RED+"***WARNING***\n**GAS EMPTY**\nCalling Emergency Contact"+Fore.RESET)
    elif gasLevelIndicator == "Low":
        print(Fore.LIGHTYELLOW_EX+"***WARNING***\n**LOW ON GAS**\nThe closest gas station is "+random.choice(gasStations)+Fore.RESET)
    elif gasLevelIndicator == "Quarter Tank":
        print(Fore.YELLOW+"QUARTER TANK Of Gas\nPlan On Visiting The Gas Station"+Fore.RESET)
    elif gasLevelIndicator == "Half Tank":
        print(Fore.LIGHTGREEN_EX+"HALF TANK Of Gas\n125 Miles Till Empty"+Fore.RESET)
    elif gasLevelIndicator == "Three Quarter Tank":
        print(Fore.GREEN+"THREE QUARTER TANK Of Gas\n205 Miles Till Empty"+Fore.RESET)
    else:
        print(Fore.GREEN+"FULL TANK Of Gas\n310 Miles Till Empty"+Fore.RESET)

# Call Functions Here
gasLevelAlert()
