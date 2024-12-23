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


# Функция для генерации последовательности
def generate_sequence(n, x):
    a = [x]
    for i in range(1, n):
        a.append(a[i - 1] * (x + 5) % 700)
    return a


# Построение BST из последовательности
def build_bst(sequence):
    root = TreeNode(sequence[0])
    for num in sequence[1:]:
        insert(root, num)
    return root


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
    print("Сгенерированная последовательность:", sequence)

    root = build_bst(sequence)

    print("Инфиксный обход (in-order traversal) построенного BST:")
    inorder_traversal(root)

    print("\nIs the tree a Binary Search Tree?", isBinarySearchTree(root))
