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
total_sales_volume, sum_age, month, variety = {}, {}, {}, {}
sheet_num = len(f.sheets())
for a in range(0, 12):
    day = {}
    sheet = f.sheet_by_index(a)

    # 读取数据
    rows = sheet.nrows  # 获取多少行
    cols = sheet.ncols  # 获取多少列

    for i in range(1, rows):
        n = sheet.row_values(i)
        day[n[0]] = n[1:]
        month[i] = day
        if n[1] not in variety:
            variety.setdefault(n[1], None)
month_money = {}
for a in range(0, 12):
    s = 0
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
            sum_age.setdefault(data[1], data[4] * data[2])
        else:
            total_sales_volume[data[1]] = total_sales_volume[data[1]] + data[4]
            sum_age[data[1]] = sum_age[data[1]] + data[4] * data[2]
        # 计算全部的销售总量
        sum = sum + data[4]
var_dict = {}
var_dict2 = {}
for x in range(sheet_num):
    sheet_num_x = f.sheet_by_index(x)
    var_len = sheet_num_x.nrows
    for y in range(1, var_len):
        var_list = sheet_num_x.row_values(y)
        if var_list[1] not in var_dict:
            var_dict[var_list[1]] = int(var_list[2]) * int(var_list[4])
        else:
            var_dict[var_list[1]] += int(var_list[2]) * int(var_list[4])
        if var_list[1] not in var_dict2:
            var_dict2[var_list[1]] = int(var_list[4])
        else:
            var_dict2[var_list[1]] += int(var_list[4])


def month_var(sheet_month, month_len):
    month_dict = {}
    for i in range(1, month_len):
        month_list = sheet_month.row_values(i)
        if month_list[1] not in month_dict:
            month_dict[month_list[1]] = int(month_list[4])
        else:
            month_dict[month_list[1]] += int(month_list[4])
    return month_dict


seasons_dict = {}
spring = [2, 3, 4]
summer = [5, 6, 7]
fall = [8, 9, 10]
winter = [11, 12, 1]


def four_seasons(seasons):
    for i in seasons:
        seasons_num_i = f.sheet_by_index(i - 1)
        rows_seasons = seasons_num_i.nrows
        for j in range(1, rows_seasons):
            data_seasons = seasons_num_i.row_values(j)
            if data_seasons[1] not in seasons_dict:
                seasons_dict[data_seasons[1]] = int(data_seasons[4])
            else:
                seasons_dict[data_seasons[1]] += int(data_seasons[4])

    key_list = list(var_dict2.keys())
    value_list = list(var_dict2.values())
    max_var = max(value_list)
    k = value_list.index(max_var)
    return key_list[k]


b = 0
print('年销售总额为:', round(sum_age_money, 2))
for i in total_sales_volume:
    total_sales_volume[i] = (round(total_sales_volume[i] / sum * 100, 2))
    sum_age[i] = (round(sum_age[i] / sum_age_money * 100, 2))
    b += 1
print('销售数量占比为', total_sales_volume)
month = 1

for n in range(sheet_num):
    sheet_num_n = f.sheet_by_index(n)
    month_len = sheet_num_n.nrows
    month_dict = month_var(sheet_num_n, month_len)
    month_sum = 0
    for m in month_dict:
        month_sum += month_dict[m]
    for n in month_dict:
        print('%s月%s的销售件数占比为%.2f%%' % (month, n, month_dict[n] / month_sum * 100), end=' ')
    print('')
    month += 1
print('销量最低的为', max(total_sales_volume))
print('最畅销的为', min(total_sales_volume))
print('春季最畅销的是%s，夏季最畅销的是%s，秋季最畅销的是%s，冬季最畅销的是%s' % (
    four_seasons(spring), four_seasons(summer), four_seasons(fall), four_seasons(winter)))
