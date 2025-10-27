#!/usr/bin/env python3

class DoublyLinkedNode:
    '''Data for doubly linked node'''
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous
