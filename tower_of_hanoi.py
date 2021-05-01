import time

class TowerOfHanoi: 
    """Tower of Hanoi class encapsulating all related functions """

    Array2D = []
    total_moves = 0

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
        print("_______________________________________________________________")
        print("")



    def recursive_solver(self, rings_left = None, starting_peg = 1, target_peg = 3, other_peg = 2):
        """Solves the Tower of Hanoi game

        Key parameters: 
        rings_left   = Optional arg, defaults to the max number of rings. 
                       Otherwise it specifies the number of rings left that needs to be moved to the target. 
        starting_peg = The peg where the rings currently are
        target_peg   = The peg where we want the all the rings except the base ring to go to 
        other_peg    = The left over peg (since there are a total of 3 pegs)

        How the solver works: 
        The function must be able to move the top (rings_left - 1) rings to the other location, 
        such that the base ring can be moved to the target location. 
        It needs to be do this by recursively calling the function until only 2 rings are left, 
        where the base case is excuted. 
        """
        #sets up so the function can be called with no parameters
        if rings_left is None:
            rings_left = len(self.Array2D[0])
            self.print_state()
        #the Base case
        if rings_left == 2: 
            self.move(starting_peg, other_peg)
            self.move(starting_peg, target_peg)
            self.move(other_peg, target_peg)
            return
        else: 
            #the recursion portion
            rings_left = rings_left - 1 
            self.recursive_solver(rings_left, starting_peg, other_peg, target_peg)
            self.move(starting_peg, target_peg)
            self.recursive_solver(rings_left, other_peg, target_peg, starting_peg)



        

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
        start_col_index    = self.__next_available_index_start(start_row_index)
        target_col_index   = self.__next_available_index_target(target_row_index)

        #Get the ring number from the identified top-most ring location from the starting peg
        item = self.Array2D[start_row_index][start_col_index]
        #Clear the ring from the top-most ring location from the starting peg
        self.Array2D[start_row_index][start_col_index] = 0 

        #move the identified ring to the top-most ring location in the target peg
        #the "-1" in the col index of the array is to represent 
        self.Array2D[target_row_index][target_col_index] = item

        self.print_state()

        self.total_moves = self.total_moves + 1
        time.sleep(0.1)


    
    def __next_available_index_start(self, row_number): 
        """Returns the next column index in the row = row_number of the 2D array 
        where a ring currently exists. The ring can only be taken from a location where 
        there is a non-zero number. 

        Key parameters: 
        row_number = The row where we are investigating
        """
        #if the row is empty, return the bottom-most ring location
        if self.Array2D[row_number][0] == 0: 
            return 0

        #if the row is not empty and also not completely full, return the top-most ring
        for i in range(len(self.Array2D[row_number])):
            if self.Array2D[row_number][i] == 0:
                #Since the ring can only be taken from a non-zero location, 
                # we return the index before the index of the first zero
                return i-1 
        
        #if the row is completely full, return the top-most ring 
        return len(self.Array2D[row_number]) - 1 
    
    def __next_available_index_target(self, row_number): 
        """Returns the next column index in the row = row_number of the 2D array 
        where a ring can be placed. The ring can only be placed in a location where 
        there is a zero. 

        Key parameters: 
        row_number = The row where we are investigating
        """
        #if the row is empty, return the bottom-most ring location
        if self.Array2D[row_number][0] == 0: 
            return 0

        #if the row is not empty and also not completely full, return the top-most ring
        for i in range(len(self.Array2D[row_number])):
            if self.Array2D[row_number][i] == 0:
                #since the ring can only be placed in the location of a zero, 
                # we return the index of the first zero.
                return i
        
        #if the row is completely full, return the top-most ring 
        return len(self.Array2D[row_number]) - 1 

    def is_optimal(self):
        n = len(self.Array2D[0])
        if self.total_moves == 2**n - 1:
            return True
        else:
            return False
    
        

if __name__ == "__main__": 

    number_of_rings = input("How many rings would you like to solve the game for?")
    game = TowerOfHanoi(int(number_of_rings))
    game.recursive_solver()
    if game.is_optimal():
        print("The game was solved optimally")
    else: 
        print("The game was not solved optimally")