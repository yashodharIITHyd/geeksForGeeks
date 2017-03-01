boxes = [ [4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32] ]

class boxStacking:
    def __init__(self,boxes):
        self.boxes = []
        for box in boxes:
            for box2 in self.rotate(box):
                self.boxes.append(box2)
        self.n = len(self.boxes)
        self.boxes = [e for e in sorted(self.boxes)[::-1]]
        self.n = len(self.boxes)
        self.arr=[0 for _ in range(self.n)]
        self.arr[0]=self.boxes[0][3]
        print self.boxes

    def rotate(self,l):
        l1=len(l)
        res2=[]
        for i in range(l1):
            res=l[i:]+l[:i]
            v=[res[0]*res[1]]
            v.extend(res)
            res2.append(v)
        return res2

    def check1(self,l1,l2):
        return len(set(l1).intersection(set(l2)))==0

    def bottomUp(self):
        for i in range(1,self.n):
            l1=[self.arr[k] for k in range(i) if self.check1(self.boxes[k][1:3],self.boxes[i][1:3])]
            self.arr[i]=self.boxes[i][3]
            if len(l1)>0:
                self.arr[i]+=max(l1)
        print self.arr

b1 = boxStacking(boxes)
b1.bottomUp()