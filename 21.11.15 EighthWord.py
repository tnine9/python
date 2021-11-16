import xlrd

f = xlrd.open_workbook(filename=r"D:\测试开发\python\day8\2020年每个月的销售情况.xlsx", encoding_override=True)

# 全年的销售总额
# 每种衣服的销售（件数）占比
# 每种衣服的月销售（件数）占比
# 每种衣服的销售额占比
# 最畅销的衣服是那种
# 每个季度最畅销的衣服
# 全年销量最低的衣服
a, gross_sales, sum_age_money, sum, c = 0, 0, 0, 0, 0
total_sales_volume = {}
sum_age = {}
for a in range(0, 12):
    sheet = f.sheet_by_index(a)  # 读取每张表格
    # 读取数据
    rows = sheet.nrows  # 获取多少行
    cols = sheet.ncols  # 获取多少列

    for i in range(1, rows):
        data = sheet.row_values(i)  # 保存每天的销售数据
        sum_age_money = sum_age_money + data[4] * data[2]  # 计算全年的销售总额
        # 计算各种类销售总量
        if data[1] not in total_sales_volume:
            total_sales_volume.setdefault(data[1], data[4])
            sum_age.setdefault(data[1], data[4]*data[2])
        else:
            total_sales_volume[data[1]] = total_sales_volume[data[1]] + data[4]
            sum_age[data[1]]=sum_age[data[1]]+data[4]*data[2]
        # 计算全部的销售总量
        sum = sum + data[4]

b = 0
print('年销售总额为:', round(sum_age_money, 2))
for i in total_sales_volume:
    total_sales_volume[i] = (round(total_sales_volume[i] / sum * 100, 2))
    sum_age[i]=(round(sum_age[i] / sum_age_money * 100, 2))
    b += 1
print('销售数量占比为', total_sales_volume)
print('销售额占比为',sum_age)
print('销量最低的为',max(total_sales_volume))
print('最畅销的为',min(total_sales_volume))