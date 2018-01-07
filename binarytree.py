# encoding: utf-8

# Defination of binary tree
import random
from collections import deque
from drawtree import draw_level_order

NONE_NODE = '#'


class BinTNode:
    """二叉树节点"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '{}'.format(self.val)



def build_a_random_bintree(node_nums=10, min_val=0, max_val=100):
    """构建一个随机的二叉树"""
    root = None
    values = random.sample(range(min_val, max_val), node_nums)
    if values:
        root = BinTNode(val=values.pop())
        building_nodes = [root]
    while values:
        val = values.pop()
        node = BinTNode(val=val)
        t = random.choice(building_nodes)
        go_left = random.randint(0, 1)
        if go_left:
            if not t.left:
                t.left = node
                building_nodes.append(node)
        else:
            if not t.right:
                t.right = node
                building_nodes.append(node)
        if t.left and t.right:
            building_nodes.remove(t)
    return root

def preorder_recursive(root):
    """pre-order traversal by recursive method"""
    if not root:
        return
    yield root
    for x in preorder_recursive(root.left):
        yield x
    for x in preorder_recursive(root.right):
        yield x

def preoder_iterative(root):
    """pre-order traversal by iterative method"""
    stack = [root]
    while stack:
        root = stack.pop()
        if root:
            yield root
            stack.append(root.right)
            stack.append(root.left)

def inorder_recursive(root):
    """in-order traversal by recursive method"""
    if root:
        for x in inorder_recursive(root.left):
            yield x
        yield root
        for x in inorder_recursive(root.right):
            yield x

def inorder_iterative(root):
    """in-order traversal by iterative method"""
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            yield root
            root = root.right


def postorder_recursive(root):
    """post-order traversal by recursive"""
    if root:
        for x in postorder_recursive(root.left):
            yield x
        for x in postorder_recursive(root.right):
            yield x
        yield root

def postorder_iterative(root):
    """post-order traversal by iterative method"""
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            if root.left:
                root = root.left
            else:
                root = root.right
        root = stack.pop()
        yield root
        if stack and stack[-1].left == root:
            root = stack[-1].right
        else:
            root = None


def level_iterative(root):
    """level order traversal by iterative method"""
    q = deque()
    q.append(root)
    while q:
        root = q.popleft()
        if root:
            q.append(root.left)
            q.append(root.right)
            yield root
            #  result.append(root)
        else:
            yield NONE_NODE
            #result.append(NONE_NODE)
    #return result

def format_for_drawtree(node_list):
    result_str = ','.join([str(item) for item in node_list])
    return '{' + result_str + '}'

if __name__ == '__main__':
    t = build_a_random_bintree()

    level_order_list = list(level_iterative(t))
    print('the tree is:')
    draw_level_order(format_for_drawtree(level_order_list))
    print('level order node value list is:{}'.format(level_order_list))

    pre_order_recursive_list = list(preorder_recursive(t))
    print('pre order recursive node value list is:{}'.format(pre_order_recursive_list))

    pre_order_iterative_list = list(preoder_iterative(t))
    print('pre order iterative node value list is:{}'.format(pre_order_iterative_list))

    in_order_recursive_list = list(inorder_recursive(t))
    print('in order recursive node value list is:{}'.format(in_order_recursive_list))

    in_order_iterative_list = list(inorder_iterative(t))
    print('in order iterative node value list is:{}'.format(in_order_iterative_list))

    post_order_recursive_list = list(postorder_recursive(t))
    print('post order recursive node value list is:{}'.format(post_order_recursive_list))

    post_order_iterative_list = list(postorder_iterative(t))
    print('post order iterative node value list is:{}'.format(post_order_iterative_list))
