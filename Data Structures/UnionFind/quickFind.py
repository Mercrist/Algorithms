class QuickFind:
    def __init__(self, n):
        self.id = [i for i in range(n)] #site indexed array

    def connected(self, p, q):
        '''Checks if components are connected -> Bool'''
        return self.id[p] == self.id[q]

    def find(self, p):
        '''Returns id[p], value of that element on the sites'''
        return self.id[p]

    def union(self, p, q):
        '''Connects p to q by changing their values in id to the same'''
        if self.connected(p, q):
            return None

        pID = self.id[p] #the array keeps changing so store their initial values
        qID = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID
        return None

uf = QuickFind(10)
#return True since 4 and 5 get connected, there should be 9 components now
uf.union(4,5)
print(uf.connected(4,5))
#Should return False
print(uf.connected(1,5))
#Actually connects the, check if 1 is connected to 4 since 4 is connected to 5, should return True
uf.union(1,5)
print(uf.connected(1,4))