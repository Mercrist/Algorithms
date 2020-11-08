from quickUnion import QuickUnion
class WeightedQU(QuickUnion):
    '''Keeps track of the size of each tree and instead, connects the smaller tree to the larger tree'''
    def __init__(self, n):
        self.count = n 
        self.id = [i for i in range(n)]
        self.size = [1 for i in range(n)] #seperate array keeps track of the weights of each node, all nodes start with a weight/size of 1

    def union(self, p, q):
        '''Connects smaller node to bigger node by pointing root of smaller node to root of bigger node. Changes only one link.'''
        '''Worst Case: Θ(lg N), also the same for find'''
        if self.connected(p, q):
            return None
        
        pRoot = self.find(p)
        qRoot = self.find(q)
        
        if self.size[pRoot] > self.size[qRoot]: #p is the bigger node, compare using size list 
            self.id[qRoot] = pRoot 
            self.size[pRoot] += self.size[qRoot] #add weight of q to p since p will be a "heavier" tree now
            self.count -= 1
        else: #q is the bigger node
            self.id[qRoot] = pRoot 
            self.size[pRoot] += self.size[qRoot]
            self.count -= 1
        return None

if __name__ == "__main__":
    uf = WeightedQU(10)
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