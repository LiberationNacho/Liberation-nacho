import time

size = 700

# Define the list node class
class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value

# Function to insert a value into the list (at the end)
def insert_list(head, value):
    if head is None:
        return ListNode(value)
    current = head
    while current.next is not None:
        current = current.next
    current.next = ListNode(value)
    return head

# Function to search for a value in the list
def search_list(head, target):
    if head is None:
        return False
    if head.value == target:
        return True
    return search_list(head.next, target)

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1

# AVL 트리에 노드 삽입하는 함수
def insert_tree(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_tree(root.left, value)
    elif value > root.value:
        root.right = insert_tree(root.right, value)
    else:
        return root

    # 노드 삽입 후 높이 갱신
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # 균형 확인 후 회전 수행
    balance = get_balance(root)
    if balance > 1:
        if value < root.left.value:
            return rotate_right(root)
        else:
            root.left = rotate_left(root.left)
            return rotate_right(root)
    if balance < -1:
        if value > root.right.value:
            return rotate_left(root)
        else:
            root.right = rotate_right(root.right)
            return rotate_left(root)
    return root

# AVL 트리에서 값 찾는 함수
def search_tree(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    if root.value < target:
        return search_tree(root.right, target)
    return search_tree(root.left, target)

# AVL 트리의 높이 구하는 함수
def get_height(root):
    if root is None:
        return 0
    return root.height

# AVL 트리의 균형을 확인하는 함수
def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)

# 오른쪽으로 회전하는 함수
def rotate_right(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

# 왼쪽으로 회전하는 함수
def rotate_left(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def main():
    # AVL 트리 생성 및 초기화
    tree_root = None
    for i in range(size):
        tree_root = insert_tree(tree_root, i)

    # AVL 트리 검색
    start_time1 = time.time()
    result = search_tree(tree_root, size - 1)
    end_time1 = time.time()
    print(f"AVL Tree execution time: {end_time1 - start_time1:.6f} seconds")

    # Create and initialize the list
    list_head = None
    for i in range(size):
        list_head = insert_list(list_head, i)

    # List search
    start_time2 = time.time()
    result = search_list(list_head, size - 1)
    end_time2 = time.time()
    print(f"List execution time: {end_time2 - start_time2:.6f} seconds")

if __name__ == "__main__":
    main()
