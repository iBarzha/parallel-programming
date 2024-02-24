import time
import random
import matplotlib.pyplot as plt


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
    sizes = [1000, 10000, 100000, 1000000, 10000000]
    build_times = []
    search_times = []
    unique_times_tree = []
    unique_times_comparison = []

    for size in sizes:
        array = [random.randint(0, size * 10) for _ in range(size)]

        start_time = time.time()
        tree = build_tree_from_array(array)
        build_times.append(time.time() - start_time)

        start_time = time.time()
        missing_elements = search_missing_elements(tree, array)
        search_times.append(time.time() - start_time)

        start_time = time.time()
        unique_elements_tree = count_unique_elements_with_tree(array)
        unique_times_tree.append(time.time() - start_time)

        start_time = time.time()
        unique_elements_comparison = count_unique_elements_with_comparison(array)
        unique_times_comparison.append(time.time() - start_time)

    # Побудова графіків
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.plot(sizes, build_times, marker='o')
    plt.title('Build Time')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')

    plt.subplot(2, 2, 2)
    plt.plot(sizes, search_times, marker='o')
    plt.title('Search Time')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')

    plt.subplot(2, 2, 3)
    plt.plot(sizes, unique_times_tree, marker='o')
    plt.title('Unique Elements Time (Tree)')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')

    plt.subplot(2, 2, 4)
    plt.plot(sizes, unique_times_comparison, marker='o')
    plt.title('Unique Elements Time (Comparison)')
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')

    plt.tight_layout()
    plt.show()