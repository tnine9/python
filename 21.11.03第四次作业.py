dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
# 1、请循环遍历出所有的key
for a in dict.keys():
    print(a)
# 2、请循环遍历出所有的value
for a in dict.values():
    print(a)
# 3、请在字典中增加一个键值对,"k4":"v4"
dict['k4'] = 'v4'
print(dict)

Friuts = {
    '苹果': 12.3,
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8}

# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# print(Friuts.get(input('请输入要查询的水果名'), '没有此水果'))
# 请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 1
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 1
    }
}

d = 0
Friuts_money = list(Friuts.values())
for name_ in info.keys():
    c = 0
    for a in Friuts.keys():
        b = info[name_]['fruits'].get(a, -1)
        if b == -1:
            continue
        else:
            c = c + b * Friuts_money[d]
            d += 1
    info[name_]['money'] = c
print(info)

# 编写一个函数，传入一个列表，并统计每个数字出现的次数，返回字典数据。
a = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8]


def countnum(a):
    sep = list(set(a))
    dict1 = dict.fromkeys(sep, 0)
    x = 0
    while x < len(sep):
        dict1[sep[x]] = a.count(sep[x])
        x = x + 1
    return dict1


def countnum1(a):
    dict1 = {}
    for i in a:
        if str(i) not in dict1.keys():
            dict1[str(i)] = 1
        else:
            dict1[str(i)] += 1
    return dict1


dict1 = countnum1(a)
print(dict1)
