# <editor-fold desc="猜字游戏">
import random  # 引用random模块

z = 0
while 1:  # 循环一次证明重新开始了一次游戏
    randint_num = random.randint(0, 100)  # 随机出0至100之间的随机数
    min_, max_, integral = 0, 100, 10  # 定义最小数、最大数、积分
    while 1:  # 循环一次证明输入了一次
        z += 1
        try:  # 异常处理，下面是可能会发生异常的代码
            a = input('请输入你预测的数字')  # 用a保存输入的字符串
            if a == 'q' or a == 'Q':  # 判断a是否为q
                print('游戏退出')
                integral = 0  # 积分清零
                break  # 退出小循环
            num = int(a)  # 将a转换为数字
            integral = integral - 1  # 积分减一
        except ValueError:  # 异常处理，发生ValueError异常后运行以下代码
            print('请输入正确的数字')
            break  # 退出小循环
        else:  # 异常处理，不发生异常运行以下的代码
            if num > 100 or num < 0:  # 判断是否大于100或者小于0
                print('请输入0至100之间的数字', ',第', z, '次', ',积分为', integral)
            elif num == randint_num:  # 判断是否猜对
                print('猜对了,重新来')
                break  # 退出小循环
            elif num < randint_num:  # 判断是否猜小了
                print(num, '到', max_, ',第', z, '次', ',积分为', integral)
                if min_ < num:  # 如果min_小，则把此数值赋给min_
                    min_ = num
            elif num > randint_num:  # 判断是否猜大了
                print(min_, '到', num, ',第', z, '次', ',积分为', integral)
                if max_ > num:  # 如果max_大，则把此数值赋给max_
                    max_ = num
            if integral <= 0:  # 如果积分为0则运行以下代码
                print('你输了')
                break  # 退出小循环
    if integral <= 0:  # 如果积分为0则运行以下代码
        break  # 退出大循环
# </editor-fold>

# <editor-fold desc="取值求和">
a, b, max_, sum_ = 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0
while a < 10:
    b[a] = int(input('请输入第%s个数' % (a + 1)))
    a = a + 1
while a > 0:
    sum_ = sum_ + b[a - 1]
    if max_ < b[a - 1]:
        max_ = b[a - 1]
    a = a - 1
print('最大值为', max_)
print('和为', sum_)
print('平均值为', sum_ / 10)
# </editor-fold

# <editor-fold desc="随机数">
# import random
randint_num = random.randint(50, 100)
print(randint_num)
# </editor-fold>

# <editor-fold desc="判断三角形">
c, d = 0, [0, 0, 0]
while c < 3:
    d[c] = int(input('请输入第%s条边' % (c + 1)))
    c = c + 1
if d[0] <= 0 or d[1] <= 0 or d[2] <= 0:
    print('不能形成三角形')
elif d[0] + d[1] <= d[2] or d[0] + d[2] <= d[1] or d[2] + d[1] <= d[0]:
    print('不能形成三角形')
elif d[0] == d[1] == d[2]:
    print('形成等边三角形')
elif d[0] == d[1] or d[1] == d[2] or d[0] == d[2]:
    print('形成等腰三角形')
elif d[0] ^ 2 + d[1] ^ 2 == d[2] ^ 2 or d[0] ^ 2 + d[2] ^ 2 == d[2] ^ 2 or d[2] ^ 2 + d[1] ^ 2 == d[0] ^ 2:
    print('形成直角三角形')
else:
    print('形成普通三角形')
# </editor-fold>

# <editor-fold desc="登录界面">
e = 0
while e < 3:
    root = input('请输入用户名')
    admin = input('请输入密码')
    if root == 'root' and admin == 'admin':
        print('登录成功')
        break
    else:
        print('输入错误，登录失败')
        e += 1
    if e == 3:
        print('账户锁定')
        break
# </editor-fold>

# <editor-fold desc="打印三角">
j = 8
while j > 0:
    for i in range(1, j):
        print(' ' * j, " *" * i)
        j -= 1
# </editor-fold>

# <editor-fold desc="乘法表">
l = 1
while l < 10:
    m = 1
    while m <= l:
        print(l, '*', m, '=', l * m, end=' ')
        m += 1
    l += 1
    print('')
# </editor-fold>

# <editor-fold desc="倒序乘法表">
n, w = 9, 9
while n > 0:
    o = 1
    while o <= w:
        print(n, '*', o, '=', n * o, end=' ')
        o += 1
    n -= 1
    w -= 1
    print('')
# </editor-fold>

# <editor-fold desc="青蛙爬井">
x, y = 0, 0
while x <= 20:
    x = x + 3
    y = y + 1
    if x >= 20:
        print('青蛙出来了')
        print(y)
        break
    else:
        x = x - 2
# </editor-fold>

# <editor-fold desc="阶乘">
product, A = 1, 1
factorial = int(input('请输入要计算阶乘的数字'))
while A <= factorial:
    product = product * A
    A += 1
print(product)
# </editor-fold>