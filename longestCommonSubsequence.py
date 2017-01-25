s1="ABCDGH"
s2="AEDFHR"

class longestCommonSubsequence:
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2
        self.m=len(s1)
        self.n=len(s2)
        self.mat = [[0 for _ in range(self.n+1)] for _ in range(self.m+1)]

    def display(self):
        self.bottomUp()
        for i in self.mat:
            for j in i:
                print j,
            print
        print

    def bottomUp(self):
        for i in range(1,self.m+1):
            if self.s2[0]==self.s1[i-1]:
                self.mat[i][0]=1

        for i in range(1,self.n+1):
            if self.s1[0]==self.s2[i-1]:
                self.mat[0][i]=1

        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                if self.s1[i-1]==self.s2[j-1]:
                    self.mat[i][j]=1+self.mat[i-1][j-1]
                else:
                    self.mat[i][j]=max(self.mat[i][j-1],self.mat[i-1][j])


l1=longestCommonSubsequence(s1,s2)
l1.display()