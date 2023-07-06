
def sum(a,b,c):
    return a + b + c


def printBoard(xState, zState): 
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")

def checkWin(xState, zState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X won the match !!!")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the match !!!")
            return 0
    return -1


if __name__ == "__main__": 
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for O
    print("\nWelcome to Tic Tac Toe")
    print("\n----------------------------------------------------------------------------------------------------------\n")
    print("Rules for the game: \n")
    print("1. The game is played on a grid that's 3 squares by 3 squares.\n")
    print("2. You are X and your friend is O. Players take turns putting their marks in empty squares(in this case you put the values displayed on the screen).\n")
    print("3. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n")
    print("\n----------------------------------------------------------------------------------------------------------\n")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("\nX's Chance")
            value = int(input("\nPlease enter a value where you want to put X: "))
            xState[value] = 1
        else: 
            print("\nO's Chance")
            value = int(input("\nPlease enter a value where you want to put O: "))
            zState[value] = 1
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("\nMatch Over...")
            break

        turn = 1 - turn