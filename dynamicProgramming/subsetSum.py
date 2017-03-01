numbers=[3, 34, 4, 12, 5, 2]
amount=9
class subsetSum:
    def __init__(self,numbers,amount):
        self.numbers=numbers
        self.amount=amount
        self.n=len(numbers)
        self.mat=[[0 for _ in range(self.amount+1)] for _ in range(self.n+1)]
        for i in range(self.n+1):
            self.mat[i][0]=1
        for i in range(1,self.n+1):
            pivot=1#self.numbers[i-1]
            while pivot<=self.amount:
                if self.mat[i-1][pivot]==1:
                    self.mat[i][pivot]=1
                elif pivot>=self.numbers[i-1] and self.mat[i-1][pivot-self.numbers[i-1]]==1:
                    self.mat[i][pivot]=1
                pivot+=1

    def display(self):
        for i in self.mat:
            print " ".join([str(e) for e in i])
        print

s1=subsetSum(numbers,amount)
s1.display()