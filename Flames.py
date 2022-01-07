# FLAMES Application - Python 3.9 - Nizar Arjoun
import time

# Just some fancy schmancy things
print("    ______   __      ___      __  ___   ______  _____")
print("   / ____/  / /     /   |    /  |/  /  / ____/ / ___/")
print("  / /_     / /     / /| |   / /|_/ /  / __/    \__ \ ")
print(" / __/  _ / /____ / ___ |_ / /  / /_ / /___ _ ___/ / ")
print("/_/    (_)_____(_)_/  |_(_)_/  /_/(_)_____/(_)____(_) \n")
            
print("Welcome to Flames! We will predict your destiny with your partner!")
time.sleep(3)

def flames():

    # Name vairables, gets turned into lowercase and into lists
    name1Str = input("\nWhat is your name?: ")
    name2Str = input("\nWhat is your partner's name?: ")

    name1 = list(name1Str.lower())
    name2 = list(name2Str.lower())

    # Creates the commonChar variable to subtract letters from both names
    set_name1 = set(name1)
    intersection = set_name1.intersection(name2)
    commonChar = list(intersection)

    # Removes name 1 common characters
    remainingName1 = list(set(name1) - set(commonChar))

    # Removes name 2 common characters
    remainingName2 = list(set(name2) - set(commonChar))

    count1 = len(remainingName1)
    count2 = len(remainingName2)

    time.sleep(1)
    print("\n")
    print(name1Str, "          : ", remainingName1, " Count: ", count1) 
    print(name2Str, "          : ", remainingName2, " Count: ", count2)

    totalCount = count1 + count2
    print("\nTotal count: ", totalCount)

    flamesResult = {1: "Friend", 2: "Lovers", 3: "Affection", 4: "Marriage", 5: "Enemy", 6: "Siblings"}

    if totalCount > 6:
        totalCount = totalCount % 6
    print("\nYour flame is: ",flamesResult[totalCount],"!")

    x = input("\nWould you like to try again? (Y/N): ")

    if x == 'Y' or x== 'y':
        
        flames()
   
    else:
    
        exit()
    
    return 

flames()