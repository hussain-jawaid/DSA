class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left is None:
                self.left = BinaryTree(data)
            else:
                self.left.add_child(data)
        else:
            if self.right is None:
                self.right = BinaryTree(data)
            else:
                self.right.add_child(data)

def building_binary_tree(elements):
    root = BinaryTree(10)
    for i in range(len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [7, 11, 16, 8, 9, 14, 16, 18]
    root = building_binary_tree(numbers)
    pass