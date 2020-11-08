class QuickUnion:
    '''Works with a tree structure where you keep indexing upwards through the array through the tree until the root is reached'''
    def __init__(self,n):
        self.count = n 
        self.id = [i for i in range(n)]

    def find(self, p):
        '''Follows links to the root'''
        '''Time complexity worst case: Tree height'''
        '''Worst Case: Θ(lg N) in weighted Quick Union'''
        if self.id[p] == p:
            return p
        return self.find(self.id[p])

    def connected(self, p, q):
        '''Checks if components are connected -> Bool'''
        return self.find(p) == self.find(q) #two elements are connected only if they share the same root
   
    def union(self, p, q):
        '''Connects two nodes by pointing root of p to root of q. Changes only one link.'''
        '''Time complexity worst case: Tree height'''
        if self.connected(p, q):
            return None
        pRoot = self.find(p)
        qRoot = self.find(q)
        self.id[pRoot] = qRoot
        self.count -= 1
        return None

if __name__ == "__main__":
    uf = QuickUnion(10)
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