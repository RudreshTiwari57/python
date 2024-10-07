class Leaf:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def append(self,data):
        if self.root is None:
            self.root = Leaf(data)
        else:
            self.append_tree(self.root,data)
    def append_tree(self,node,data):

        if data < node.data:
            if node.left is None:
                node.left = Leaf(data)

            else:
                self.append_tree(node.left,data)
        else:
            if node.right is None:
                node.right = Leaf(data)
            else:
                self.append_tree(node.right,data)

    def delete(self,data):
        self.delete_and_rearrange(self.root,data)
    def delete_and_rearrange(self,node,data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete_and_rearrange(node.left,data)
        elif data > node.data:
            node.right = self.delete_and_rearrange(node.right,data)

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.find_min(node.right)
            node.data = temp.data
            node.right = self.delete_and_rearrange(node.right,temp.data)
        return node
    def find_min(self,node):
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp

    def in_order_traversal(self, node):
        """Performs in-order traversal of the tree."""
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)



tree = Tree()
tree.append(5)
tree.append(3)
tree.append(7)
tree.append(2)
tree.append(4)
tree.append(6)
tree.append(8)
tree.in_order_traversal(tree.root)
print()
tree.delete(5)
tree.in_order_traversal(tree.root)

