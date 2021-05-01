
# Function to print out current progress given the 2D Array game progress representation

def print_state( Array2D = 0 ): 
    """ Prints the Tower of Hanoi progress.

    Keyword arguements: 
    Array2D -- the 2D Array representation of the game state

    3 row x n col array where n is the number of rings we start with
    Row i = peg i, for i = 0, 1, 2 
    Col i = the bottom-most ring. All numbers must be in decreasin consecutive sequence. 0 if no rings

    ex: 
        [4, 3, 0, 0] 
        [2, 0, 0, 0]
        [1, 0, 0, 0]

        should turn into: 

        3
        4  2  1
        =  =  =

    """ 


    n = len(Array2D[0])

    for col in range(n-1, -1, -1):
        for row in range(3):
            item = Array2D[row][col]
            if item == 0:
                print("  ", end=' ')
            else:
                print(f"{item} ", end=' ')
        print("")

    print("=  =  =  =")
        

if __name__ == "__main__": 

    Array2D = [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0]]
    print_state(Array2D)




