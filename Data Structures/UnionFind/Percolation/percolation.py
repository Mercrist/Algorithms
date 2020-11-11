#https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php
from random import randrange
class Percolation:
    def __init__(self, n, T):
        '''Performs percolation runs on an nxn grid for a total of T trials.'''
        if n <= 0 or T <= 0:
            raise ValueError("Board size and number of trials must be greater than or equals to one.")
            
        self.p = float(randrange(0, 101)/100) #random decimal from [0, 1.0)
        self.board = [[0 for i in range(n)] for j in range(n)] #0s are closed sites, 1s are open sites
        self.tree = [[i for i in range(n)] for j in range(n)] #we can represent the sites as a Union Find tree, traversing to the top is the same as getting to the root

    def open(self, row, col):
        '''Opens a site at (row, col). Checks if there's any neighboring open sites and unions them.'''
        try:
            self.board[row][col] = 1
            if row == 0: #top row only has access to sites to the left, right, and down
                pass
            elif row == self.n-1: #bottom row only has access to sites to the top, right, left
                pass
            elif col == 0 or col == self.n-1: #sites on the edges only have access to top, bottom, left/right rows
                pass

            else:
                '''[CODE for any other site]'''
        except IndexError:
            raise ValueError("Indeces outside range, please input a valid board index.")
    
    def isOpen(self, row, col):
        try:
            return True if self.board[row][col] == 1 else False
        except IndexError:
            raise ValueError("Indeces outside range, please input a valid board index.")
    
    def isFull(self, row, col):
        '''A full site is an open site on the bottom row that connects to open sites on the top via adjacent sites. This means the system percolates.'''
        if row != self.n-1: #not a site on the last/bottom row
            raise ValueError("A system only percolates on the bottom row. Please re-input a valid row.")
        try:
            '''[CODE HERE]'''
        except IndexError:
            raise ValueError("Indeces outside range, please input a valid board index.")
    
    def numberOfOpenSites(self):
        return sum(row.count(1) for row in self.board) #adds how many open sites are in each row and returns that
    
    def percolates(self):
        '''Returns True if a system percolates.'''
        for i in range(self.n-1):
            if self.isFull(self.n-1, i) and self.isOpen(self.n-1, i): #checks if any open site on the bottom row percolates
                return True
        return False
    
sim = Percolation(20,1)
sim.open(19,19)
sim.open(5,6)
sim.open(10,11)
print(sim.numberOfOpenSites())