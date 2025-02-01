# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serializeLevelOrder(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        s = []
        q = [root]

        while q:
            curr = q.pop(0)
            if curr:
                s.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                s.append("None")
        return ",".join(s)
    
    def deserializeLevelOrder(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # if not data:
        #     return None
        if not data:
            return None
        data_list = data.split(",")
        
        root = TreeNode(int(data_list[0]))

        index = 1
        q = [root]

        while q:
            curr = q.pop(0)

            if index <= len(data_list) and data_list[index] != "None":
                left = TreeNode(int(data_list[index]))
                curr.left = left
                q.append(left)
            
            index += 1
            if index <= len(data_list) and data_list[index] != "None":
                right = TreeNode(int(data_list[index]))
                curr.right = right
                q.append(right)
            
            index += 1

        return root
    
def printLevelOrderTraversal(root):
    q = [root]
    traversal = []

    while q:
        curr = q.pop(0)
        traversal.append(curr.val)

        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)
    
    return traversal
    

if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, None, TreeNode(3, TreeNode(4), TreeNode(5))))
    ser = Codec()
    des = Codec()
    
    serialized_deserialized = des.deserializeLevelOrder(ser.serializeLevelOrder(tree))
    print(printLevelOrderTraversal(tree) == printLevelOrderTraversal(serialized_deserialized))

# TC: O(N)
# SC: O(N)