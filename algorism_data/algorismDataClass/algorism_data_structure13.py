# 이진 탐색 트리의 정의
# 소스코드와 책에있는 코드는 내용이 다르다 --> 책의 내용만 보기
def search_min_bst(n):
    while n!=None and n.left!=None:
        n=n.right
    return n


def delete_bst(root, key):
    if root == None:
        return root
    if key<root.key:
        root.left=delete_bst(root.left, key)
    elif key> root.key:
        root.right=delete_bst(root.right, key)
    else:
        #case1
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left

        succ=search_min_bst(root.right)
        root.key=succ.key
        root.value=succ.value
        root.right=delete_bst(root.right, succ.key)
    return root


tree=[35, 22, 68, 7, 26, None, 99, 3, 12, 22, 30]
delete_bst()