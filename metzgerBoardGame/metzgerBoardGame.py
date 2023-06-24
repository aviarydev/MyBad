##################
# avary metzger
# sdev 140
# final project
# last update: 12/17/2022
# spin-off of "Sorry!" aka "My Bad!"
##################


###########################

# different modules i have imported
import random # for dice
import re # for input validation
import time # for stylistic delays

######## functions ########

def diceRoll(): # roll dice
   input("Press enter to roll!")
   time.sleep(.5)
   dice1 = random.randint(1, 6)
   dice2 = random.randint(1, 6)
   total = dice1 + dice2
   return total

def rollDoubles(name): # roll doubles for first move
    playerDoubles[name] = False
    while not playerDoubles[name]:
        input("Press enter to roll!")
        time.sleep(.5)
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2:
            print("Yay! You rolled doubles.")
            playerDoubles[name] = True
        else:
            time.sleep(.25)
            print("You did not roll doubles :( Roll again.")
            time.sleep(.5)
    return dice1, dice2

def specialConditions(name, total, playerScores, playerNames): # all of the special conditions
    if total == 4: # reduce player's score by 1 
        playerNames.insert(max(0, playerNames.index(name)-1), playerNames.pop(playerNames.index(name)))
        playerScores[name] = playerScores[name] - 1
        time.sleep(.5)
        print("Apologies, Player, but you rolled 4, move back 1 space.")
    elif total == 5: # reduce player's score by 2
        playerNames.insert(max(0, playerNames.index(name)-2), playerNames.pop(playerNames.index(name)))
        playerScores[name] = playerScores[name] - 2
        time.sleep(.5)
        print("Bummer... you rolled a 5. Move back two spaces")
    elif total == 7:
        # check if there is a player in first place
        if len(playerNames) > 1:
            # supposed to swap the player's position with the player in first place (this isn't working properly)
            playerNames[playerNames.index(name)], playerNames[0] = playerNames[0], playerNames[playerNames.index(name)]
            time.sleep(.5)
            print("You rolled a 7, switch places with first place if applicable.")
    elif total == 8: #score is unchanged
        playerScores[name] = playerScores[name]
        time.sleep(.5)
        print("You rolled an 8, your score does not change.")
    elif total == 11:
        # supposed swap the player's position with the player in last place (this isn't working properly)
        playerNames[playerNames.index(name)], playerNames[-1] = playerNames[-1], playerNames[playerNames.index(name)]
        time.sleep(.5)
        print("Oh man... you rolled an 11, switch places with the player in last place if applicable.")
    elif total == 12: # score is reset to zero
        playerScores[name] = 0
        time.sleep(.5)
        print("My bad! You rolled a 12. Sadly, your score has been reset to 0.")
    return playerScores[name], playerNames

###########################

###### introduction ######

print("Hi there! Welcome to \"My Bad\" a game about being sorr- uhhh I mean... apologetic?")
time.sleep(2)
print("Anyway you can have up to 4 players in this game, but remember, you can't play by yourself.")
time.sleep(2)

###########################

####### player info #######

# gathering player info
numPlayers = int(input("Please enter how many players you have (2-4): ")) #ask user for number of players
while numPlayers < 2 or numPlayers > 4: # checks if they are playing alone or with too many people
    print("You can't play with that amount of players!")
    numPlayers = int(input("Please enter how many players you have (2-4): "))

# create a list that players get stored in
playerNames = []

# input validation for the name of each player
for i in range(numPlayers):
    # ask the user for the name of the player
    name = input(f"Enter the name of player {i+1}: ")

    # check if the input is a character using a regular expression
    match = re.fullmatch(r'[a-zA-Z]+', name)

    # if the input is not valid, display an error message and ask again
    while not match:
        print("The name must contain only characters.")
        name = input(f"Enter the name of player {i+1}: ")
        match = re.fullmatch(r'[a-zA-Z]+', name)

    # the input is valid, add it to the list of player names
    playerNames.append(name)

# dictionary that stores the score of the player
playerScores = {}

# dictionary that stores whether the players have rolled doubles
playerDoubles = {}

# initialize the scores and playerDoubles
for name in playerNames:
    playerScores[name] = 0
    playerDoubles[name] = False

###########################

###### the game itself ######

# determines whether or not the game is over
gameOver = False

print("Let's start the game! In order to roll you will have to press enter.") # fun let's get started message

# main game loop
while not gameOver:
    # loop through each player
    for name in playerNames:
        # roll the dice until the player has rolled doubles
        while not playerDoubles[name]:
            dice1, dice2 = rollDoubles(name)

        # calling the normal dice rolling function
        total = diceRoll()
            
        # store the player's previous score in case a special condition alters the score
        prevScore = playerScores[name]

        # calling the function with special conditions
        playerScores[name], playerNames = specialConditions(name, total, playerScores, playerNames)

        # making sure the player can't go over 50
        if playerScores[name] > 50:
            print("You can't go over 50 spaces!")
            playerScores[name] = prevScore

        # print the scores of each player
        print(f"{name}'s score: {playerScores[name]}")

    # checking if player won
    if playerScores[name] == 50:
        print(f"Congrats!! {name} has won the game!")
        # asking if player wants to play again?
        playAgain = input("Would you like to play another round of \"My Bad?\" (y/n): ") 
        if playAgain.lower() == "y":
             # resets the players scores and sets gameOver to False
            for player in playerScores:
                playerScores[player] = 0
            gameOver = False
        else:
            # if n is pressed then the game will end
            print("Thanks for playing!")
            gameOver = True

###########################
       

