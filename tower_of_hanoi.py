

class TowerOfHanoi: 
    """Tower of Hanoi class encapsulating all related functions """

    Array2D = []

    def __init__(self, numer_of_rings = 3):
        """ Creates the starting game array, with the numer of rings as the input 
        Key parameters: 
        n = number of rings, defaults to 3 if no input

        """
        n = numer_of_rings

        self.Array2D = [[0]*n for i in range(3)]
        self.Array2D[0] = [i for i in range(n, 0, -1)]

        


    def print_state( self ): 
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


        n = len(self.Array2D[0])

        for col in range(n-1, -1, -1):
            for row in range(3):
                item = self.Array2D[row][col]
                if item == 0:
                    print("  ", end=' ')
                else:
                    print(f"{item} ", end=' ')
            print("")

        print("=  =  =")



    def recursive_solver(self, rings_left = None, starting_peg = 1, target_peg = 3, other_peg = 2):
        """Solves the Tower of Hanoi game

        Key parameters: 
        rings_left   = Optional arg, defaults to the max number of rings. 
                       Otherwise it specifies the number of rings left that needs to be moved to the target. 
        starting_peg = The peg where the rings currently are
        target_peg   = The peg where we want the all the rings except the base ring to go to 
        other_peg    = The left over peg (since there are a total of 3 pegs)

        How the solver works: 
        The goal of the solver is to move the base of the ring stack to the target location.
        It does this by moving everything but the base ring to the other location. 
        Then the base ring is moved to the target location. 
        However unless the base case of just 2 rings are left, the function must be recursively called
        until there are just 2 rings left, with the new target switching to the "other_peg"
        """
        if rings_left is None:
            rings_left = len(self.Array2D[0])
            self.print_state()

        if rings_left == 2: 
            self.move(starting_peg, other_peg)
            self.move(starting_peg, target_peg)
            self.move(other_peg, target_peg)

        

    def move(self, starting_peg, target_peg):
        """Manipulates the 2D array to move the top most ring around.
        The ring is represented by cells within the 2D array

        Key parameters: 
        starting_peg = The peg where we want to move the ring from
        target_peg   = The peg where we want to move the ring to 
        """

        #Translation between the peg number of zero-index array
        start_row_index = starting_peg - 1
        target_row_index = target_peg - 1

        #Get the col index of the starting and target ring locations
        start_col_index    = self.__next_available_index(start_row_index)
        target_col_index   = self.__next_available_index(target_row_index)

        #Get the ring number from the identified top-most ring location from the starting peg
        item = self.Array2D[start_row_index][start_col_index]
        #Clear the ring from the top-most ring location from the starting peg
        self.Array2D[start_row_index][start_col_index] = 0 

        #move the identified ring to the top-most ring location in the target peg
        #the "-1" in the col index of the array is to represent 
        self.Array2D[target_row_index][target_col_index] = item

        self.print_state()


    
    def __next_available_index(self, row_number): 
        """Returns the next column index in the row = row_number of the 2D array 
        where a ring exists or where it can be placed

        Key parameters: 
        row_number = The row where we are investigating
        """
        #if the row is empty, return the bottom-most ring location
        if self.Array2D[row_number][0] == 0: 
            return 0

        #if the row is not empty and also not completely full, return the top-most ring
        for i in range(len(self.Array2D[row_number])):
            if self.Array2D[row_number][i] == 0:
                return i-1
        
        #if the row is completely full, return the top-most ring 
        return len(self.Array2D[row_number]) - 1 
        

if __name__ == "__main__": 

    game = TowerOfHanoi(2)
    game.recursive_solver()