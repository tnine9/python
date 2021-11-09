# 随机生成1000个整数;
# 数字范围[20,100];
# 输出所有不同的数字及其每个数字重复的次数,
# 有能力的话升序排序打印所有数字{“数字”:”次数”}
import random  # 引用random模块

num = [random.randint(20, 100) for i in range(1000)]  # 随机出20至100之间的随机数
numdict = {}
for a in range(20, 101):
    b = num.count(a)
    numdict[str(a)] = b
print(numdict)

# 输出商品列表，用户输入序号，显示用户选中的商品
# 商品列表：
goods = [{"name": "电脑  ", "price": 1999},

         {"name": "鼠标  ", "price": 10},

         {"name": "显示器", "price": 120},

         {"name": "内存  ", "price": 230}, ]
# 1：页面显示 序号 + 商品名称 + 商品价格
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入
# 4：用户输入Q或者q，退出程序
for s in range(len(goods)):
    print(s + 1, ' ', goods[s]['name'], ' ', goods[s]['price'])
while True:
    try:
        a = input('请输入商品序号')
        if a == 'q' or a == 'Q':
            print('退出系统')
            break
        elif int(a) <= 0:
            raise OverflowError
        else:
            print(a, ' ', goods[int(a) - 1]['name'], ' ', goods[int(a) - 1]['price'])
    except:
        print('请输入正确的序号')
        continue
