from random import randrange
class Percolation():
    def __init__(self, n, T):
        '''Performs percolation runs on an nxn grid for a total of T trials.'''
        if n <= 0 or T <= 0:
            raise ValueError("Board size and number of trials must be greater than or equals to one.")
            
        self.p = float(randrange(0, 101)/100) #random decimal from [0, 1.0)
        self.board = [[0 for i in range(n)] for j in range(n)] #0s are closed sites, 1s are open sites
        

sim = Percolation(20,1)