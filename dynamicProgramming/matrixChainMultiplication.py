arr=[40, 20, 30, 10, 30]

class matrixChainMultiplication:
    def __init__(self,arr):
        self.arr=arr
        self.n = len(arr)-1
        self.mat = [[0 for _ in range(self.n+1)] for _ in range(self.n+1)]

    def display(self):
        for i in self.mat:
            for j in i:
                print j,
            print
        print

    def bottomUp(self):
        for i in range(1,self.n):
            self.mat[i][i+1]=self.arr[i-1]*self.arr[i]*self.arr[i+1]

        k=3
        while k<=self.n:
            i=1
            j=k
            while i<self.n and j<=self.n:
                self.mat[i][j]=min([self.mat[i][pivot]+self.mat[pivot+1][j]+self.arr[i-1]*self.arr[pivot]*self.arr[j] for pivot in range(i,j)])
                i+=1
                j+=1
            k+=1
m1=matrixChainMultiplication(arr)
m1.bottomUp()
m1.display()
