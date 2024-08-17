class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def decimal_to_binary_tree(decimal):
        if decimal == 00:
            return BinaryTreeNode(0)
        root = BinaryTreeNode(decimal % 2)
        decimal = decimal // 2
        current = root
        while decimal > 0:
            new_node = BinaryTreeNode(decimal % 2)
            current.left = new_node
            current = new_node
            decimal = decimal // 2
        return root
    
    def print_binary_tree(root):
        if root:
            print_binary_tree(root.left)
            print(root.data, end='')
            