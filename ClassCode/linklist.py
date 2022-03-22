class LinkNode:  # 单链表的节点类  
    def __init__(self,data=None):  # 初始化方法
        self.data = data  # 存储节点中的数据
        self.next = None  # 指向下一个节点的指针
    

class LinkList:  # 单链表类 
    def __init__(self):
        self.head = LinkNode()  # 头节点head
        self.head.next = None
    
    def createlistf(self,a):  # 头插法：由数组a整体建立单链表
        for i in range(len(a)):
            s = LinkNode(a[i])
            s.next = self.head.next
            self.head.next = s
    
    def createlistr(self,a):  # 尾插法：由数组a来整体建立单链表
        t = self.head  # t始终指向尾节点，开始时指向头节点 
        for i in range(len(a)):
            s = LinkNode(a[i])  # 生成一个新节点
            t.next = s  # 将s节点插入t节点之后
            t = s
        t.next = None  # 将尾节点的next成员置为空
    
    def get_node_i()
        