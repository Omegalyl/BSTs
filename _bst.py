import random
from time import time
from bst import test
import sys
sys.setrecursionlimit(10000)


class _BstNode():
    def __init__(self, value, parent=None):
        self.value = value
        self.right = None
        self.left = None
        self.parent = parent
        self.size = 1
        self.depth = 0
        self.disconnect()


    def _insert(self, node, depth=0):
        if node.value > self.value:
            if self.right:
                self.size += 1
                depth += 1
                self.right._insert(node, depth)
            else:
                node.parent = self
                node.depth = depth + 1
                self.right = node
                self.size += 1
        else:
            if self.left:
                self.size += 1
                depth += 1
                self.left._insert(node, depth)
            else:
                node.parent = self
                node.depth = depth + 1
                self.left = node
                self.size += 1
        return depth

    def __bool__(self):
        return True

    def find(self, value):
        if value == self.value:
            return self
        elif value > self.value:
            if self.right:
                return self.right.find(value)
        else:
            if self.left:
                return self.left.find(value)

    def delete_min(self, root):
        if self.left:
            self.size -= 1
            return self.left.delete_min(root)
        else:
            if self.parent is None:
                root.root = self.right
                print(self.right.value)
            else:
                self.parent.left = None
            self.disconnect()
            return self

    def rank(self, value, rank=0):
        if self.value < value:
            rank += 1
            if self.left:
                rank += self.left.size
            if self.right:
                return self.right.rank(value, rank)
        elif self.value == value:
            rank += 1
            if self.left:
                rank += self.left.size
        else:
            if self.left:
                return self.left.rank(value, rank)
        return rank

    def disconnect(self):
        self.parent = None
        self.left = None
        self.right = None
        self.depth = 0
        self.size = 1

    def __str__(self) -> str:
        if self.parent:
            if self == self.parent.right:
                return str(self.value) + "->right%d"%(self.depth)
            if self == self.parent.left:
                return str(self.value) + "->left%d"%(self.depth)
        return str(self.value) + "->root"


class BST():
    def __init__(self) -> None:
        self.root = None
        self.depth = 0

    def insert(self, value):
        node = _BstNode(value)
        if self.root is None:
            self.root = node
        else:
            self.depth = self.root._insert(node, self.depth)
        return node

    def find(self, value)->_BstNode:
        return self.root.find(value)

    def delete_min(self)->_BstNode:
        if self.root is None:
            return None
        return self.root.delete_min(self)

    def rank(self, value)->int:
        if self.root is None:
            return 0
        return self.root.rank(value)

def main():
    bst = BST()

    st = time()
    for i in range(100):
        print(bst.insert(random.randint(
            2, 1000)))
    s = time()
    

    # for a in [49,46,43,79,64,83]:
    #     bst.insert(a)
    # #bst.delete_min()
    # print(bst.find(79).size)
    # print(bst.rank(83),bst.root.size)

    # bst.delete_min()
    # print(bst.find(79).size)
    # print(bst.rank(83),bst.root.size)

    # bst.delete_min()
    # print(bst.find(79).size)
    # print(bst.rank(83),bst.root.size)

    # bst.delete_min()
    # print(bst.find(79).size)
    # print(bst.rank(83),bst.root.size)

    # bst.delete_min()
    # print(bst.find(79).size)
    # print(bst.rank(83),bst.root.size)

    # print(bst.delete_min().value)
    # print(bst.find(79).size)
    # print(bst.rank(83),bst.root.size)


if __name__ == "__main__":
    #test(BSTtype=BST)
    main()
# print(bst.root)
# print(bst.find(19))
