chairs = [[5, 24], [39, 60], [15, 28], [27, 40], [50, 90] ]
class lisChainOfPairs:
    def __init__(self,chairs):
        self.chairs = chairs
        self.n = len(chairs)
        self.arr=[0 for _ in range(self.n)]
        self.arr[0]=1
    def bottomUp(self):
        for i in range(1,self.n):
            l1 = [self.arr[k] for k in range(i) if self.chairs[k][1]<self.chairs[i][0]]
            self.arr[i]=1
            if len(l1)>0:
                self.arr[i]+=max(l1)
        print self.arr

l1 = lisChainOfPairs(chairs)
l1.bottomUp()