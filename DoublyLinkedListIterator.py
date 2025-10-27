#!/usr/bin/env python3

class DoublyLinkedListIterator:
    def __init__(self, currentNode):
        self.currentNode = currentNode

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentNode is None:
            raise StopIteration
        else:
            copyCurrentNode = self.currentNode
            self.currentNode = self.currentNode.next
            return copyCurrentNode
