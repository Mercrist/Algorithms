class SuccesorDelete():
    def __init__(self, n): 
        self.id = [i for i in range(n)]
        #a succesor of x is the number that should be the root of x+1 but that root will have been deleted, succesor is the next largest num
        self.succesors = [i for i in range(n)] #will hold the root of any removed number (number that was 'deleted' due to union)   
        self.size = [1 for i in range(n)] #weighted structures run in log time

    def find(self, p):
        '''Follows links to the root'''
        if self.id[p] == p:
            return p
        return self.find(self.id[p])

    def connected(self, p, q):
        '''Checks if components are connected -> Bool'''
        return self.find(p) == self.find(q) #two elements are connected only if they share the same root
   
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
            self.succesors[pRoot] = qRoot #list that corresponds to the root of any removed number
        else: #q is the bigger node
            self.id[qRoot] = pRoot 
            self.size[pRoot] += self.size[qRoot]
            self.succesors[pRoot] = qRoot 
        return None

    def remove(self, p):
        '''Removes a num, it's the same as joining it to that number+1'''
        return self.union(p,p+1)

    def succesor(self, p):
        return self.succesors[self.find(p+1)]

if __name__ == "__main__":
    uf = SuccesorDelete(10)
    uf.remove(5) #deletes 5
    uf.remove(6) #deletes 6
    print(uf.succesor(4)) #should be 7, 7 is the root of both 5 and 6, (4+1 is 5, 7 >= 4)