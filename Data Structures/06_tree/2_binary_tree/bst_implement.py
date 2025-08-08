class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key == node.data:
            return False

        if key < node.data:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.data:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.data:
            return True
        if key < current_node.data:
            return self._search(current_node.left, key)
        elif key > current_node.data:
            return self._search(current_node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.right
            # Node with two children: find inorder successor
            temp_val = self._min_value_node(node.right)
            node.data = temp_val.data
            node.right = self._delete(node.right, temp_val.data)
        return node

    def find_min(self):
        try:
            min_node = self._min_value_node(self.root)
            if min_node: return min_node.data
        except Exception:
            raise Exception('tree not initialize')

    def find_max(self):
        try:
            max_node = self._max_value_node(self.root)
            if max_node: return max_node.data
        except Exception:
            raise Exception('tree not initialize')

    def _max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def is_empty(self):
        return True if self.root is None else False

def build_bst(elements):
    bst = BinarySearchTree()
    for i in elements:
        bst.insert(i)
    return bst

if __name__ == '__main__':
    numbers = [10, 8, 11, 12, 14, 17, 9, 3]
    bst = build_bst(numbers)
    pass