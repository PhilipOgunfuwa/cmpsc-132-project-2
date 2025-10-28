#!/usr/bin/env python3

from DoublyLinkedNode import DoublyLinkedNode
from DoublyLinkedListIterator import DoublyLinkedListIterator

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


    def __iter__(self):
        """Overloaded iterator operator that goes to DoublyLinkedListIterator to allow for looping the linked list"""
        return DoublyLinkedListIterator(self.head)


    def __contains__(self, data):
        """Overloads contains operator so you can check to see if data is within the linked list"""
        for node in self:
            if node.data == data:
                return True

        return False
