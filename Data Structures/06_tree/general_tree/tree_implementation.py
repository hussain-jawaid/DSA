class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        level = self.get_level()
        spaces = ' ' * level*3
        prefix = spaces + '|__' if level != 0 else ''
        print(prefix, self.data)
        for child in self.children:
            child.print_tree()

def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    macbook = TreeNode('Macbook')
    laptop.add_child(macbook)
    laptop.add_child(TreeNode('Microsoft Surface'))
    laptop.add_child(TreeNode('Think pad'))

    macbook.add_child(TreeNode('Macbook Pro'))

    cell_phone = TreeNode('Cell Phone')
    cell_phone.add_child(TreeNode('iPhone'))
    cell_phone.add_child(TreeNode('Google Pixel'))
    cell_phone.add_child(TreeNode('ViVo'))

    tv = TreeNode('Television')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)

    return root.print_tree()

if __name__ == '__main__':
    build_product_tree()