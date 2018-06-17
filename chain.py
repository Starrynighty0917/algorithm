
'''
此链只是我按照自己的思路写出来的：
1 还有很多方法没有写
2 很多方法没有达到最佳的效果
3 有些方法可以通过多种方法来实现，比如reverse翻转函数
4 参考下思路即可

另外对我想法的链做个简单的介绍：
1 head_node是一个链的头节点，不带值
2 length记录链的长度
3 tail指向尾节点，只是记录位置，并不是一个真的Node
4 索引从0开始，规定第一个节点的索引值为0
'''


class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class MyChain():
    length = 0

    def __init__(self):
        self.head_node = Node()
        self.tail = self.head_node

    # 增
    # 头插法
    def head_add(self, value=None):
        self.head_node.next = Node(value, next=self.head_node.next)
        self.length += 1
        if self.tail == self.head_node:
            self.tail = self.head_node.next
        return True

    # 位置插法
    def insert(self, index, value=None):
        if not isinstance(index, int):
            raise ValueError("index应为整数。")
        if index < 0:
            raise ValueError("index应大于等于(0)。")
        if index >= self.length:
            self.tail_add(value)
            return True
        if index == 0:
            self.head_add(value)
            return True
        start_node = self.head_node
        change_node = self.head_node.next
        for i in range(index):
            start_node = start_node.next
            change_node = change_node.next
        start_node.next = Node(value, change_node)
        self.length += 1
        if self.tail == start_node:
            self.tail = start_node.next
        return True

    # 尾插法
    def tail_add(self, value=None):
        self.tail.next = Node(value, self.tail.next)
        self.tail = self.tail.next
        self.length += 1
        return True

    # 删
    # 按照索引删除
    def delete_index(self, index=None):
        if self.length == 0:
            raise ValueError("链长为(0)，无法删除节点。")
        if not isinstance(index, int):
            raise ValueError("index应为整数。")
        if (index < 0) or (index >= self.length):
            raise ValueError("index应小于链长(" + str(self.length) + "),大于等于(0)。")
        start_node = self.head_node
        delete_node = self.head_node.next
        for i in range(index):
            start_node = start_node.next
            delete_node = delete_node.next
        # 记录要删除的节点
        final_node = delete_node
        start_node.next = delete_node.next
        # 把记录节点的next置为空
        final_node.next = None
        self.length -= 1
        return final_node

    # 按照值删除，只删除第一个值，并返回第一个值的索引
    def delete_value(self, value=None):
        start_node = self.head_node
        delete_node = self.head_node
        for i in range(self.length):
            if i == 0:
                delete_node = delete_node.next
            if delete_node.value == value:
                if delete_node == self.tail:
                    self.tail = start_node
                final_node = delete_node
                start_node.next = delete_node.next
                final_node.next = None
                self.length -= 1
                return i
            start_node = start_node.next
            delete_node = delete_node.next
        raise ValueError("无法在链中找到(" + str(value) + "),故无法删除。")

    # 改
    # 按照索引修改
    def alter_index(self, index=None, value=None):
        if not isinstance(index, int):
            raise ValueError("index应为整数。")
        if (index < 0) or (index >= self.length):
            raise ValueError("index应小于链长(" + str(self.length) + "),大于等于(0)。")
        start_node = self.head_node.next
        for i in range(index):
            start_node = start_node.next
        start_node.value = value
        return True

    # 查
    # 打印链表的结构
    @property
    def all(self):
        chain = ""
        now_node = self.head_node.next
        for i in range(self.length):
            ok = str(i) + " : " + str(now_node.value)
            if i == (self.length - 1):
                chain += ok
            else:
                chain += ok + " --> "
            now_node = now_node.next
        print(chain)

    # # 按照索引查找并返回值
    def search_index(self, index=None):
        if not isinstance(index, int):
            raise ValueError("index应为整数。")
        if (index < 0) or (index >= self.length):
            raise ValueError("index应小于链长(" + str(self.length) + "),大于等于(0)。")
        start_node = self.head_node.next
        for i in range(index):
            start_node = start_node.next
        return start_node.value

    # 按照值查找并返回索引
    def search_value(self, value=None):
        start_node = self.head_node
        for i in range(self.length):
            start_node = start_node.next
            if start_node.value == value:
                return i
        raise ValueError("无法在链中找到(" + str(value) + ")。")

    @property
    def reverse(self):
        if self.length == 0:
            raise ValueError("链长为(0)，无法反转链表。")
        if self.length == 1:
            self.all
            return
        previous =self.tail
        j = self.length - 1
        for i in range(j):
            delete_node = self.delete_index(0)
            if i == 0:
                # 第一次在尾节点添加
                self.tail.next = delete_node
                self.tail = self.tail.next
            if i != 0:
                # 之后均在previous后添加
                delete_node.next = previous.next
                previous.next = delete_node
            self.length += 1
        self.all
        return


if __name__ == "__main__":
    chain=MyChain()
    try:
        for i in range(10):
            chain.tail_add(i)
        for i in  range(10):
            chain.head_add(i)
        chain.all
        chain.reverse
        print(chain.tail, chain.tail.value)
        # final_node = chain.delete_index(0)
        # print(chain.search_index(0))
        # print(final_node, final_node.next, final_node.value)
        my_chain = MyChain()
        # my_chain.delete_index(9)
        my_chain.all
        my_chain.tail_add(5)
        my_chain.all
        my_chain.head_add(3)
        my_chain.all
        my_chain.insert(1, 99)
        # my_chain.delete_index(0)
        # my_chain.delete_index(0)
        a = my_chain.delete_value(99)
        my_chain.insert(66, 23)
        my_chain.alter_index(1, 66)
        my_chain.tail_add(5)
        my_chain.head_add(3)
        a = my_chain.search_index(3)
        b = my_chain.search_value(23)
        my_chain.all
        print("length:", my_chain.length, " tail:", my_chain.tail.value, a, b)
        my_chain.insert(5, 9)
        my_chain.tail_add(10)
        my_chain.all
        print(my_chain.length, my_chain.tail.value)
    except ValueError as e:
        print(e)
