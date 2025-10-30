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
                        exponent = "\u207b"
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
            term_coefficient = "1"

        if term_coefficient[0] == "-":
            term_coefficient = -1

        term_coefficient = int(term_coefficient)

        polynomial.addTerm(term_coefficient, term_degree)

    return polynomial

            


def main():

    print("\nThe following program does the following:")
    print("1.) Takes user input for two polynomials")
    print("2.) Orders polynomials rom the highest degree to the lowest degree")
    print("3.) Outputs the sum of the polynomials\n")
    print("Your expected to type in polynomials like: 10x^2 9x 10\n")
    print("The program will read 10x^2 as 10 to the second degree")
    print("The program will read 9x has 9 to the 1st degree")
    print("The program will read 10 as 10 the the 0th degree\n")
    print("If you want to put in an exponent be sure to do x^(exponent)")
    print("10^2 is not acceptable as user input\n")
    print("If you want something to be of the 1st degree you can either implicity")
    print("Do this by writing out 10x or explicitly do it with 10x^1. This principle works for 0th degree\n")
    print("You can type in as many terms as you want just be sure to put a space between each term!\n")
    print("starting...\n")
    user_input = ""

    while user_input != "q":
        user_input = input("Enter polynomial 1 to add >> ")
        polynomial1 = parseStringForPolynomial(user_input, "x")
        user_input = input("Enter polynomial 2 to add >> ")
        polynomial2 = parseStringForPolynomial(user_input, "x")
        print(f"here is polynomial 1: {polynomial1}")
        print(f"here is polynomial 2: {polynomial2}")
        print(f"here is their sum of polynomial 1 and 2: {polynomial1 + polynomial2}")
        user_input = input("Would you like to quit? (q to quit) >> ")


if __name__ == "__main__":
    main()
