# Assignment: Craps Dice Game
# Description: Create Craps Dice Game with a money betting system
# Name: Jerry He
# Date: June 10, 2021
# Course Code: ICS201-H3

# Variable Dictionary
# dice1 - stores the roll on the first dice
# dice2 - stores the roll on the second dice
# total - the sum of the values of dice1 and dice2 
# goal - stores the original total of the first roll if the game did not end
# bet - input by the user for the amount desired to be placed for a bet
# betCheck - saves the part after the negative sign of the bet if there is one
# wallet - stores total money left for placing bets

# import random so method can work
import random

# save $100 to the wallet used for bets
wallet = 100

# Save bet as a variable so it can be used in the loop
bet = 0
# Save betCheck as a variable so it can be used in the loop
betCheck = 0
# Save total as a variable so it can be used in the loop
total = 0

# Loop the program until user enters a negative number or out of money
while not(wallet <= 0 or str(bet)[0] == "-" and betCheck.isdigit()):

# Prompt the user for bet amount or to end program
    bet = input("""
Enter a number less than or equal to {} to bet.
(Or enter a negative number to end the game): """.format(wallet)) 
    
# Save the part after the negative sign to a variable       
    betCheck = str(bet[1:])    
        
# Check if the user entered a negative sign
    if bet[0] == "-":

# End the game if the user entered a negative number
        if betCheck.isdigit():
            print("Game Over!")

# Check if the input is an integer 
    if bet.isdigit():

# If so, change the type to an integer
        bet = int(bet)

# Check if the bet is greater than amount in wallet
        if bet > wallet:

# If so, tell user that input is not valid
            print("Not a valid input.")
        
# Repeat program if the user did not enter an positive integer 
    elif not(betCheck.isdigit()):
        print("Not a valid input.")
        
# Continue the program if input is a positive int less than or equal to wallet
    if str(bet).isdigit() and int(bet) <= wallet:

 # Randomize the values of both dice
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
            
# Add the total for both dice
        total = dice1 + dice2
            
# Save the original total as a goal 
        goal = total    

# Print the result
        print("{}, {}".format(dice1, dice2))

# Save the bet as an integer for calculations
        bet = int(bet)

# Check if the user rolled a 2, 3, or 12        
        if total == 2 or total == 3 or total == 12:
            print("You lose.")

# Subtract bet amount from wallet and print wallet amount  
            wallet = wallet - bet
            print("You have ${}".format(wallet))

# If the user bet all their money and lost, end the game
            if wallet <= 0:
                print("Game over, you're broke!")
                
# Check if the user rolled a 7 or 11        
        elif total == 7 or total == 11:

# Print a winning message if result was 7 or 11
            print("You win!")
            
# Add bet amount to wallet and print wallet amount
            wallet = wallet + bet
            print("You have ${}".format(wallet)) 
        
# If the total is not 2, 3, 12, 7, or 11, continue the second part of the game
        elif total != 2 and total != 3 and total != 12 and total != 7\
        and total != 11:
            
# Roll both dice again
            dice1 = random.randrange(1, 7)
            dice2 = random.randrange(1, 7)  
                                    
# Add the values and save to total
            total = dice1 + dice2
                                    
# Print the result
            print("{}, {}".format(dice1, dice2)) 
        
# Check if the total is equal to the goal or if the total is equal to 7
            if total != goal or total != 7:

# Loop the reroll of the dice until the total = goal or total = 7
                while not(total == goal or total == 7):
                    
# Roll both dice again
                    dice1 = random.randrange(1, 7)
                    dice2 = random.randrange(1, 7)  

# Add the values and save to total
                    total = dice1 + dice2

# Print the result
                    print("{}, {}".format(dice1, dice2)) 

# Check if the total is equal to the goal        
            if total == goal:
                
# Print a message indicating a win
                print("You win!")
                
# Add bet amount to wallet
                wallet = wallet + int(bet)

# Print amount of money left
                print("You have ${}".format(wallet))
    
# Check if the total is equal to 7
            elif total == 7:
                
# Print a message indicated a loss
                print("You lose.")
                            
# Subtract bet amount from wallet
                wallet = wallet - int(bet)

# Print amount of money left
                print("You have ${}".format(wallet))
                    
# If the user bet all money and lost, end the game
                if wallet <= 0:
                    print("Game over, you're broke!")   


