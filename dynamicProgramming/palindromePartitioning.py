s="ababbbabbababa"
#s="aaa"

class palindromePartition:
    def __init__(self,s):
        self.s=s
        self.n = len(s)
        self.boolPalindrome = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.palindromeMatrix=[['!' for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.boolPalindrome[i][i]=1
            self.palindromeMatrix[i][i]=0
        for i in range(self.n-1):
            if self.s[i]==self.s[i+1]:
                self.boolPalindrome[i][i+1]=1
                self.palindromeMatrix[i][i+1]=0
            else:
                self.palindromeMatrix[i][i+1] = 1
        
    def display(self):
        for i in self.boolPalindrome:
            print " ".join([str(e) for e in i])
        print

        for i in self.palindromeMatrix:
            print " ".join([str(e) for e in i])
        print

    def bottomUp(self):
        k=2
        while k<self.n:
            i=0
            j=k
            while i<self.n and j<self.n:
                if self.s[i]==self.s[j] and self.boolPalindrome[i+1][j-1]==1:
                    self.boolPalindrome[i][j]=1
                if self.boolPalindrome[i][j]==1:
                    self.palindromeMatrix[i][j]=0
                else:
                    self.palindromeMatrix[i][j]=1+min([self.palindromeMatrix[i][pivot]+self.palindromeMatrix[pivot+1][j] for pivot in range(i,j)])
                i+=1
                j+=1
            k+=1

p1 = palindromePartition(s)
p1.bottomUp()
p1.display()