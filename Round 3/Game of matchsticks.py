"""
COMP.CS.100
Huyen Pham, huyen.pham@tuni.fi
Solution of task 3.3: Project: Game of Matchsticks
"""

def main():
    total = 21
    condition_1 = True
    condition_2 = True
    condition_Final = True
    print("Game of sticks")

    while condition_Final:
        # While loop to find player 1 input
        while condition_1:
            p1 = int(input("Player 1 enter how many sticks to remove: "))
            if 0 < p1 < 4:
                total -= p1 # Finding remaining number of matchsticks
                # If the total is smaller than 0, the loop will stop and determinant is set to player 1
                if total < 1:
                    determinant = 1
                    condition_Final = False # Stopping the entire loop for both players
                    break
                # Loop continues if total >=1
                print(f"There are {total} sticks left")
                condition_1 = False # Stopping the loop of player 1
                condition_2 = True # Starting the loop of player 2
            else:
                print("Must remove between 1-3 sticks!")

        # While loop to find player 2 input
        while condition_2:
            p2 = int(input("Player 2 enter how many sticks to remove: "))
            if 0 < p2 < 4:
                total -= p2 # Finding remaining number of matchsticks
                if total < 1:
                    determinant = 2
                    condition_Final = False # Stopping the entire loop for both players
                    break
                print(f"There are {total} sticks left")
                condition_2 = False # Stopping the loop of player 2
                condition_1 = True # Starting the loop of player 1
            else:
                print("Must remove between 1-3 sticks!")

    # Finding the loser using the determinant
    if determinant == 1:
        print("Player 1 lost the game!")
    else:
        print("Player 2 lost the game!")

if __name__ == '__main__':
    main()