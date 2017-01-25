import copy
mat=[
   map(int,"0  1  1  0  1".split("  ")),
   map(int,"1  1  0  1  0".split("  ")),
   map(int,"0  1  1  1  0".split("  ")),
   map(int,"1  1  1  1  0".split("  ")),
   map(int,"1  1  1  1  1".split("  ")),
   map(int,"0  0  0  0  0".split("  "))
]

class maxSquare:
    def __init__(self,mat):
        self.mat = mat
        self.m = len(mat)
        self.n = len(mat[0])
        self.mat2 = copy.deepcopy(mat)

    def display(self):
        for i in self.mat2:
            for j in i:
                print j,
            print
        print

        for i in self.mat:
            for j in i:
                print j,
            print
        print

    def bottomUp(self):
        for i in range(1,self.m):
            for j in range(1,self.n):
                if self.mat[i][j]>0:
                    min1=min(self.mat2[i-1][j-1],self.mat2[i][j-1],self.mat2[i-1][j])
                    self.mat2[i][j]=1+min1


m1= maxSquare(mat)
m1.bottomUp()
m1.display()
