def binary_search(list_, x):
    low = 0
    high = len(list_)

    while low < high:
        mid = (low+high) // 2
        if x < list_[mid]:
            high = mid
        else:
            low = mid+1
    return low

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        left = f'[{self.left.value}]' if self.left else '[]'
        right = f'[{self.right.value}]' if self.right else '[]'
        return f'{left} <- {self.value} -> {right}'

class BinarySearchTree:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        if self.nodes:
            parent, direction = self.find_parent(value)
            if direction == 'left':
                parent.left = node
            else:
                parent.right = node
        self.nodes.append(node)

    def find_parent(self, value):
        node = self.nodes[0]
        while node:
            p = node
            if p.value == value:
                raise ValueError
            if p.value > value:
                direction = 'left'
                node = p.left
            else:
                direction = 'right'
                node = p.right
        return p, direction

if __name__=="__main__":
    btree = BinarySearchTree()
    for v in [10, 20, 12, 4, 3, 9, 30]:
        btree.add_node(v)

    for node in btree.nodes:
        print(node)


