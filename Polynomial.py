#!/usr/bin/env python3

from DoublyLinkedNode import DoublyLinkedNode
from DoublyLinkedList import DoublyLinkedList

class Polynomial:
    def __init__(self, variable):
        #Constructs DoublyLinkedList for Polynomial and its Terms
        self.polynomial = DoublyLinkedList()
        self.size = 0
        self.variable = variable

    def addTerm(self, coefficient, degree):
        """Method to add term to polynomial"""

        #Important to note that the first index will ALWAYS be the coefficient and the second index
        #will ALWAYS be the degree of the term
        if self.polynomial.head is None:
            self.polynomial.append([coefficient, degree])
            self.size += 1
            return

        currentTerm = self.polynomial.head

        while currentTerm is not None:
            if currentTerm.data[1] == degree:
                currentTerm.data[0] += coefficient

                if currentTerm.data[0] == 0:
                    self.polynomial.removeNode(currentTerm)
                    self.size -= 1

                break

            if currentTerm.data[1] < degree:
                self.polynomial.insertNodeBeforeNode(DoublyLinkedNode([coefficient, degree]), currentTerm)
                self.size += 1
                break

            if currentTerm is self.polynomial.tail:
                self.polynomial.insertNodeAfterNode(DoublyLinkedNode([coefficient, degree]), currentTerm)
                self.size += 1
                break

            currentTerm = currentTerm.next

    def __repr__(self):

        superscript_escapes = [
            '\u2070', '\u00b9', '\u00b2', '\u00b3',
            '\u2074', '\u2075', '\u2076', '\u2077',
            '\u2078', '\u2079'
        ]
        
        polynomial_string = ""
    
        currentTerm = self.polynomial.head
        firstTerm = True
        exponent = ""

        while currentTerm is not None:
            for digit in str(currentTerm.data[1]):
                exponent += superscript_escapes[int(digit)]

            if firstTerm:
                polynomial_string += f"{currentTerm.data[0]}{self.variable}{exponent}"
                firstTerm = False
            else:
                polynomial_string += f" + {currentTerm.data[0]}{self.variable}{exponent}"
                
            exponent = ""

            currentTerm = currentTerm.next

        return polynomial_string

    def __add__(self, right):
        """Method that overloads the addition operator so you can add polynomials"""

        if self.variable != right.variable:
            raise ValueError("Cant add polynomials of different variables")

        sumOfPolynomials = Polynomial(self.variable)

        currentLeftTerm = self.polynomial.head
        currentRightTerm = right.polynomial.head

        while currentLeftTerm is not None:
            sumOfPolynomials.addTerm(currentLeftTerm.data[0], currentLeftTerm.data[1])
            currentLeftTerm = currentLeftTerm.next

        while currentRightTerm is not None:
            sumOfPolynomials.addTerm(currentRightTerm.data[0], currentRightTerm.data[1])
            currentRightTerm = currentRightTerm.next

        return sumOfPolynomials

    def size(self):
        return self.size



def main():
    poly = Polynomial("x")

    poly2 = Polynomial("x")

    poly2.addTerm(3, 5)
    poly.addTerm(3, 4)

    poly.addTerm(2, 5) 
    poly.addTerm(1, 3)

    print(poly)
    print(poly2)

    print(poly + poly2)

    print(poly.size)
    print(poly2.size)
    print((poly + poly2).size)

    poly2.addTerm(-2, 5)
    print(poly2)
    poly2.addTerm(-1, 5)
    print(poly2)
    print(poly2.size)

if __name__ == "__main__":
    main()
