class SqList:  # 顺序表类
    def __init__(self):  # 初始化方法
        self.initcapacity = 5
        self.capasity = 5  # 初始容量设置为5
        self.data = [None] * self.capasity  # 设置顺序表的存储空间
        self.size = 0  # 线性表的实际长度为0

    def resize(self, newcapacity):  # 改变顺序表的容量，使其容量为newcapacity
        assert newcapacity >= 0  # 确认顺序表的容量应该大于等于0
        olddata = self.data
        self.data = [None] * newcapacity
        self.capasity = newcapacity
        for i in range(self.size):
            self.data[i] = olddata[i]

    def createlist(self, a):
        for i in range(0, len(a)):
            if self.size == self.capasity:
                self.resize(2 * self.size)
            self.data[self.size] = a[i]
            self.size += 1

    def add(self, e):
        if self.size == self.capasity:
            self.resize(2 * self.size)
        self.data[self.size] = e
        self.size += 1

    def getsize(self):
        return self.size

    def __getitem__(self, i):
        assert 0 <= i < self.size
        return self.data[i]

    def __setitem__(self, i, x):
        """设置序号i的元素值"""
        assert 0 <= i < self.size
        self.data[i] = x

    def getno(self, e):
        """查找第一个为e的元素的序号"""
        i = 0
        while i < self.size and self.data[i] != e:
            i += 1
        if (i >= self.size):
            return -1
        else:
            return i

    def insert(self, i, e):
        """在顺序表中序号为i的位置上插入元素e"""
        assert 0 <= i <= self.size
        if self.size == self.capasity:
            self.resize(self.size * 2)
        for j in range(self.size, i-1, -1):
            self.data[j] = self.data[j-1]
        self.data[i] = e
        self.size += 1

    def delete(self, i):
        """删除表中序号为i的元素"""
        assert 0 <= i < self.size
        for j in range(i, self.size-1):
            self.data[j] = self.data[j+1]
        self.size -= 1
        if self.capasity > self.initcapacity and self.size <= self.capasity/4:
            self.resize(self.capasity//2)

    def display(self):
        for i in range(0,self.size):
            print(self.data[i],end="\n")
        print("finish")
        