'''
  n_C_r = n-1_C_r-1 + n-1_C_r
'''

class binomialCoefficient:
    def __init__(self,n,r):
        self.n=n
        self.r =r
        self.mat=[['!' for _ in range(n+1)] for _ in range(r+1)]

    def display(self):
        for i in self.mat:
            print " ".join([str(e) for e in i])
        print

    def bottomUp(self):
        self.mat[0]=[0]+[1 for _ in range(1,self.n+1)]
        self.mat[1]=[0]+[i for i in range(1,self.n+1)]
        for i in range(1,self.r+1):
            self.mat[i][i]=1
        for i in range(2,self.r+1):
            for j in range(i+1,self.n+1):
                self.mat[i][j]=self.mat[i][j-1]+self.mat[i-1][j-1]

n,r=10,5
b1=binomialCoefficient(n,r)
b1.bottomUp()
b1.display()