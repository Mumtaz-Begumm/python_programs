class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def dfs_inorder(root):
    if root==None:
        return
    dfs_inorder(root.left)
    print(root.data)
    dfs_inorder(root.right)
def dfs_preorder(root):
    if root==None:
        return
    print(root.data)
    dfs_preorder(root.left)
    dfs_preorder(root.right)
def dfs_postorder(root):
    if root==None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.data)  
def BFS(root):
    q=[root]
    if root==None:
        return
    while q:
        a=q.pop(0)
        print(a.data)
        if a.left:
            q.append(a.left)
        if a.right:
            q.append(a.right)      
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print("inorder traversal")
dfs_inorder(root)
print("preorder traversal")
dfs_preorder(root)
print("postorder traversal")
dfs_postorder(root)
print("BFS taversal:")
BFS(root)
