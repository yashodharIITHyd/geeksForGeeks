arr=[1, 11, 2, 10, 4, 5, 2, 1]

class longestBitonicSubsequence:
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        self.left = [0 for _ in range(self.n)]
        self.right = [1 for _ in range(self.n)]

    def bottomUp(self):
        self.left[0]=1
        for i in range(1,self.n):
            subDp = [self.left[j] for j in range(i) if self.arr[j]<self.arr[i]]
            if len(subDp)>0:
                self.left[i]=1+max(subDp)
            else:
                self.left[i]=1

        j=self.n-2
        while j>=0:
            subDp = [ self.right[k] for k in range(j+1,self.n) if self.arr[j]>self.arr[k]]
            if len(subDp)>0:
                self.right[j]+=max(subDp)
            j-=1
        print self.left
        print self.right
        print [self.left[i]+self.right[i] for i in range(self.n)]
l1=longestBitonicSubsequence(arr)
l1.bottomUp()