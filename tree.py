class TreeNode:
    def __init__(self,value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root=TreeNode(10000000000000)

def add_value(new_value, current_node): #left
    if current_node.value > new_value:
        if current_node.left is not None:
            add_value(new_value, current_node.left)
        else:
            current_node.left = TreeNode(new_value)

    else: #right
        if current_node.right is not None:
            add_value(new_value, current_node.right)
        else:
            current_node.left = TreeNode(new_value)

def find(value, current_node):
    print(current_node.value)
    if current_node.value == value:
        return  True
    if current_node.value < value:
        if current_node.left is not None:
            return find(value, current_node.left)
        else:
            return False
    if current_node.value > value:
        if current_node.right is not None:
            return find(value, current_node.right)
        else:
            return False



def print_tree(current_node):
    print(current_node.value)
    if current_node.left is not None:
        print_tree(current_node.left)
    if current_node.right is not None:
        print_tree(current_node.rigth)


add_value(10,root)
add_value(5,root)
add_value(12,root)
add_value(8,root)
add_value(6,root)
add_value(15,root)

print_tree(root)


