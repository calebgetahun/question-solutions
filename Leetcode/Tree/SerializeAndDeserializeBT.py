# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class CodecRecursively:
    def serializeRec(self, root) -> str:
        #basically a preorder traversal
        def dfs(node, res):
            if not node:
                res.append("None")
                return
            
            res.append(str(node.val))
            dfs(node.left, res)
            dfs(node.right, res)

        result = []
        dfs(root, result)
        return ",".join(result)            

    def deserializeRec(self, data) -> TreeNode:
        data_split = data.split(",")

        def dfs(index):
            if index >= len(data_split) or data_split[index] == "None":
                return None, index
            
            root = TreeNode(int(data_split[index]))

            left_node, new_index = dfs(index+1)
            root.left = left_node

            right_node, new_index = dfs(new_index+1)
            root.right = right_node

            return root, new_index
        
        root, _ = dfs(0)

        return root

class CodecIteratively:

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
    tree_2 = TreeNode(1, TreeNode(2, None, TreeNode(3, TreeNode(4), TreeNode(5))))
    ser_iter = CodecIteratively()
    des_iter = CodecIteratively()

    ser_rec = CodecRecursively()
    des_rec = CodecRecursively()
    
    serialized_deserialized_iter = des_iter.deserializeLevelOrder(ser_iter.serializeLevelOrder(tree))
    serialized_deserialized_rec = des_rec.deserializeRec(ser_rec.serializeRec(tree_2))

    print(printLevelOrderTraversal(tree) == printLevelOrderTraversal(serialized_deserialized_iter))
    print(printLevelOrderTraversal(tree) == printLevelOrderTraversal(serialized_deserialized_rec))

# TC: O(N)
# SC: O(N)