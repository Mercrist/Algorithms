from weightedQuickUnion import WeightedQU
class wquPath(WeightedQU):
    '''Weighted Quick Union but all nodes point instead to the root'''
    def find(self, p):
        '''Connects all nodes to the root as it goes up'''
        '''Worst Case: Almost Θ(1), unions is Θ(N). Amortized Constant time.'''
        if self.id[p] == p: #is a root
            return p                         #id[i] is the parent
        self.id[p] = p = self.id[self.id[p]] #https://stackoverflow.com/questions/12696803/weighted-quick-union-with-path-compression-algorithm
        return self.find(self.id[p])

if __name__ == "__main__":
    uf = wquPath(10)
    print(str(uf.count) + " components")
    #Should return False since these components aren't connected yet
    print("Is 4 connected to 5: " + str(uf.connected(4,5)))
    #return True since 4 and 5 are connected
    uf.union(4,5)
    print("Is 4 connected to 5: " + str(uf.connected(4,5)))

    #Check if 1 is connected to 4 since 4 is connected to 5
    print("Is 1 connected to 4: " + str(uf.connected(1,4)))
    #1 is connected to 5 so now it should be connected to 4
    uf.union(1,5)
    print("Is 1 connected to 4: " + str(uf.connected(1,4)))
    print(str(uf.count) + " components")