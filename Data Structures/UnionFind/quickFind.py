class QuickFind:
    '''Uses site indexed array to determine whether two sites are connected to the same component'''
    def __init__(self, n):
        self.count = n #number of non connected components 
        self.id = [i for i in range(n)] #site indexed array
    
    def find(self, p):
        '''Returns id[p], value of that element on the sites'''
        return self.id[p]

    def connected(self, p, q):
        '''Checks if components are connected -> Bool'''
        return self.id[p] == self.id[q]

    def union(self, p, q):
        '''Connects p to q by changing their values in id to the same'''
        if self.connected(p, q):
            return None

        pID = self.id[p] #the array keeps changing so store their initial values
        qID = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID
                self.count -= 1
        return None

if __name__ == "__main__":
    uf = QuickFind(10)
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