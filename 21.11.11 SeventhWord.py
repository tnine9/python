import random
import time

bank_name = '中国农业银行沙河分行'
bank_database = {}  # 银行的数据库


def welcome():  # 欢迎界面
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


def database_open_an_account(account, names, password, country, province, street, door, remaining_sum,
                             account_type):  # 银行的数据库开户
    if len(bank_database) > 10:
        return 3
    elif names in bank_database:
        return 2
    else:
        bank_database[names] = {
            'account': account,
            'password': password,
            'country': country,
            'province': province,
            'street': street,
            'door': door,
            'remaining_sum': remaining_sum,
            'bank_name': bank_name,
            'account_type': account_type,
            'the_limit': 0,
            'localtime_h': 0,
            'localtime_d': 0,
        }
        return 1


def bank_savemoney_account():  # 银行的数据库存款
    names = input("\t请输入您的姓名>>>")
    if names not in bank_database:
        return 2, 0
    elif names in bank_database:
        password = input("\t请输入您的密码>>>")
        if int(password) == bank_database[names]["password"]:
            m = input("\t请输入存款金额>>>")
            bank_database[names]["remaining_sum"] += int(m)
            return 1, bank_database[names]["remaining_sum"]
        else:
            return 3, 0


def bank_drawmoney_account():  # 银行的数据库取钱
    names = input("\t请输入您的姓名>>>")
    if names not in bank_database:
        return 1, 0
    elif names in bank_database:
        password = input("\t请输入您的密码>>>")
        if int(password) != bank_database[names]['password']:
            return 2, 0
        else:
            money = int(input('\t请输入取款金额>>>'))

            if money > bank_database[names]['remaining_sum']:
                return 3, 0
            else:
                bank_database[names]['remaining_sum'] -= money
                return 4, bank_database[names]['remaining_sum']


def database_transfer_accounts(go_names, come_names, go_password, go_money):  # 银行的转账方法
    go_names, come_names, go_password, go_money = go_names, come_names, go_password, go_money
    localtime_h = int(time.strftime("%H", time.localtime()))  # 获取当前时间
    localtime_d = int(time.strftime("%d", time.localtime()))  # 获取当前日期
    if (bank_database[go_names]['localtime_d'] + 1 == localtime_d and bank_database[go_names][
        'localtime_h'] == localtime_h) or (localtime_d > bank_database[go_names]['localtime_d']):
        bank_database[go_names]['the_limit'] = 0
    if go_names == come_names:
        return 4
    a = bank_database.get(go_names, False)
    b = bank_database.get(come_names, False)
    if (a == False) or (b == False):
        return 1
    else:
        c = bank_database[go_names].get('password', False)
        if go_password != c:
            return 2
        else:
            d = bank_database[go_names].get('remaining_sum')
            if d < go_money:
                return 3
            else:
                if (bank_database[go_names]['account_type'] == 1 and go_money > 50000) or (
                        bank_database[go_names]['account_type'] == 1 and bank_database[go_names][
                    'the_limit'] > 50000) or (
                        bank_database[go_names]['account_type'] == 1 and bank_database[go_names][
                    'the_limit'] + go_money > 50000):

                    return 6
                elif (bank_database[go_names]['account_type'] == 2 and go_money > 20000) or (
                        bank_database[go_names]['account_type'] == 2 and bank_database[go_names][
                    'the_limit'] > 20000) or (bank_database[go_names]['account_type'] == 2 and bank_database[go_names][
                    'the_limit'] + go_money > 20000):
                    return 6
                else:
                    bank_database[go_names]['remaining_sum'] = bank_database[go_names]['remaining_sum'] - go_money
                    bank_database[come_names]['remaining_sum'] = bank_database[come_names]['remaining_sum'] + go_money
                    bank_database[go_names]['the_limit'] = bank_database[go_names]['the_limit'] + go_money
                    bank_database[go_names]['localtime_h'] = int(time.strftime("%H", time.localtime()))
                    bank_database[go_names]['localtime_h'] = int(time.strftime("%d", time.localtime()))

                    return 5


def bank_about():  # 银行的数据库查询
    about_name = input('\t请输入您的姓名>>>')
    if about_name not in bank_database:
        return 1, None
    else:
        about_password = int(input('\t请输入您的密码>>>'))
        if about_password != bank_database[about_name]['password']:
            return 2, None
        else:
            return 3, about_name


def open_an_account():  # 开户
    while 1:
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
            money = int(input("\t请输入您的初始账户金额>>>"))  # 获取用户账户金额
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

        account = random.randint(10000000, 99999999)  # 获取用户账号
        # 调用银行的数据库
        status = database_open_an_account(account, names, password, country, province, street, door, money,
                                          account_type)

        if status == 3:
            print("\t银行库已经满了！请携带证件到其他银行办理！")
        elif status == 2:
            print("\t不允许重复开户！")
        elif status == 1:
            print("\t恭喜，开户成功！")
            info = '''
    ************************个人信息**********************
    *\t姓   名:%s                                       
    *\t账   号:%s
    *\t密   码:%s
    *\t国   籍:%s
    *\t省   份:%s
    *\t街   道:%s
    *\t余   额:%s
    *\t账户类型:%s类卡
    *\t门 牌 号 :%s
    *\t开户行名称:%s
    ****************************************************
            '''
            print(info % (names, account, password, country, province, street, money, account_type, door, bank_name))
        break


def SaveMoney():  # 存款
    (a, b) = bank_savemoney_account()
    if a == 1:
        print("\t存款成功!")
        print("\t您的余额为:", b)
    elif a == 2:
        print("\t请先开户!")
    elif a == 3:
        print("\t密码错误!")


def DrawMoney():  # 取钱
    (c, d) = bank_drawmoney_account()
    if c == 1:
        print('\t请先开户!')
    elif c == 2:
        print("\t密码错误!")
    elif c == 3:
        print("\t余额不足!")
    elif c == 4:
        print("\t取款成功!")
        print("\t您的余额为:", d)


def transfer_accounts():  # 转账
    while 1:
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

        status = database_transfer_accounts(go_names, come_names, go_password, go_money)
        if status == 1:
            print('\t用户不存在!')
            break
        elif status == 2:
            print('\t密码错误!')
            break
        elif status == 3:
            print('\t账户余额不足!')
            break
        elif status == 4:
            print('\t账户相同!')
            break
        elif status == 6:
            print('\t今日已限额!')
            break
        elif status == 5:
            info = '''
    ************************转账信息**********************
    *\t转入姓名:%s                                       
    *\t转出姓名:%s
    *\t转账金额:%s 
    *\t账户余额:%s
    *\t对方余额:%s
    *\t银行名称:%s
    ****************************************************'''
            print(info % (go_names, come_names, go_money, bank_database[go_names]['remaining_sum'],
                          bank_database[come_names]['remaining_sum'], bank_name))
        break


def about():  # 查询
    (about_i, about_name) = bank_about()
    if about_i == 1:
        print('\t账户信息不存在! ')
    elif about_i == 2:
        print("\t密码错误!")
    elif about_i == 3:
        print('\t信息如下')
        info = '''
    ************************转账信息**********************
    *\t姓   名:%s                                       
    *\t账   号:%s
    *\t取款密码:%s 
    *\t账户类型:%s
    *\t地址信息:
    *\t     国 籍：%s
    *\t     省 份：%s
    *\t     街 道：%s
    *\t     门牌号：%s
    *\t账户余额:%s
    *\t银行名称:%s
    ****************************************************
    '''
        print(info % (about_name, bank_database[about_name]['account'], bank_database[about_name]['password'],
                      bank_database[about_name]['account_type'], bank_database[about_name]['country']
                      , bank_database[about_name]['province'], bank_database[about_name]['street'],
                      bank_database[about_name]['door'], bank_database[about_name]['remaining_sum']
                      , bank_database[about_name]['bank_name']))


while True:
    option_number = welcome()
    if option_number == '1':
        open_an_account()
    elif option_number == '2':
        SaveMoney()
    elif option_number == '3':
        DrawMoney()
    elif option_number == '4':
        transfer_accounts()
    elif option_number == '5':
        about()
    elif option_number == '6':
        print('\t欢迎您下次光临！')
        break
    else:
        print('\t输入错误！请重新输入！')
