#!/usr/bin/env python3

from DoublyLinkedNode import DoublyLinkedNode

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, data):
        """Method to append non nodes to linked list"""
        newNode = DoublyLinkedNode(data)
        self.appendNode(newNode)

    def appendNode(self, newNode):
        """Method to append nodes to linked list"""
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def prepend(self, data):
        """Method to prepend non nodes to linked list"""
        newNode = DoublyLinkedNode(data)
        self.prependNode(newNode)


    def prependNode(self, newNode):
        """Method to prepend nodes to linked list"""
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    def insertNodeAfterNode(self, newNode, predecessorNode):
        """Method to insert a Node after another Node"""
        if predecessorNode is self.tail:
            self.appendNode(newNode)

        else:
            newNode.next = predecessorNode.next
            predecessorNode.next.previous = newNode
            newNode.previous = predecessorNode
            predecessorNode.next = newNode

    def insertNodeBeforeNode(self, newNode, successorNode):
        """Method to insert a Node after another Node"""
        if successorNode is self.head:
            self.prependNode(newNode)

        else:
            newNode.previous = successorNode.previous
            successorNode.previous.next = newNode
            newNode.next = successorNode
            successorNode.previous = newNode

    def removeNode(self, node):
        """Method to remove node"""

        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None

        elif node is self.head:
            node.next.previous = None
            self.head = node.next

        elif node is self.tail:
            node.previous.next = None
            self.tail = node.previous

        else:
            node.previous.next = node.next
            node.next.previous = node.previous

