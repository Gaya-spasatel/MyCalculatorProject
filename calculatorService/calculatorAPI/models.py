class IntegerNumber:
    def __init__(self, value: int):
        self.value = value

class IntegerOperands:
    def __init__(self, firstOpernad: IntegerNumber, secondOperand: IntegerNumber):
        self.firstOperand = firstOpernad
        self.secondOpernad = secondOperand

class SumOfIntegerNumbers:
    def __init__(self, value: IntegerNumber):
        self.sum = value

class DiffOfIntegerNumbers:
    def __init__(self, value: IntegerNumber):
        self.difference = value

class MulOfIntegerNumbers:
    def __init__(self, value: IntegerNumber):
        self.product = value

class DivOfIntegerNumbers:
    def __init__(self, quotient: IntegerNumber, remainder: IntegerNumber):
        self.quotient = quotient
        self.remainder = remainder

class ErrorMessage:
    def __init__(self, type, message):
        self.type = type
        self.message = message
