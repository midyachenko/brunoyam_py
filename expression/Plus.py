import abc

from expression.Const import Const
from expression.Expression import Expression

class BinaryOp(Expression):
    def __init__(self, left, right):
        super().__init__(left, right)

    def calc(self):
        left_result = self.left.calc()
        right_result= self.right.calc()

        return  self.operation(left_result, right_result)

    @abc.abstractmethod
    def operation(self, a, b):
        pass

class Plus(BinaryOp):
    def __init__(self, left=None, right=None):
        super().__init__(left, right)

    def operation(self, a, b):
        return a+b


class Minus(Expression):
    def __init__(self, left=None, right=None):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() - self.right.calc()


class Mult(Expression):
    def __init__(self, left=None, right=None):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() * self.right.calc()


class Div(Expression):
    def __init__(self, left=None, right=None):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() / self.right.calc()


def str_to_tree(expr):
    """
    :type expr: str
    """
    expr.strip()
    result_class=Const
    index = expr.find('+')
    if index != -1:

        result_class = Plus
    else:
        index = expr.find('-')
        if index != -1:

            result_class = Minus
        else:
            index = expr.find('*')
            if index != -1:

                result_class = Mult
            else:
                index = expr.find('/')
                if index != -1:
                    result_class = Div

    if index != -1:
        left = str_to_tree(expr[:index])
        right = str_to_tree(expr[index + 1:])
        return result_class(left,right)
    return Const(int(expr))

print(str_to_tree('6/2 +3 *4 +300/10').calc())
print(eval('6/2 +3 *4 +300/10'))
six = Const(6)
two = Const(2)
three = Const(3)
four = Const(4)

div = Div(six, two)
mul = Mult(three, four)

plus = Plus(div, mul)

print(plus.calc())

