def RPS():
    options=["ROCK", "PAPER", "SCISSORS"]
    import random
    computerSelection=random.choice(options)
    return computerSelection


def playRPS(playerSelection, computerSelection):
    if playerSelection == computerSelection:
        print(playerSelection, computerSelection)
        print("DRAW!")
    elif playerSelection=="ROCK" and computerSelection=="PAPER":
        print(playerSelection, computerSelection)
        print("You lose!!! Paper beats Rock.")
    elif playerSelection=="ROCK" and computerSelection=="SCISSORS":
        print(playerSelection, computerSelection)
        print("You win!!! Rock beats Scissors")
    elif playerSelection=="PAPER" and computerSelection=="ROCK":
        print(playerSelection, computerSelection)
        print("You win!!! Paper beats Rock.")
    elif playerSelection == "PAPER" and computerSelection == "SCISSORS":
        print(playerSelection, computerSelection)
        print("You lose!!! Scissors beats Paper.")
    elif playerSelection == "SCISSORS" and computerSelection == "ROCK":
        print(playerSelection, computerSelection)
        print("You lose!!! Rock beats Scissors")
    elif playerSelection == "SCISSORS" and computerSelection == "PAPER":
        print(playerSelection, computerSelection)
        print("You win!!! Scissors beats Paper.")
    else:
        print(playerSelection, computerSelection)
        print("You have made a wrong entry")


playerSelection =input("Rock Paper or Scissors? ")
playerSelection = playerSelection.upper()

computerSelection= RPS()

playRPS(playerSelection, computerSelection)