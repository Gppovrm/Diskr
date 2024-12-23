class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:  # для игнорирования дубликатов
            root.left = insert(root.left, key)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)


def generate_sequence(n, x):
    a = [1]  # сразу добавлем a_0
    for i in range(1, n):
        new_value = a[i - 1] * (x + 5) % 700
        a.append(new_value)
    return a


def isBinarySearchTree(root):
    def check(v, min_val, max_val):
        if v is None:
            return True
        if v.val <= min_val or v.val >= max_val:
            return False
        return check(v.left, min_val, v.val) and check(v.right, v.val, max_val)

    return check(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    n = int(input("Введите количество чисел (n): "))
    x = 439790 % 31
    # x = int(input("Введите значение x: "))

    sequence = generate_sequence(n, x)
    print("Generated numbers:", sequence)

    root = None
    for num in sequence:
        root = insert(root, num)

    print("In-order BST traversal:")
    inorder_traversal(root)

    print("\nIs the tree a Binary Search Tree?", isBinarySearchTree(root))
