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

    def __str__(self):
        level = self.get_level()
        spaces = ' ' * level * 3
        prefix = spaces + "|__" if level != 0 else ''
        print(prefix + self.data)
        for child in self.children:
            child.__str__()
        return ''

def build_tree():
    # root node
    root = TreeNode('Electronics')

    # children of root node
    laptops = TreeNode('Laptops')
    cell_phones = TreeNode('Cell Phones')
    tv = TreeNode('Televisions')

    # make a relation between children and root node
    root.add_child(laptops)
    root.add_child(cell_phones)
    root.add_child(tv)

    laptops.add_child(TreeNode('Macbook'))
    laptops.add_child(TreeNode('Microsoft Surface'))
    laptops.add_child(TreeNode('Think Pad'))

    cell_phones.add_child(TreeNode('iPhone'))
    cell_phones.add_child(TreeNode('Google Pixel'))
    cell_phones.add_child(TreeNode('ViVo'))

    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    return root

if __name__ == '__main__':
    root = build_tree()
    print(root)
    pass