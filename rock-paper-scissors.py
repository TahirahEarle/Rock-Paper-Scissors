import random

# Define a list of possible plays
options = ["rock", "paper", "scissors"]

# Keep playing until the user decides to quit
while True:
    # Randomly select a play for the computer
    computer_play = random.choice(options)

    # Initialize the player's play as None
    player_play = None

    # Keep asking the player to choose a play until they enter a valid option
    while player_play not in options:
        player_play = input("Choose rock, paper, or scissors, or type 'quit' to exit: ").lower()

        # If the player enters 'quit', exit the loop
        if player_play == 'quit':
            print("Thanks for playing!")
            break

        # If the player enters an invalid option, let them know
        if player_play not in options:
            print("Invalid input. Please try again.")

        # If the player's choice is the same as the computer's, it's a tie
        elif player_play == computer_play:
            print("It's a tie!")

        # Otherwise, compare the plays to determine the winner
        else:
            if player_play == "rock":
                if computer_play == "paper":
                    print("You lose! Paper covers rock.")
                else:
                    print("You win! Rock smashes scissors.")
            elif player_play == "paper":
                if computer_play == "scissors":
                    print("You lose! Scissors cut paper.")
                else:
                    print("You win! Paper covers rock.")
            else: # player_play == "scissors"
                if computer_play == "rock":
                    print("You lose! Rock smashes scissors.")
                else:
                    print("You win! Scissors cut paper.")

            # Show the computer's play
            print("Computer played", computer_play)
            
    # If the user chose to quit the game, break out of the outer loop
    if player_play == 'quit':
        break
