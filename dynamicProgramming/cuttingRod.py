prices = map(int,['1', '5', '8', '9', '10', '17', '17', '20'])

class cuttingRod:
    def __init__(self,prices):
        self.prices = prices
        self.n = len(prices)
        self.arr = [0 for _ in range(self.n+1)]

    def bottomUp(self):
        self.arr[1]=self.prices[0]
        self.arr[2]=max(self.prices[1],2*self.arr[1])
        for i in range(3,self.n+1):
            count = 1
            pivot = (i)/2
            self.arr[i]=self.prices[i-1]
            while count<=pivot:
                val = self.arr[count]+self.arr[i-count]
                if self.arr[i]<val:
                    self.arr[i]=val
                count+=1

        print self.arr
c1=cuttingRod(prices)
c1.bottomUp()