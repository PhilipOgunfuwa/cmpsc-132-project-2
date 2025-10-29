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

    def getSize(self):
        return self.size

def parseStringForPolynomial(string):
    polynomial = Polynomial("")
    
    split_string = string.split()
    for i in range(len(split_string)):
        split_string[i] = split_string[i].split("^")

    for term in split_string:
        if len(term) == 1 and term[0][-1].isalpha():
            degree = 0
            
        elif len(term) < 2:
            raise Exception("Too many \"^\"")
        else:
            if not term[1].isdigit():
                raise Exception("Invalid character in degree/exponent")

            degree = int(term[1])

        coefficient = 0
        FirstTerm = True

        for character in term[0]:
            if character.isalpha():
                if FirstTerm:
                    coefficient = 1
                variable = character
                break
            elif character.isdigit():
                coefficient = int(character) + (coefficient * 10)
                if FirstTerm:
                    FirstTerm = False
            else:
                raise Exception("Invalid character in Polynomial")
        polynomial.variable = variable 
        polynomial.addTerm(coefficient, degree)


    return polynomial
            


        

            


def main():

    user_input = ""
    while user_input != "q":
        
        print("Type in polynomial 1: ", end="")
        poly1 = parseStringForPolynomial(input(">> "))

        print("Type in polynomial 2:", end="")
        poly2 = parseStringForPolynomial(input(">> "))
   
        print(poly1)
        print(poly2)
        print(poly1 + poly2)


if __name__ == "__main__":
    main()
