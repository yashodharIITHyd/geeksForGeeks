s1="BBABCBCAB"
class longestPalindromeSubsequence:
    def __init__(self,s1):
        self.s1 = s1
        self.n = len(s1)
        self.mat = [[1 for _ in range(self.n)] for _ in range(self.n)]

    def display(self):
        for i in self.mat:
            print " ".join([str(e) for e in i])
        print

    def bottomUp(self):
        for i in range(self.n-1):
            if self.s1[i]==self.s1[i+1]:
                self.mat[i][i+1]=2

        k=2
        while k<self.n:
            i=0
            j=k
            while i<self.n and j<self.n:
                if self.s1[i]==self.s1[j]:
                    self.mat[i][j]=2+self.mat[i+1][j-1]
                else:
                    self.mat[i][j]=max(self.mat[i+1][j],self.mat[i][j-1])
                i+=1
                j+=1
            k+=1
l1=longestPalindromeSubsequence(s1)
l1.bottomUp()
l1.display()