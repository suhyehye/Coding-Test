import sys
sys.setrecursionlimit(10**6)
class TreeNode:
    def __init__(self, val):
        self.x = val[0]
        self.left = None
        self.right = None
        self.idx = val[2]
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
        return self.root is not None
    
    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val[0] < node.x:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node
    
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.idx, end = ' ')
            self._inorder(node.right)
    
    def preorder(self, node):
        def _preorder(node):
            if node:
                res.append(node.idx)
                _preorder(node.left)
                _preorder(node.right)
        res = []
        _preorder(node)
        return res

    def postorder(self, node):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                res.append(node.idx)
        res = []
        _postorder(node)
        return res
    
def solution(nodeinfo):
    nodeinfo = [[x[0], x[1], idx+1] for idx, x in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x:(x[1], -x[0]), reverse=True)
    
    BTree = BinarySearchTree()
    for node in nodeinfo:
        BTree.insert(node)
    
    answer = []
    answer.append(BTree.preorder(BTree.root))
    answer.append(BTree.postorder(BTree.root))
    return answer