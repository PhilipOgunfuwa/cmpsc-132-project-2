#!/usr/bin/env python3

from DoublyLinkedNode import DoublyLinkedNode
from PolynomialTerm import PolynomialTerm
from DoublyLinkedList import DoublyLinkedList

class Polynomial:
    def __init__(self, size=0):
        #Constructs DoublyLinkedList for Polynomial and its Terms
        self.polynomial = DoublyLinkedList()
        self.size = size

    def findLikeTerm(self, coefficient, variable, degree):
        """Method to find like term in polynomial"""
        self.findLikePolynomialTerm(PolynomialTerm(coefficient, variable, degree))

    def findLikePolynomialTerm(self, keyTerm):
        for term in self.polynomial:
            if term.data.areLikeTerms(keyTerm):
                return term

        return None

    def addTerm(self, coefficient, variable, degree):
        """Method to add term to polynomial"""
        self.addPolynomialTerm(PolynomialTerm(coefficient, variable, degree))

    def addPolynomialTerm(self, newTerm):
        #Polynomial is empty
        if self.polynomial.head is None:
            self.polynomial.append(newTerm)
            return True

        #Add like terms if applicable
        possibleLikeTerm = self.findLikePolynomialTerm(newTerm)
        if possibleLikeTerm is not None:
            possibleLikeTerm.data += newTerm
            return True 

        currentTerm = self.polynomial.head

        #Searching for where to place newTerm depending on its degree or if its a constant
        while currentTerm is not None:

            #Place terms of a higher degree before lower degree terms
            if currentTerm.data.degree < newTerm.degree:
                self.polynomial.insertNodeBeforeNode(DoublyLinkedNode(newTerm), currentTerm)
                return True
            
            #Add constants to the end of the polynomial and keep non constants to the most left
            if currentTerm is self.polynomial.tail:
                if currentTerm.data.isAConstant():
                    self.polynomial.insertNodeBeforeNode(DoubyLinkedNode(newTerm), curentTerm)
                    return True

                else:
                    self.polynomial.insertNodeAfterNode(DoublyLinkedNode(newTerm), currentTerm)
                    return True

            currentTerm = currentTerm.next

        #Failed to add Term for some reason 
        return False



    def __add__(self, right):
        """Overloads the adding operator for Polynomials"""

        #Sum o fthe polynomials
        sumOfPolynomials = Polynomial()

        #Add like terms
        for rightTerm in right.polynomial:
            possibleLikeTerm = self.findLikePolynomialTerm(rightTerm.data)
            if possibleLikeTerm is not None:
                sumOfPolynomials.addPolynomialTerm(possibleLikeTerm.data + rightTerm.data)

        #Add non like terms from right polynomial
        for rightTerm in right.polynomial:
            if not sumOfPolynomials.findLikePolynomialTerm(rightTerm.data):
                sumOfPolynomials.addPolynomialTerm(rightTerm.data)

        #Add non like terms from left polynomial
        for leftTerm in self.polynomial:
            if not sumOfPolynomials.findLikePolynomialTerm(leftTerm.data):
                sumOfPolynomials.addPolynomialTerm(leftTerm.data)

        return sumOfPolynomials

    #See if this should be __repr__
    def __str__(self):
        """Method to give string representation to polynomials"""
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
    test2 = Polynomial()
    test.addTerm(10, "x", 5)
    test.addTerm(10, "x", 2)
    test2.addTerm(10, "y", 3)
    test2.addTerm(10, "x", 2)

    print(test)
    print(test2)
    print(test + test2)
    print(test)
    print(test2)





if __name__ == "__main__":
    main()
