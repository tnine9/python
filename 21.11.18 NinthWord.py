import random
import time
import pymysql
import datetime

bank_name = '中国农业银行沙河分行'
the_limit = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 针对增删改
def update(sql, param):
    con = pymysql.connect(host="localhost", user="root", password='', database="bank")  # 连接数据库
    cursor = con.cursor()  # 创建控制台
    cursor.execute(sql, param)  # 执行sql语句
    con.commit()  # 提交到数据库
    cursor.close()  # 关闭控制台
    con.close()  # 关闭数据库链接


# 针对查询
def select(sql, param, mode="many", size=1):
    con = pymysql.connect(host="localhost", user="root", password='', database="bank")  # 连接数据库
    cursor = con.cursor()  # 创建控制台
    cursor.execute(sql, param)  # 执行sql语句

    if mode == "all":  # 全部查询
        return cursor.fetchall()
    elif mode == "one":  # 单个查询
        return cursor.fetchone()
    elif mode == "many":  # 多个查询，size为查询数量
        return cursor.fetchmany(size)

    con.commit()  # 提交到数据库
    cursor.close()  # 关闭控制台
    con.close()  # 关闭数据库链接
    data = cursor.fetchmany()  # 提取数据
    return data


# 欢迎界面
def welcome():
    print('\t当前时间为:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('''
    ****************************************************
    *               中国农业银行账户管理系统                *
    ****************************************************
    *                       选项                        *
    *                      1.开户                       *
    *                      2.存款                       *
    *                      3.取款                       *
    *                      4.转账                       *
    *                      5.查询                       *
    *                      6.退出                       *
    ****************************************************
    ''')
    a = input('\t请输入序号选择要办理的业务>>>')
    return a


# 开户
def open_an_account():
    while True:
        names = input("\t请输入您的姓名>>>")  # 获取用户姓名
        try:
            password = input("\t请输入您的密码>>>")  # 获取用户密码
            if len(password) != 6:
                raise ValueError()
            password = int(password)
        except ValueError:
            print('\t输入错误，密码只支持六位数字！')
            break
        country = input("\t请输入您的国籍>>>")  # 获取用户国籍
        province = input("\t请输入您的省份>>>")  # 获取用户省份
        street = input("\t请输入您的街道>>>")  # 获取用户街道
        door = input("\t请输入您的门牌号>>>")  # 获取用户门牌号
        try:
            remaining_sum = int(input("\t请输入您的初始账户金额>>>"))  # 获取用户账户金额
        except ValueError:
            print('\t输入错误，账户余额只支持数字！')
            break
        try:
            print('\t请输入序号选择账户类型，1.金卡  2.普通卡')
            account_type = int(input('\t>>>'))  # 获取用户类型
            if account_type != 1 and account_type != 2:
                raise ValueError()
        except ValueError:
            print('\t输入错误，请重新输入！')
            break

        account = random.randint(10000000, 99999999)  # 随机获取用户账号

        # 调用银行的数据库
        sql = "select count(*) from user"
        data = select(sql, [], mode="all")

        if data[0][0] >= 100:
            print("\t银行库已满，请携带身份证去其他银行办理！")
            break

        try:
            sql = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = [names, account, password, country, province, street, door, remaining_sum,
                     account_type, the_limit, bank_name, 0, the_limit]
            update(sql, param)  # 调用update函数
        except pymysql.err.IntegrityError:
            print("\t不允许重复开户！")
            break

        print("\t恭喜，开户成功！")
        info = '''
        ************************个人信息**********************
        *\t姓   名:%s
        *\t账   号:%s
        *\t密   码:%s
        *\t国   籍:%s
        *\t省   份:%s
        *\t街   道:%s
        *\t门 牌 号:%s
        *\t余   额:%s
        *\t账户类型:%s类卡
        *\t操作时间:%s
        *\t开户行名称:%s
        ****************************************************
                '''
        print(info % (names, account, password, country, province, street, door, remaining_sum,
                      account_type, the_limit, bank_name))
        break


# 存款
def dave_money():
    while True:
        names = input("\t请输入您的姓名>>>")
        try:
            password = input("\t请输入您的密码>>>")  # 获取用户密码
            if len(password) != 6:
                raise ValueError()
            password = int(password)
        except ValueError:
            print('\t输入错误，密码只支持六位数字！')
            break
        try:
            money = int(input("\t请输入存款金额>>>"))  # 获取存款金额
            if money <= 0:
                raise ValueError()
        except ValueError:
            print('\t输入错误，存款金额只支持正数！')
            break

        try:
            sql = 'SELECT password FROM user WHERE names = %s'
            data = select(sql, names, 'one')  # 获取数据库内信息

            if data[0] != password:
                print('\t密码错误，请核证后重试！')
                break
        except TypeError:
            print('\t未查询到账户信息，请您开户后重试！')
            break

        else:
            sql = 'UPDATE user SET remaining_sum = remaining_sum + %s WHERE names=%s'
            param = [money, names]
            update(sql, param)
            sql1 = 'SELECT names,account,remaining_sum,account_type FROM user WHERE names = %s'
            data = select(sql1, names, 'one')  # 获取数据库内信息
            print('\t恭喜，存款成功！')
            info = '''
    ************************个人信息**********************
    *\t姓   名:%s
    *\t账   号:%s
    *\t余   额:%s
    *\t账户类型:%s类卡
    *\t存款时间:%s
    *\t开户行名称:%s
    ****************************************************
                            '''
            print(info % (data[0], data[1], data[2], data[3], the_limit, bank_name))
            break


# 取款
def draw_money():
    while True:
        names = input("\t请输入您的姓名>>>")
        try:
            password = input("\t请输入您的密码>>>")  # 获取用户密码
            if len(password) != 6:
                raise ValueError()
            password = int(password)
        except ValueError:
            print('\t输入错误，密码只支持六位数字！')
            break
        try:
            money = int(input("\t请输入取款金额>>>"))  # 获取存款金额
            if money <= 0:
                raise ValueError()
        except ValueError:
            print('\t输入错误，取款金额只支持正数！')
            break

        try:
            sql = 'SELECT password,remaining_sum FROM user WHERE names = %s'
            param = [names]
            data = select(sql, param, 'one')  # 获取数据库内信息

            if data[0] != password:
                print('\t密码错误，请核证后重试！')
                break
            if data[1] - money < 0:
                print('\t您的账户余额不足！')
                break
        except TypeError:
            print('\t未查询到账户信息，请您开户后重试！')
            break

        else:
            sql = 'UPDATE user SET remaining_sum = remaining_sum - %s WHERE names=%s'
            param = [money, names]
            update(sql, param)
            sql1 = 'SELECT names,account,remaining_sum,account_type FROM user WHERE names = %s'
            data = select(sql1, names, 'one')  # 获取数据库内信息
            print('\t恭喜，取款成功！')
            info = '''
    ************************个人信息**********************
    *\t姓   名:%s
    *\t账   号:%s
    *\t余   额:%s
    *\t账户类型:%s类卡
    *\t存款时间:%s
    *\t开户行名称:%s
    ****************************************************
                            '''
            print(info % (data[0], data[1], data[2], data[3], the_limit, bank_name))
            break


# 转账
def transfer_accounts():
    while True:
        go_names = input("\t请输入转出账号的姓名>>>")  # 获取转出账号用户姓名
        try:
            go_password = input("\t请输入转出账号的密码>>>")  # 获取转出账号用户密码
            if len(go_password) != 6:
                raise ValueError()
            go_password = int(go_password)
        except ValueError:
            print('\t输入错误，密码只支持六位数字！')
            break
        come_names = input("\t请输入转入账号的姓名>>>")  # 获取转入账号用户姓名
        try:
            go_money = int(input("\t请输入转账金额>>>"))  # 获取转账金额
        except ValueError:
            print('\t输入错误，账户余额只支持数字！')
            break
        try:
            sql = 'SELECT operation_time FROM user WHERE names = %s'
            time_data = select(sql, go_names, 'one')  # 获取数据库内信息
            if time_data[0] + datetime.timedelta(1) <= datetime.datetime.now():
                sql = 'UPDATE user SET  cumulative_amount=0 WHERE names=%s'
                update(sql, go_names)

            #          姓名    密码      账户余额        账户类型       累计转账金额        操作时间
            sql = 'SELECT names,password,remaining_sum,account_type,cumulative_amount,operation_time' \
                  ' FROM user WHERE names = %s'
            data = select(sql, go_names, 'one')  # 获取数据库内信息
            sql = 'SELECT names,account_type FROM user WHERE names = %s'
            data2 = select(sql, come_names, 'one')  # 获取数据库内信息

            if data[1] != go_password:
                print('\t密码错误!')
                break
            elif data[2] - go_money < 0:
                print('\t账户余额不足!')
                break
            elif data[0] == data2[0]:
                print('\t账户相同!')
                break
            elif (data[3] == 1 and data[4] >= 50000) or (data[3] == 1 and data[4] + go_money > 50000):
                print('\t今日已限额!')
                break
            elif (data[3] == 2 and data[4] >= 20000) or (data[3] == 2 and data[4] + go_money > 20000):
                print('\t今日已限额!')
                break
            else:
                sql = 'UPDATE user SET remaining_sum = remaining_sum - %s WHERE names=%s '
                sql0 = 'UPDATE user SET remaining_sum = remaining_sum + %s WHERE names=%s '
                sql1 = 'UPDATE user SET cumulative_amount = cumulative_amount + %s WHERE names=%s '
                sql2 = 'UPDATE user SET operation_time=%s WHERE names=%s '
                param = [go_money, go_names]
                param0 = [go_money, come_names]
                param2 = [the_limit, go_names]
                update(sql, param)
                update(sql0, param0)
                update(sql1, param)
                update(sql2, param2)

                sql2 = 'SELECT names,remaining_sum,account_type,operation_time FROM user WHERE names = %s'
                data = select(sql2, go_names, 'one')  # 获取数据库内信息
                info = '''
    ************************转账信息**********************
    *\t转帐姓名:%s
    *\t收款姓名:%s
    *\t转账金额:%s
    *\t账户余额:%s
    *\t账户类型:%s类卡
    *\t操作时间:%s
    *\t银行名称:%s
    ****************************************************'''
                print(info % (data[0], come_names, go_money, data[1], data[2], data[3], bank_name))
            break

        except TypeError:
            print('\t未查询到账户信息，请您开户后重试！')
            break


# 查询
def query_information():
    while True:
        names = input("\t请输入您要查询的姓名>>>")
        try:
            password = input("\t请输入该账户的密码>>>")  # 获取用户密码
            if len(password) != 6:
                raise ValueError()
            password = int(password)
        except ValueError:
            print('\t输入错误，密码只支持六位数字！')
            break

        try:
            #               密码     姓名    账号     国家     省份     街道  门牌号   账户余额       账户类型       开户时间
            sql = 'SELECT password,names,account,country,province,street,door,remaining_sum,account_type,the_limit,' \
                  'bank_name,operation_time FROM user WHERE names = %s'
            #        开户行     最后操作时间
            data = select(sql, names, 'one')  # 获取数据库内信息

            if data[0] != password:
                print('\t密码错误,请核证后重试!')
                break
            else:
                print('\t信息如下:')
                info = '''
    ************************转账信息**********************
    *\t姓   名:%s                                       
    *\t账   号:%s 
    *\t账户类型:%s类卡
    *\t地址信息:
    *\t     国 籍：%s
    *\t     省 份：%s
    *\t     街 道：%s
    *\t     门牌号：%s
    *\t账户余额:%s
    *\t开户时间:%s
    *\t开户行名称:%s
    *\t最后操作时间:%s
    ****************************************************
                '''
                print(info % (
                    data[1], data[2], data[8], data[3], data[4], data[5], data[6], data[7], data[11], data[10],
                    data[9],))
            break
        except TypeError:
            print('\t未查询到账户信息，请您开户后重试！')
            break


# 系统主体
while True:
    option_number = welcome()
    if option_number == '1':
        open_an_account()
    elif option_number == '2':
        dave_money()
    elif option_number == '3':
        draw_money()
    elif option_number == '4':
        transfer_accounts()
    elif option_number == '5':
        query_information()
    elif option_number == '6':
        print('\t欢迎您下次光临！')
        break
    else:
        print('\t输入错误！请重新输入！')
