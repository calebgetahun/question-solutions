class Traversals:
    def preorder(root):
        def preTraverse(root, traversal):
            if not root:
                return
            traversal.append(root.val)
            preTraverse(root.left, traversal)
            preTraverse(root.right, traversal)
        traversal = []
        preTraverse(root, traversal)

        return traversal

    def inorder(root):
        def inTraverse(root, traversal):
            if not root:
                return
            inTraverse(root.left, traversal)
            traversal.append(root.val)
            inTraverse(root.right, traversal)
        traversal = []
        inTraverse(root, traversal)

        return traversal

    def postorder(root):
        def postTraverse(root, traversal):
            if not root:
                return
            postTraverse(root.left, traversal)
            postTraverse(root.right, traversal)
            traversal.append(root.val)
        traversal = []
        postTraverse(root, traversal)

        return traversal
