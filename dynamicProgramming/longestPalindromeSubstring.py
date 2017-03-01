s="forgeeksskeegfor"

class lps:
    def __init__(self,s):
        self.s=s
        self.n=len(s)
        self.mat=[[0 for _ in range(self.n)]for _ in range(self.n)]
        maxLength=1
        maxSubstring=s[0]
        for i in range(self.n):
            self.mat[i][i]=1
            #print self.s[i]
        for i in range(self.n-1):
            if self.s[i]==self.s[i+1]:
                self.mat[i][i+1]=1
                maxLength=2
                maxSubstring=s[i:i+2]
                #print self.s[i:i+2]
            else:
                self.mat[i][i+1]=0
        k=2
        while k<self.n:
            i=0
            j=k
            while i<self.n and j<self.n:
                if self.s[i]==self.s[i+k] and self.mat[i+1][j-1]==1:
                    self.mat[i][j]=1
                    if maxLength<k:
                        maxLength=k
                        maxSubstring=s[i:j+1]
                    #print self.s[i:j+1]
                else:
                    self.mat[i][j]=0
                i+=1
                j+=1
            k+=1
        print maxLength,maxSubstring
    def display(self):
        for i in self.mat:
            print ' '.join([str(e) for e in i])
        print

l1=lps(s)
l1.display()