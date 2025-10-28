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
            if term.areLikeTerms(keyTerm):
                return term

        return None

    def subtractTerm(self, coefficient, variable, degree):
        """Method to subtract term from polynomial"""
        self.subtractPolynomialTerm(PolynomialTerm(coefficient, variable, degree))

    def subtractPolynomialTerm(self, newTerm):
        copy_of_newTerm = PolynomialTerm(-newTerm.coefficient, newTerm.variable, newTerm.degree)
        self.addPolynomialTerm(copy_of_newTerm)

    def addTerm(self, coefficient, variable, degree):
        """Method to add term to polynomial"""
        self.addPolynomialTerm(PolynomialTerm(coefficient, variable, degree))

    def addPolynomialTerm(self, newTerm):
        
        #Don't add because term is 0
        if newTerm.coefficient == 0:
            return True

        #Polynomial is empty
        if self.polynomial.head is None:
            self.polynomial.append(newTerm)
            return True

        #Add like terms if applicable
        possibleLikeTerm = self.findLikePolynomialTerm(newTerm)
        if possibleLikeTerm is not None:
            possibleLikeTerm += newTerm
            return True

        #Add constant terms
        if newTerm.isAConstant():
            if self.polynomial.tail.data.isAConstant():
                self.polynomial.tail.data += newTerm
                return True
            else:
                self.polynomial.append(newTerm)
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
                self.polynomial.insertNodeAfterNode(DoublyLinkedNode(newTerm), currentTerm)
                return True


            currentTerm = currentTerm.next

        #Failed to add Term for some reason 
        return False

    def indefiniteIntegral(self):
        integralOfPolynomial = Polynomial()
        for term in self.polynomial:
            integralOfPolynomial.addPolynomialTerm(term.integrate())

        return integralOfPolynomial

    def printIndefiniteIntegral(self):
        integralOfPolynomial = self.indefiniteIntegral()

        return f"{integralOfPolynomial} + C"

    def definiteIntegral(self, lower_bound, upper_bound):
        integralOfPolynomial_lower = self.indefiniteIntegral()
        integralOfPolynomial_upper = self.indefiniteIntegral()

        return integralOfPolynomial_upper
    
    def derivative(self):
        derivativeOfPolynomial = Polynomial()

        for term in self.polynomial:
            derivativeOfPolynomial.addPolynomialTerm(term.differentiate())

        return derivativeOfPolynomial

    def __sub__(self, right):
        """Overloads the subtraction operator for Polynomials"""
        
        #Difference of the polynomials
        differenceOfPolynomials = Polynomial()

        #Subtract left terms
        for leftTerm in self.polynomial:
            differenceOfPolynomials.subtractPolynomialTerm(leftTerm)

        for rightTerm in right.polynomial:
            differenceOfPolynomials.subtractPolynomialTerm(rightTerm)

        return differenceOfPolynomials

    def __add__(self, right):
        """Overloads the adding operator for Polynomials"""

        #Sum o fthe polynomials
        sumOfPolynomials = Polynomial()

        #Add left terms
        for leftTerm in self.polynomial:
            sumOfPolynomials.addPolynomialTerm(leftTerm)

        #Add right terms
        for rightTerm in right.polynomial:
            sumOfPolynomials.addPolynomialTerm(rightTerm)

        return sumOfPolynomials

    #See if this should be __repr__
    def __str__(self):
        """Method to give string representation to polynomials"""
        string_representation = ""
        first_term = True
        for term in self.polynomial:
            if first_term:
                string_representation += f"{term}"
                first_term = False
                continue

            string_representation += f" + {term}"

        return string_representation


def main():
    test = Polynomial()
    test2 = Polynomial()
    test.addTerm(10, "x", 5)
    test.addTerm(10, "x", 2)
    test2.addTerm(10, "y", 3)
    test2.addTerm(10, "x", 2)
    test2.addTerm(10, "", 0)
    test3 = Polynomial()
    test3.addTerm(5, "x", 3)
    test3.addTerm(5, "x", 0)

    print(test3 - test)
    print(test3.derivative())
    print(test3)
    print(test)






if __name__ == "__main__":
    main()
