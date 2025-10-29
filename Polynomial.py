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
        isNegative = False
        exponent = ""

        while currentTerm is not None:
            if currentTerm.data[1] not in [0, 1]:
                
                if currentTerm.data[1] < 0:
                    exponent = "-"
                    isNegative = True
                else:
                    isNegative = False

                for digit in str(currentTerm.data[1]):
                    if isNegative:
                        exponent = "-"
                        isNegative = False
                        continue

                    exponent += superscript_escapes[int(digit)]
            else:
                exponent = ""

            if currentTerm.data[1] == 0:
                variable = ""
            else:
                variable = self.variable
            
            
            if firstTerm:
                polynomial_string += f"{currentTerm.data[0]}{variable}{exponent}"
                firstTerm = False
            else:
                polynomial_string += f" + {currentTerm.data[0]}{variable}{exponent}"
                
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

def parseStringForPolynomial(string, variable):
    polynomial = Polynomial(variable)
    split_string = string.split()

    for term in split_string:
        term = term.split(f"{variable}^")
        term

        if len(term) > 2:
            raise Exception("Too many \"{variable}^\" in terms")
        
        #Getting degree of term
        if len(term) == 1:
            #If coefficient's last item is variable then no degree given
            if term[0][-1] == variable:
                term_degree = 1
            #If coefficient last item is not a variable then their is no variable (constant)
            else:
                term_degree = 0

        #term degree is just the second term
        else:
            term_degree = int(term[1])


        if term_degree == 1:
            if len(term) == 1:
                term_coefficient = term[0][:-1]
            else:
                term_coefficent = term[0]

        else:
            term_coefficient = term[0]

        if term_coefficient == "":
            term_coefficient = 1

        term_coefficient = int(term_coefficient)

        polynomial.addTerm(term_coefficient, term_degree)

    return polynomial

            


def main():

    user_input = ""
    while user_input != "q":
        
        print("Type in polynomial 1: ", end="")
        poly1 = parseStringForPolynomial(input(">> "), "x")

        print("Type in polynomial 2:", end="")
        poly2 = parseStringForPolynomial(input(">> "), "x")
   
        print(poly1)
        print(poly1.size)
        print(poly2)
        print(poly2.size)
        print(poly1 + poly2)
        print((poly1 + poly2).size)


if __name__ == "__main__":
    main()
