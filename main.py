from display import display
from operation import add, sell
from restock import restock

import datetime

#---------------------------------------------------------------------------------------------------------------
'''  This is a code of one of the marketing where you can buy, add, display in this xitiz wholesale system. '''
#---------------------------------------------------------------------------------------------------------------

def main():
    """This code runs until valid input is entered for menu selection."""
    while True:
        print()
        print("*******************************************************************")
        print("======  Welcome to the SpeedzWear Wholesale Xitiz System  ======")
        print("*******************************************************************")
        print()
        print("You can selected your work according to your demand: \n")
        print(" 1. Display product")
        print(" 2. selling Product")
        print(" 3. Exiting the System")
        print(" 4. Adding Product")
        print(" 5. Restock Product\n")

#--------------------------------------------------------   
#  || you can achieve your request as per your need. ||
# -------------------------------------------------------

        try:
            select = int(input("Enter what you want to do from here: "))

            if select == 1:
                display() # This is display properties where we can see product

            elif select == 2:
                sell() # this is where we can sell product in market

            elif select == 3:
                print("Exiting the System. Thank you!") # existing system
                break

            elif select == 4:
                add() # this is where where we can add product

            elif select == 5:
                restock()#restock updte value

            else:
                print("Please enter a valid option: 0, 1, or 2.")

#------------------------------------------
# | If no input goes then exception exit |
#------------------------------------------

        except Exception as ex:
            print()
            print("-------------------")
            print("| Invalid input!. |")
            print("-------------------")

main()
