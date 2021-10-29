city = ['北京', '广东', '上海', '石家庄', '海口', ]
print(city)
city_GDP = [36710.36, 35427.10, 29863.23, 29667.39, 27665.36, 27650.45, 27620.38, 25369.20]
s, s1 = 0, 0
while s < 8:
    s1 = s1 + city_GDP[s]
    s += 1
print('总值为', s1)
print('平均值为', s1 / 8)

a = [1, 5, 21, 30, 15, 9, 30, 24]
a1, a2 = 0, 0
while a1 < 8:
    if a[a1] % 5 == 0:
        a2 = a2 + a[a1]
    a1 += 1
print(a2)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b1, b2 = 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, ]
while b1 < 9:
    b2[b1] = b[-b1 - 1]
    b1 += 1
print(b2)
b2 = list(reversed(b))
print(b2)

c = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
c1 = c.count(int(input('请输入数字')))
print('出现了%s次' % c1)

#    姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]]
names.insert(4, ["刘备", "45", "男", "220", "alibaba", 500, "30"])
d1, d2, d3, d5, d7 = 0, 0, 0, 0, 0
d4 = input('请输入要统计的性别')
d6 = input('请输入要统计的部门')
while d1 < len(names):
    d2 = d2 + names[d1][5]
    d3 = d3 + int(names[d1][1])
    d5 = d5 + names[d1][3].count(d4)
    d7 = d7 + names[d1][6].count(d6)
    d1 += 1
print('平均薪资为', d2 / 4)
print('平均年龄为', d3 / 4)
print('%s性有%d人' % (d4, d5))
print('%s部门有%d人' % (d6, d7))

e1 = 0
mogic = [['罗恩', 23, 35, 44],
         ['哈利', 60, 77, 68, 88, 90],
         ['赫敏', 97, 99, 89, 91, 95, 90],
         ['马尔福 ', 100, 85, 90]]
while e1 < len(mogic):
    e2, e3 = 0, 0
    while e2 < len(mogic[e1]):
        if e2 < 1:
            print(mogic[e1][e2], end=':')
        else:
            e3 = e3 + mogic[e1][e2]
        e2 += 1
    print(e3)
    e1 += 1

num = int(input('请输入一个数：'))
while num != 0:
    print(num % 10)
    num = num // 10

f = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
f1=0
for f1 in range(len(f)):
    for f2 in range(0,len(f)-1):
        if f[f2]>f[f2+1]:
            f[f2],f[f2+1]=f[f2+1],f[f2]
print(f)