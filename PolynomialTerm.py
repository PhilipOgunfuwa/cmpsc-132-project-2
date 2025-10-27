#!/usr/bin/env python3

class PolynomialTerm:
    '''Class to hold Polynomial Terms'''
    def __init__(self, coefficient: float, variable: str, degree: int):
        self.coefficient = coefficient
        self.variable = variable
        self.degree = degree
        self.degree_superscript = ""
        self.degree_superscript = self.getDegreeSuperScript()

    def __add__(self, right):
        if self.variable != right.variable:
            return "Failed"

        if self.degree != right.degree:
            return "Failed"

        return PolynomialTerm(self.coefficient + right.coefficient, self.variable, self.degree)

    def __sub__(self, right):
        if self.variable != right.variable:
            return "Failed"

        if self.degree != right.degree:
            return "Failed"

        return PolynomialTerm(self.coefficient - right.coefficient, self.variable, self.degree)

    def getDegreeSuperScript(self):
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
            degree_superscript = "\u207b" + self.degree_superscript

        return degree_superscript

    def __str__(self):
        return f"{self.coefficient}{self.variable}{self.degree_superscript}"
