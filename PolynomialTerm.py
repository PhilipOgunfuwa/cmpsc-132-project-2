#!/usr/bin/env python3

class PolynomialTerm:
    '''Class to hold Polynomial Terms'''
    def __init__(self, coefficient: float, variable: str, degree: int):
        self.coefficient = coefficient
        self.variable = variable
        self.degree = degree
        self.degree_superscript = ""
        self.degree_superscript = self.getDegreeSuperScript()

    def simplify(self):
        """Method to simplify Polynomial term if its degree is 0"""
        if self.degree == 0:
            return PolynomialTerm(self.coefficient, "", 0)

    def __add__(self, right):
        """Overloaded addition operator that allows for polynomial terms to be added"""
        if self.areLikeTerms(right):
            return PolynomialTerm(self.coefficient + right.coefficient, self.variable, self.degree)

    def __sub__(self, right):
        """Overloaded subtraction operator that allows for polynomial terms to be subtracted"""
        if self.areLikeTerms(right):
            return PolynomialTerm(self.coefficient - right.coefficient, self.variable, self.degree)

    def __eq__(self, right):
        """Overloaded equality operator the allows for polynomial terms to be checked for equality"""
        if self.coefficient != right.coefficient:
            return False

        if self.variable != right.variable:
            return False

        if self.degree != right.degree:
            return False

        return True

    
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




