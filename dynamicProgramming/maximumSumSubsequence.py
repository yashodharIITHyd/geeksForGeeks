arr=[1, 101, 2, 3, 100, 4, 5]

class maximumSumSequence:
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        self.dp = [i for i in arr]

    def bottomUp(self):
        for k in range(1,self.n):
            subDp = [j for j in range(k) if arr[j]<arr[k]]
            if len(subDp)>0:
                self.dp[k]=self.arr[k]+max([self.dp[pos] for pos in subDp])
        print self.dp

m1 = maximumSumSequence(arr)
m1.bottomUp()
