class QuickUnion:
    '''Works with a tree structure where you keep indexing upwards through the array through the tree until the root is reached'''
    def __init__(self,n):
        self.count = n 
        self.id = [i for i in range(n)]

    def root(self, p):
        '''Follows links to the root'''
        '''Time complexity worst case: Tree height'''
        '''Worst Case: Θ(lg N) in weighted Quick Union'''
        if self.id[p] == p:
            return p
        return self.root(self.id[p])

    def find(self, i): 
        '''Finds the largest element in a component containing i'''
        maxElem = 0
        while self.id[i] != i: 
            i = self.id[i]
            if i > maxElem:
                maxElem = i
        return maxElem

    def connected(self, p, q):
        '''Checks if components are connected -> Bool'''
        return self.root(p) == self.root(q) #two elements are connected only if they share the same root
   
    def union(self, p, q):
        '''Connects two nodes by pointing root of p to root of q. Changes only one link.'''
        '''Time complexity worst case: Tree height'''
        if self.connected(p, q):
            return None
        self.id[self.root(p)] = self.root(q)
        self.count -= 1
        return None

if __name__ == "__main__":
    uf = QuickUnion(10)
    uf.union(2,4)
    uf.union(1,9)
    uf.union(2,3)
    print(uf.find(1)) #9 is the largest element in this component    