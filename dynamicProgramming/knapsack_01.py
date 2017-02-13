weights = [10,20,30]
values =[60, 100, 120]
amount = 50
class knapsack:
    def __init__(self,weights,values,amount):
        self.weights = weights
        self.values = values
        self.n = len(weights)
        self.amount = amount#sum(weights)
        self.mat=[[0 for _ in range(self.amount+1)] for _ in range(self.n+1)]

    def display(self):
        for i in self.mat:
            print " ".join([str(e) for e in i])
        print

    def bottomUp(self):
        for i in range(1,self.n+1):
            for j in range(1,self.amount+1):
                self.mat[i][j]=self.mat[i-1][j]
                if j>=self.weights[i-1]:
                    self.mat[i][j]=max(self.mat[i][j],self.values[i-1]+self.mat[i-1][j-self.weights[i-1]])
k1=knapsack(weights,values,amount)
k1.bottomUp()
k1.display()