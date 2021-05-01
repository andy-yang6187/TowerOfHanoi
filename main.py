
import printTOHascii

def create_array(n = 3):
    """ Creates the starting game array, with the numer of rings as the input 
    Key parameters: 
    n = number of rings, defaults to 3 if no input

    """
    Array2D = [[0]*n for i in range(3)]
    Array2D[0] = [i for i in range(n, 0, -1)]

    return Array2D




if __name__ == "__main__": 

    printTOHascii.print_state(create_array(n = 4))