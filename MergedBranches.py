#Welcome Branch
# Code Name - Hornet

# Print to one line with time delay between prints
from time import sleep
import colorama
from colorama import Fore
colorama.init(strip=False, autoreset=True)

print(Fore.MAGENTA+"Welcome to Hornet's InfoTechCenter\n")

sleep(1)

print("Hornet's Operating System Booting Up\n")

sleep(1)


#Gas Branch
import random

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
    miles = random.randint(1,25)
    if gasLevelIndicator == "Empty":
        print(Fore.RED+"***WARNING***\n**GAS EMPTY**\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print(Fore.LIGHTYELLOW_EX+"***WARNING***\n**LOW ON GAS**")
        print(Fore.LIGHTYELLOW_EX+"The closest gas station is "+random.choice(gasStations)+" which is "+str(miles)+" miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print(Fore.YELLOW+"QUARTER TANK Of Gas\nPlan On Visiting The Gas Station")
    elif gasLevelIndicator == "Half Tank":
        print(Fore.LIGHTGREEN_EX+"HALF TANK Of Gas\n125 Miles Till Empty")
    elif gasLevelIndicator == "Three Quarter Tank":
        print(Fore.GREEN+"THREE QUARTER TANK Of Gas\n205 Miles Till Empty")
    else:
        print(Fore.GREEN+"FULL TANK Of Gas\n310 Miles Till Empty")

# Call Functions Here
gasLevelAlert()
