s1="sunday"
s2="saturday"

class editDistance:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        self.m = len(s1)
        self.n = len(s2)
        self.mat = [[0 for _ in range(self.n+1)]for _ in range(self.m+1)]

    def display(self):
        self.bottomUp()
        for i in self.mat:
            for j in i:
                print j,
            print
        print

    def bottomUp(self):
        self.mat[0]=[i for i in range(self.n+1)]
        for i in range(self.m+1):
            self.mat[0][i]=i
        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                if self.s1[i-1]==self.s2[j-1]:
                    self.mat[i][j]=self.mat[i-1][j-1]
                else:
                    self.mat[i][j]=1+min(self.mat[i-1][j],self.mat[i][j-1],self.mat[i-1][j-1])

e1=editDistance(s1,s2)
e1.display()