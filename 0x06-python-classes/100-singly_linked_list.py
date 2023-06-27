#!/usr/bin/python3
'''Define a Singly linked list'''


class Node:
    '''Create the Node object'''
    def __init__(self, data, next_node=None):
        '''Instantiate the Node object

        Args:
            data (int): Node's value
            next_node (Node): The next element of the singly
            linked list
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Get the data value of the Node object'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Set the data value of the Node object

        Args:
            value (int): The new value of the Node's data
            value
        '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        '''Get the Node object's next_node value'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Set the new value of the Node object's next_node value

        Args:
            value (Node): The next element of the linked list
            or None if the current object is the last
        '''
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    '''Create the SinglyLinkedList object'''
    def __init__(self):
        '''Instantiate the SinglyLinkedList object'''
        self.__head = None

    def sorted_insert(self, value):
        '''Insert a new element to the SinglyLinkedList objet

        Args:
            value (Node): The new element to add to the
            SinglyLinkedList object
        '''
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            save = self.__head
            while (save.next_node is not None and
                    save.next_node.data < value):
                save = save.next_node
            new.next_node = save.next_node
            save.next_node = new

    def __str__(self):
        '''Define the printed message at the SinglyLinkedList
        object creation'''
        objs = []
        save = self.__head
        while save is not None:
            objs.append(str(save.data))
            save = save.next_node
        return ('\n'.join(objs))
