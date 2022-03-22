class LinkNode:  # 单链表的节点类
    def __init__(self, data=None):  # 初始化方法
        self.data = data  # 存储节点中的数据
        self.next = None  # 指向下一个节点的指针


class LinkList:  # 单链表类
    def __init__(self):
        self.head = LinkNode()  # 头节点head
        self.head.next = None

    def create_list_f(self, a):  # 头插法：由数组a整体建立单链表
        for i in range(len(a)):
            s = LinkNode(a[i])
            s.next = self.head.next
            self.head.next = s

    def create_list_r(self, a):  # 尾插法：由数组a来整体建立单链表
        t = self.head  # t始终指向尾节点，开始时指向头节点
        for i in range(len(a)):
            s = LinkNode(a[i])  # 生成一个新节点
            t.next = s  # 将s节点插入t节点之后
            t = s
        t.next = None  # 将尾节点的next成员置为空

    def get_node_i(self, i):
        """返回序号为i的节点"""
        p = self.head
        j = -1
        while (j < i and p is not None):
            j += 1
            p = p.next
        return p

    def add(self, e):
        """在单链表的末尾添加一个元素e"""
        s = LinkNode(e)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = s

    def getsize(self):
        """返回单链表中数据节点的个数"""
        p = self.head
        cnt = 0
        while p.next is not None:
            cnt += 1
            p = p.next
        return cnt

    def __getitem__(self, i):
        """求单链表中序号为i的元素的元素值"""
        assert i >= 0
        p = self.get_node_i(i)
        assert p is not None
        return p.data

    def __setitem__(self, i, e):
        """设置单链表中序号i的元素值"""
        assert i >= 0
        p = self.get_node_i(i)
        assert p is not None
        p.data = e

    def get_no(self, e):
        """求单链表中第一个值为e的元素的序号"""
        j = 0
        p = self.head.next
        while p is not None and p.data != e:
            j += 1
            p = p.next
        if p is None:
            return -1
        else:
            return j

    def insert(self, i, e):
        """在单链表中插入e作为第i个元素"""
        assert i >= 0
        s = LinkNode(e)
        p = self.get_node_i(i-1)
        assert p is not None
        s.next = p.next
        p.next = s

    def delete(self, i):
        """在单链表中删除序号i位置的元素"""
        assert i >= 0
        p = self.get_node_i(i-1)
        assert p != None and p.next is not None
        p.next = p.next.next

    def display(self):
        """输出单链表"""
        p = self.head.next
        while p is not None:
            print(p.data, end="")
            p = p.next
        print()
