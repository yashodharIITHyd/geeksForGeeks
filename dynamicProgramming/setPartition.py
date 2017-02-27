numbers = [1, 5, 11, 5]

class partition:
    def __init__(self,numbers):
        self.numbers = numbers
        self.n = len(numbers)
        self.amount = sum(numbers)
        self.boolValue = (self.amount&1 == 0) and True or False
        self.amount/=2
        if self.boolValue:
            self.mat=[[0 for _ in range(self.amount+1)] for _ in range(self.n+1)]
            for i in range(self.n+1):
                self.mat[i][0]=1

    def display(self):
        for i in self.mat:
            print ' '.join([str(e) for e in i])
        print

    def bottomUp(self):
        if not self.boolValue:
            print 'We can\'t make the partition'
            return
        for i in range(1,self.n+1):
            pivot=self.numbers[i-1]
            while pivot<=self.amount:
                self.mat[i][pivot]=self.mat[i-1][pivot]+self.mat[i-1][pivot-self.numbers[i-1]]
                pivot+=1

p1 = partition(numbers)
p1.bottomUp()
p1.display()