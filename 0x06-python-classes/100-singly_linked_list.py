#!/usr/bin/python3
"""
singly linked list implementation
"""


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the linked list.

    Methods:
        No additional methods are defined in this class.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a node with the given data and optional next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node or None: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node or None): The next node in the linked list.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node or None): The head node of the linked list.

    Methods:
        print_list(): Print the elements of the linked list.
        sorted_insert(value): Insert a value into the linked list while
        maintaining sorted order.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a value into the linked list while maintaining sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node

        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            curr = self.__head
            while (curr.next_node is not None and curr.next_node.data < value):
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """
        Convert the linked list to a string representation.

        Returns:
            str: The string representation of the linked list.
        """
        new_list = []
        if self.__head is None:
            return None
        value = self.__head
        while value is not None:
            new_list.append(str(value.data))
            value = value.next_node
        return ("\n".join(new_list))
