class Counter():
    num1 = 0
    num2 = 0
    __operator = ''

    def setoperator(self, operation):
        if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '^':
            print('您输入的运算符号不正确')
        else:
            self.__operator = operation

    def count(self):
        if self.__operator == '+':
            print
