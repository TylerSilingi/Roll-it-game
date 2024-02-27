# checks users enters yes (y) or no (n)

def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instruction():
    print('''
    
    **** INSTRUCTIONS ****
    
To begin, decide on a score goal (eg: The first one to get a score of 50 wins).

For each round of the game, you win points by rolling dice.
The winner of the round is the one who gets 13 (or slightly less)

If you win the round, then your score will increase by the 
number of points that you earned.  If your first roll of two
dice is double (eg: both dice show a three), then your score 
will be double the number of points.

If you lose the round, then you dont get any points.

If you and the computer tie (eg: you both get a score of 11,
then you will have 11 points added to your score).

your goal is to try to get to the target score before the 
computer.

Good Luck.
    
    ''')


# Main routine
print()
print("🎲🎲Role it 13🎲🎲")
print()


want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
