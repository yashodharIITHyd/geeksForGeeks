words = [3, 2, 2, 5]
width = 6
class wordWrap:
    def __init__(self,words,width):
        self.words = words
        self.n =len(words)
        self.width = width
        self.countMatrix = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.mat = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.countMatrix[i][i]=words[i]
            self.mat[i][i]=(width-words[i])**2
        k=1
        while k<self.n:
            i=0
            j=k
            while i<self.n and j<self.n:
                self.countMatrix[i][j]=self.countMatrix[i][j-1]+self.countMatrix[j][j]
                self.mat[i][j] = sum([self.mat[k1][k1] for k1 in range(i, j + 1)])
                if k==1:
                    if self.countMatrix[i][j]+j-i<=self.width:
                        self.mat[i][j]=min(
                            self.mat[i][j],
                            (self.width-self.countMatrix[i][j])**2
                        )
                else:
                    self.mat[i][j]=min(
                        self.mat[i][j],
                        min([self.mat[i][pivot]+self.mat[pivot+1][j] for pivot in range(i,j)])
                    )
                i+=1
                j+=1
            k+=1

    def display(self):
        for i in self.countMatrix:
            print ' '.join([str(e) for e in i])
        print

        for i in self.mat:
            print ' '.join([str(e) for e in i])
        print

w1 = wordWrap(words,width)
w1.display()