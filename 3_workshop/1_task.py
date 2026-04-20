class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None

    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)

    return root

def level_order(root):
    if not root:
        return []

    result = []
    queue = [root]

    while len(queue) > 0:
        next_queue = []
        current_level = []

        for node in queue:
            current_level.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

        result.append(current_level)
        queue = next_queue

    return result

tree = build_tree([9, 16, 8, None, None, 6, 11])
result = level_order(tree)

print(result)
