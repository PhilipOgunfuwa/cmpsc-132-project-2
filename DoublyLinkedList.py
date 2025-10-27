#!/usr/bin/env python3

from DoublyLinkedNode import DoublyLinkedNode
from DoublyLinkedListIterator import DoublyLinkedListIterator

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, data):
        newNode = DoublyLinkedNode(data)
        self.appendNode(newNode)

    def appendNode(self, newNode):

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def prepend(self, data):
        newNode = DoublyLinkedNode(data)
        self.prependNode(newNode)


    def prependNode(self, newNode):

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    def insertNodeAfterNode(self, newNode, predecessorNode):
        if predecessorNode is self.tail:
            predecessorNode.next = newNode
            newNode.previous = predecessorNode
            self.tail = newNode

        else:
            newNode.next = predecessorNode.next
            predecessorNode.next.previous = newNode
            newNode.previous = predecessorNode
            predecessorNode.next = newNode

    def insertNodeBeforeNode(self, newNode, successorNode):
        if successorNode is self.head:
            successorNode.previous = newNode
            newNode.next = successorNode
            self.head = newNode

        else:
            newNode.previous = successorNode.previous
            successorNode.previous.next = newNode
            newNode.next = successorNode
            successorNode.previous = newNode

        return "N/A"

    def __iter__(self):
        return DoublyLinkedListIterator(self.head)
