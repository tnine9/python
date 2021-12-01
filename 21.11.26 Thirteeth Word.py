class Counter:
    num1 = 0
    num2 = 0
    operator = ''

    def count(self):
        if self.operator == '+':
            print('%s+%s=%s' % (self.num1, self.num1, self.num1 + self.num1))
        elif self.operator == '-':
            print('%s-%s=%s' % (self.num1, self.num1, self.num1 - self.num1))
        elif self.operator == '*':
            print('%s*%s=%s' % (self.num1, self.num1, self.num1 * self.num1))
        elif self.operator == '/':
            print('%s/%s=%s' % (self.num1, self.num1, self.num1 / self.num1))
        else:
            print('您输入的运算符有错')


num = Counter
num.num1 = int(input('请输入第一个运算数:'))
num.operator = input('请输入运算符:')
num.num2 = int(input('请输入第二个运算数:'))
num().count()
