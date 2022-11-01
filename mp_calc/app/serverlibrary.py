import re


def merge(array, p, q, r, key=None):
    if key == None:
        def key(x): return x
    arr1 = array[p:q]
    arr2 = array[q:r+1]
    i1, i2 = 0, 0
    len1, len2 = len(arr1), len(arr2)
    for i in range(p, r+1):
        if i1 == len1:
            array[i:r+1] = arr2[i2:]
            break
        if i2 == len2:
            array[i:r+1] = arr1[i1:]
            break
        if key(arr1[i1]) <= key(arr2[i2]):
            array[i] = arr1[i1]
            i1 += 1
        else:
            array[i] = arr2[i2]
            i2 += 1

def mergesort_recursive(array, p, r, key):
    if p == r:
        return
    if p + 1 == r:
        merge(array, p, r, r, key)
        return
    mergesort_recursive(array, p, (p + r)//2, key)
    mergesort_recursive(array, (p + r)//2 + 1, r, key)
    merge(array, p, (p+r)//2 + 1, r, key)


def mergesort(array, byfunc=lambda x: x):
    if len(array) == 0:
      return
    mergesort_recursive(array, 0, len(array) - 1, byfunc)

class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items == []:
            return None
        else:
            return self.__items.pop()

    def peek(self):
        if self.__items == []:
            return None
        return self.__items[-1]

    @property
    def is_empty(self):
        if self.__items == []:
            return True
        return False

    @property
    def size(self):
        return len(self.__items)


class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    operators = "+-*/()"
    operands = "0123456789"

    # Regex patterns used for syntax checking
    EMPTY_BRACKETS = re.compile(r"\(\)")
    ADJACENT_OPERATORS = re.compile(r"[+\-*/][+\-*/]")
    OPERATOR_ADJ_BRACKET = re.compile(r"\([+\-*/]|[+\-*/]\)")
    INITIAL_OPERATOR = re.compile(r"^[+\-*/\)]")
    OPERAND_ADJ_BRACKET = re.compile(r"\d\(|\)\d")
    ADJACENT_OPERANDS = re.compile(r"\d\s+\d")

    def __init__(self, string=""):
        self.expression = string

    @property
    def expression(self):
        return self.expr

    @expression.setter
    def expression(self, new_expr: str):
        if not isinstance(new_expr, str):
            raise TypeError("Expression should be a string.")
        if re.search(EvaluateExpression.ADJACENT_OPERANDS, new_expr):
            raise SyntaxError("Numbers cannot be separated by a space.")
        if new_expr == "":
            raise SyntaxError("Expression cannot be empty.")
        new_expr = "".join(new_expr.split())
        bracket_counter = 0
        for char in new_expr:
            if char not in self.valid_char:
                self.expr = ""
                raise SyntaxError(
                    f"Invalid character found in expression: {char}")
            elif char == "(":
                bracket_counter += 1
            elif char == ")":
                bracket_counter -= 1
                if bracket_counter < 0:
                    raise SyntaxError("Unmatched close bracket in expression.")
        if bracket_counter > 0:
            raise SyntaxError("Unmatched open bracket in expression.")
        if re.search(EvaluateExpression.EMPTY_BRACKETS, new_expr):
            raise SyntaxError("Empty brackets '()' found in expression.")
        if re.search(EvaluateExpression.ADJACENT_OPERATORS, new_expr):
            raise SyntaxError("Adjacent operators found in expression.")
        if re.search(EvaluateExpression.OPERATOR_ADJ_BRACKET, new_expr):
            raise SyntaxError(
                "Invalid operator placement beside brackets found in expression.")
        if re.search(EvaluateExpression.INITIAL_OPERATOR, new_expr):
            raise SyntaxError("First token of expression cannot be operator.")
        if re.search(EvaluateExpression.OPERAND_ADJ_BRACKET, new_expr):
            raise SyntaxError("Operand cannot be just outside a bracket.")

        self.expr = new_expr

    def insert_space(self):
        expr = self.expression
        new_expr = []
        for char in expr:
            if char in self.operators:
                new_expr.append(" " + char + " ")
            else:
                new_expr.append(char)
        return "".join(new_expr)

    def process_operator(self, operand_stack: Stack, operator_stack: Stack):
        """Process the next operator in the operator stack, and push the result to the operand stack.

        Does not check for empty stack!"""
        oprt = operator_stack.pop()
        opr2 = operand_stack.pop()
        opr1 = operand_stack.pop()
        if oprt == "+":
            result = opr1 + opr2
        elif oprt == "-":
            result = opr1 - opr2
        elif oprt == "*":
            result = opr1 * opr2
        elif oprt == "/":
            result = opr1 // opr2
        operand_stack.push(result)

    def evaluate(self):
        """Evaluates the expression stored in self.expr.
        Does not check for expression syntax!"""
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        for token in tokens:
            if re.match(r"^\d+$", token):
                operand_stack.push(int(token))
            elif token in "-+":
                while not operator_stack.is_empty and operator_stack.peek() not in "()":
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)
            elif token in "*/":
                while not operator_stack.is_empty and operator_stack.peek() in "*/":
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)
            elif token == "(":
                operator_stack.push(token)
            elif token == ")":
                while operator_stack.peek() != "(" and not operator_stack.is_empty:
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()
            else:
                raise SyntaxError(
                    f"Invalid syntax passed to evaluate! Invalid tokens: {token} in {tokens}")
        while not operator_stack.is_empty:
            self.process_operator(operand_stack, operator_stack)
        return operand_stack.peek()


def get_smallest_three(challenge):
    records = challenge.records
    times = [r for r in records]
    mergesort(times, lambda x: x.elapsed_time)
    return times[:3]
