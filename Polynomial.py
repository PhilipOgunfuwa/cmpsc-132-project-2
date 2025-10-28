#!/usr/bin/env python3

from DoublyLinkedNode import DoublyLinkedNode
from PolynomialTerm import PolynomialTerm
from DoublyLinkedList import DoublyLinkedList

class Polynomial:
    def __init__(self, size=0):
        self.polynomial = DoublyLinkedList()
        self.size = size

    def addTerm(self, coefficient, variable, degree):
        self.addPolynomialTerm(PolynomialTerm(coefficient, variable, degree))

    def addPolynomialTerm(self, term):
        currentTerm = self.polynomial.head

        if self.polynomial.head is None:
            self.polynomial.append(term)
            return

        while currentTerm is not None:
            if currentTerm.data.areLikeTerms(term):
               currentTerm.data += term
               return

            if currentTerm.data.degree < term.degree and not term.isAConstant():
                self.polynomial.insertNodeBeforeNode(DoublyLinkedNode(term), currentTerm)
                return

            if currentTerm is self.polynomial.tail:
                if currentTerm.data.isAConstant():
                    self.polynomial.insertNodeBeforeNode(DoublyLinkedNode(term), currentTerm)
                else:
                    self.polynomial.append(term)

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
                continue

            string_representation += f" + {term.data}"

        return string_representation


def main():
    test = Polynomial()
    test.addTerm(10, "x", 5)
    test.addTerm(10, "x", 2)
    test.addTerm(10, "x", 3)
    test.addTerm(20, "x", 2)
    test.addTerm(10, "x", 3)
    test.addTerm(5, "", 1)
    test.addTerm(5, "", 1)
    test.addTerm(5, "x", 1)
    test.addTerm(5, "xy", 2)
    test.addTerm(5, "", 5)
    test.addTerm(5, "", 2)
    test.addTerm(2, "", -1)
    test.addTerm(.5, "z", -10)
    test.addTerm(.2, "z", -10)


    print(PolynomialTerm(5, "", 1))
    print(test)

    currentNode = test.polynomial.head




if __name__ == "__main__":
    main()
