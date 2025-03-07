
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self, root_val=1):
        self.root = TreeNode(val=root_val)

    def generate_random_tree(self):
        nums = iter(range(2, 10))
        self.root.left = TreeNode(next(nums))
        self.root.right = TreeNode(next(nums))
        self.root.left.left = TreeNode(next(nums))
        self.root.left.right = TreeNode(next(nums))
        self.root.right.left = TreeNode(next(nums))
        self.root.right.right = TreeNode(next(nums))

    def printTreeLevelOrderTraversal(self):
        q = [self.root]
        curr_level = 0

        while q:
            curr = q[0]
            print(f"level {curr_level}: ", end="")
            for _ in range(len(q)):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                
                print(curr.val, end=" ")
            print()
            curr_level += 1
        
        return

if __name__ == "__main__":
    tree = BinaryTree()
    tree.generate_random_tree()
    tree.printTreeLevelOrderTraversal()
