import random
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursively(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self._insert_recursively(node.right, value)
            else:
                node.right = Node(value)

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

def build_tree_from_array(array):
    tree = BinaryTree()
    for num in array:
        tree.insert(num)
    return tree

def search_missing_elements(tree, array):
    missing_elements = []
    for num in array:
        if not tree.search(num):
            missing_elements.append(num)
    return missing_elements

def count_unique_elements_with_tree(array):
    tree = build_tree_from_array(array)
    unique_elements = 0
    # Here you can implement a traversal algorithm to count unique elements
    return unique_elements

def count_unique_elements_with_comparison(array):
    unique_elements = len(set(array))
    return unique_elements

if __name__ == "__main__":
    sizes = [1000, 10000, 100000, 1000000, 10000000]  # Reduced the size to 10 million
    for size in sizes:
        array = [random.randint(0, size * 10) for _ in range(size)]

        start_time = time.time()
        tree = build_tree_from_array(array)
        build_time = time.time() - start_time

        start_time = time.time()
        missing_elements = search_missing_elements(tree, array)
        search_time = time.time() - start_time

        start_time = time.time()
        unique_elements_tree = count_unique_elements_with_tree(array)
        unique_time_tree = time.time() - start_time

        start_time = time.time()
        unique_elements_comparison = count_unique_elements_with_comparison(array)
        unique_time_comparison = time.time() - start_time

        print(f"Array Size: {size}")
        print("Build Time:", build_time)
        print("Search Time:", search_time)
        print("Unique Elements (Tree):", unique_elements_tree)
        print("Time for Unique Elements (Tree):", unique_time_tree)
        print("Unique Elements (Comparison):", unique_elements_comparison)
        print("Time for Unique Elements (Comparison):", unique_time_comparison)
        print("----------------------------------")
