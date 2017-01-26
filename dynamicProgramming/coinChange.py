coins=[2,3,5]
amount=10
class coinChange:
    def __init__(self,coins,amount):
        self.coins=coins
        self.amount = amount
        self.n=len(coins)
        self.values = [0 for _ in range(self.amount+1)]
        self.values[0]=1

    def bottomUp(self):
        print self.values
        for i in range(1,self.n+1):
            pivot=self.coins[i-1]
            while pivot<=self.amount:
                self.values[pivot]+=self.values[pivot-self.coins[i-1]]
                pivot+=1
            print self.values

c1 = coinChange(coins,amount)
c1.bottomUp()