import copy

mat = [ [1, 2, 3],
      [4, 8, 2],
      [1, 5, 3]
]

class minCostPath:
    def __init__(self,mat):
        self.mat=mat
        self.m=len(mat)
        self.n=len(mat[0])
        self.mat2=copy.deepcopy(mat)

    def display(self):
        for i in self.mat2:
            for j in i:
                print j,
            print
        print

    def bottomUp(self):
        self.mat2[0] = [self.mat[0][0]]+[self.mat[0][i-1]+self.mat2[0][i] for i in range(1,self.m)]
        for i in range(1,self.n):
            self.mat2[i][0]=self.mat2[i][0]+self.mat[i-1][0]

        for i in range(1,self.m):
            for j in range(1,self.n):
                self.mat2[i][j]=self.mat[i][j]+min(self.mat2[i-1][j-1],self.mat2[i][j-1],self.mat2[i-1][j])

m1 = minCostPath(mat)
m1.bottomUp()
m1.display()