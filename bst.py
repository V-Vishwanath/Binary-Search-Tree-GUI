class BinarySearchTree:
    """Creates a Binary Search Tree"""

    class Node:
        """Node for holding data of the Binary Search tree"""

        def __init__(self, data):
            self.key = data
            self.left = self.right = self.parent = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a node into the Binary Search Tree

        :param:
        key (int) : the key value of the node

        :return:
        boolean : boolean value representing the success of the operation
        """

        self.root, status = self._insert(self.root, key)
        return status

    def _insert(self, root, key):
        if root is None: return self.Node(key), True
        status = True
        if root.key > key:
            root.left, status = self._insert(root.left, key)
            root.left.parent = root
        elif root.key < key:
            root.right, status = self._insert(root.right, key)
            root.right.parent = root
        else:
            return root, False
        return root, status

    def search(self, key):
        """Searches for a node in the Binary Search Tree

        :param:
        key (int): the key value of the node

        :return:
        self.Node : returns the address of the node if found, else returns None
        """

        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None: return None
        if root.key > key:
            return self._search(root.left, key)
        elif root.key < key:
            return self._search(root.right, key)
        return root

    def delete(self, key):
        """Deletes a node from the Binary Search Tree

        :param:
        key (int) : the key value of the node

        :return:
        boolean : boolean value representing the success of the operation
        """

        self.root, status = self._delete(self.root, key)
        return status

    def _delete(self, root, key):
        if root is None: return root, False
        status = None
        if root.key > key:
            root.left, status = self._delete(root.left, key)
        elif root.key < key:
            root.right, status = self._delete(root.right, key)
        else:
            if root.left is None: return root.right, True
            if root.right is None: return root.left, True
            root.key = self._min(root.right)
            root.right, status = self._delete(root.right, root.key)
        return root, status

    def _min(self, root):
        if root is None: return None
        while root.left: root = root.left
        return root.key

    def _max(self, root):
        if root is None: return None
        while root.right: root = root.right
        return root.key

    def height(self):
        """Returns the height of the Binary Search Tree
        :return:
        int : height of the binary search tree
        """

        return self._height(self.root)

    def _height(self, root):
        if root is None: return 0
        return max(self._height(root.left), self._height(root.right)) + 1

    def level(self, key):
        """Returns the level of a node in the Binary Search Tree

        :param:
        key (int) : the key value of the node

        :return:
        int : level of the node in the Binary Search Tree
        """

        return self._level(self.root, key)

    def _level(self, root, key, level=1):
        if root is None: return 0
        if root.key == key: return level
        l = self._level(root.left, key, level + 1)
        if l: return l
        return self._level(root.right, key, level + 1)

    def predecessor(self, key):
        """Returns the In-Order Predecessor of the node in the Binary Search Tree

        :param:
        key (int) : the key value of the node

        :return:
        self.Node : the address of the in-order predecessor to the node if it exists, else returns None
        """

        return self._predecessor(self.root, key)

    def _predecessor(self, root, key):
        if root is None: return None
        predecessor = None
        while root.key != key:
            if root.key > key:
                root = root.left
            else:
                predecessor = root.key
                root = root.right
        if root and root.left: predecessor = self._max(root.left)
        return predecessor

    def successor(self, key):
        """Returns the In-Order Successor of the node in the Binary Search Tree

        :param:
        key (int) : the key value of the node

        :return:
        self.Node : the address of the in-order successor to the node if it exists, else returns None
        """

        return self._successor(self.root, key)

    def _successor(self, root, key):
        if root is None: return None
        successor = None
        while root.key != key:
            if root.key <= key:
                root = root.right
            else:
                successor = root.key
                root = root.left
        if root and root.right: successor = self._min(root.right)
        return successor
