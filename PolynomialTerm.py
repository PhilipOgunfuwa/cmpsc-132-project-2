#!/usr/bin/env python3

class PolynomialTerm:
    '''Class to hold Polynomial Terms'''
    def __init__(self, coefficient: float, variable: str, degree: int):

        if len(variable) > 1:
            raise ExceptionType("Only single variables are accepted")

        self.coefficient = coefficient
        self.variable = variable
        self.degree = degree
        self.degree_superscript = ""
        self.degree_superscript = self.getDegreeSuperScript()

    def __add__(self, right):
        """Overloaded addition operator that allows for polynomial terms to be added"""
        if self.areLikeTerms(right):
            return PolynomialTerm(self.coefficient + right.coefficient, self.variable, self.degree)

    def __sub__(self, right):
        """Overloaded subtraction operator that allows for polynomial terms to be subtracted"""
        if self.areLikeTerms(right):
            return PolynomialTerm(self.coefficient - right.coefficient, self.variable, self.degree)

    def __mul__(self, right):
        """Overloaded the multiplication operator allows for polynomial terms to be multiplied"""
        if self.variable != right.variable:
            return "Failed"

        return PolynomialTerm(self.coefficient * right.coefficient, self.variable, self.degree + right.degree)

    def __truediv__(self, right):
        """Overloads the true division operator and allows for polynomial terms to be dividied"""
        if self.variable != right.variable:
            return "Failed"

        return PolynomialTerm(self.coefficient * right.coefficient, self.variable, self.degree - right.degree)

    def __eq__(self, right):
        """Overloaded equality operator the allows for polynomial terms to be checked for equality"""
        if self.coefficient != right.coefficient:
            return False

        if self.variable != right.variable and not (self.isAConstant() and right.isAConstant()):
            return False

        if self.degree != right.degree:
            return False

        return True

    def setVariableEqualTo(self, value):
        return self.coefficient * (value ** self.degree)

    def integrate(self):
        return PolynomialTerm(self.coefficient / (self.degree + 1), self.variable, self.degree + 1)

    def differentiate(self):
        return PolynomialTerm(self.coefficient * self.degree, self.variable, self.degree - 1)

    
    def isAConstant(self):
        """Method that checks if term is a constant or not"""
        if self.degree != 0:
            return False

        return True

    def areLikeTerms(self, right):
        """Method that checks if another polynomial term is a like term or not"""
        if self.isAConstant() and right.isAConstant():
            return True

        if self.degree == right.degree and self.variable == right.variable:
            return True

        return False

    def getDegreeSuperScript(self):
        """Method that gets the superscript for the degree (exponent) by using the digits to go to its index of superscript"""
        superscript_escapes = [
            '\u2070', '\u00b9', '\u00b2', '\u00b3',
            '\u2074', '\u2075', '\u2076', '\u2077',
            '\u2078', '\u2079'
        ]

        degree_superscript = ""
        copy_of_degree = str(abs(self.degree))

        for digit in copy_of_degree:
            degree_superscript += superscript_escapes[int(digit)]

        if self.degree < 0:
            degree_superscript = "\u207b" + degree_superscript

        return degree_superscript

    def __str__(self):
        """Method that gives string representation to Polynomial terms"""
        if self.degree == 0:
            return f"{self.coefficient}"

        if self.degree == 1:
            return f"{self.coefficient}{self.variable}"

        return f"{self.coefficient}{self.variable}{self.degree_superscript}"




