from helper import player_board, player_turn, player_wins
import os

position = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
            6: '6', 7: '7', 8: '8', 9: '9'}

# player_board(position)

playing = True
end = False
turn = 0
prev_turn = -1

while playing:
    # Reset the screen display
    os.system('cls' if os.name == 'nt' else 'clear')

    player_board(position)

    # If invalid position was chosen in previous loop
    if prev_turn == turn:
        print("Invalid position chosen. try again")
    prev_turn = turn

    print("Go Player " + str((turn % 2) + 1) + ". Pick your position or 'q' to quit.")

    # Get input from player during their turn
    move = input()

    # Terminate While Loop
    if move == "q":
        playing = False

    # Check if player inputs a valid number from 1-9 as given on board
    elif str.isdigit(move) and int(move) in position:
        # Check if players chosen position has not been taken
        if not position[int(move)] in {"X", "O"}:
            # updates board if input is valid
            turn += 1
            position[int(move)] = player_turn(turn)

    # Check if someone has won or game has come to an end
    if player_wins(position):
        playing = False
        end = True
    if turn > 8:
        playing = False
# Game ended, print result
player_board(position)

# Tell who won
if end:
    if player_turn(turn) == 'X':
        print("Congratulations Player 1! You WIN!")
    else:
        print("Congratulations Player 2! You WIN!")
else:
    print("Its a Tie!")

print("Thanks for playing. Hope you had fun!")
