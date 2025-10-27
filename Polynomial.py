#!/usr/bin/env python3

from DoublyLinkedNode import DoublyLinkedNode
from PolynomialTerm import PolynomialTerm
from DoublyLinkedList import DoublyLinkedList

class Polynomial:
    def __init__(self):
        self.polynomial = DoublyLinkedList()
        #
    def addTerm(self, coefficient, variable, degree):
        self.addPolynomialTerm(PolynomialTerm(coefficient, variable, degree))

    def addPolynomialTerm(self, term):
        currentTerm = self.polynomial.head

        if self.polynomial.head is None:
            self.polynomial.append(term)
            return

        while currentTerm is not None:
            if currentTerm.data.degree == term.degree:
                if currentTerm.data.variable == term.variable:
                    currentTerm.data += term
                    return
                #FIXME
                #elif (currentTerm is self.polynomial.tail) or (currentTerm.next.data.variable != term.variable):
                    #self.polynomial.insertNodeAfterNode(term, currentTerm)

            elif currentTerm.data.degree < term.degree:
                self.polynomial.insertNodeBeforeNode(DoublyLinkedNode(term), currentTerm)
                return


            
            currentTerm = currentTerm.next

    #See if this should be __repr__
    def __str__(self):
        string_representation = ""
        first_term = True
        for term in self.polynomial:
            if first_term:
                string_representation += f"{term.data}"
                first_term = False

            string_representation += f" + {term.data}"

        return string_representation


def main():
    test = Polynomial()
    test.addTerm(10, "x", 2)
    test.addTerm(10, "x", 3)
    test.addTerm(20, "x", 2)
    test.addTerm(5, "y", 2)
    test.addTerm(5, "x", 10)
    test.addTerm(12, "z", 5)
    test.addTerm(5, "xy", 10)
    test.addTerm(5, "z", 5)
    test.addTerm(3, "", 1)
    print(test)

    currentNode = test.polynomial.head




if __name__ == "__main__":
    main()
