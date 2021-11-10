city = {
    '北京': {
        '东城区': {
            '公园': ['天坛公园', '中山公园', '龙潭公园'],
            '商场': ['银河购物中心'],
            '剧院': ['保利剧院', '德云社', '首都剧场'],
            '博物馆': ['故宫博物院', '中国国家博物馆', '中国美术院', '北京自然博物馆'],
            '纪念馆': ['毛主席纪念堂', '老舍纪念馆'], },
        '西城区': {
            '公园': ['北海公园', '景山公园', '北京动物园'],
            '商场': ['西单商业街'],
            '剧院': ['国家大剧院', '湖广会馆', ],
            '博物馆': ['鲁迅博物馆', '首都博物馆', '中国地质博物馆', ],
            '纪念馆': ['梅兰芳纪念馆', '宋庆龄故居', '鲁迅故居'], },
        '海淀区': {
            '公园': ['颐和园', '圆明园', '北京植物园', '香山公园'],
            '大学': ['北京大学', '清华大学', '中国人民大学', '北京航空航天大学'],
            '剧院': ['国家大剧院', '湖广会馆', ],
            '博物馆': ['石刻艺术博物馆', '中国人民革命军事博物馆', ], },
        '朝阳区': {
            '公园': ['奥利匹克森林公园', '朝阳公园', ],
            '商场': ['三里屯'],
            '剧院': ['京城梨园', '中央电视台', ],
            '博物馆': ['观复博物馆', '中国电影博物馆', ],
            '体育馆': ['鸟巢', '水立方', '国家奥林匹克体育中心'], },
    },
    '上海': {},
    '广州': {},
    '深圳': {},
}
gift = {
    '翡翠': {'极品冰种翡翠大佛': 100000, '高端糯种翡翠镯': 1000, '豆种吊坠': 10},
    '文玩': {'极品文玩核桃': 100000, '高端降龙木手串': 1000, '普通念珠': 10},
    '糕点': {'芳香四溢全聚德烤鸭': 100000, '稻香村糕点礼盒': 1000, '王致和臭豆腐': 10}, }


def showCity(data):
    for i in data:
        print(i)


while True:
    print("---------------欢迎来到旅行社-----------------")
    print("有以下城市可以去：")
    showCity(city)
    chose = input("请输入您要去的城市：")

    if chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    elif chose not in city:
        print("输入非法！请重新输入：")
    else:
        showCity(city[chose])
        chose2 = input("请输入您要去的市区：")
        if chose2 == "q" or chose2 == "Q":
            print("欢迎下次光临！")
            break
        elif chose2 not in city[chose]:
            print("输入非法！请重新输入：")

        else:
            showCity(city[chose][chose2])
            chose3 = input("请输入要去的景点类型：")
            if chose3 == "q" or chose3 == "Q":
                print("欢迎下次光临！")
                break
            elif chose3 not in city[chose][chose2]:
                print("输入非法！请重新输入：")
            else:
                showCity(city[chose][chose2][chose3])
                chose4 = input("请输入要去的具体景点:")
                if chose4 == "q" or chose4 == "Q":
                    print("欢迎下次光临！")
                    break
                elif chose4 not in city[chose][chose2][chose3]:
                    print("输入非法！请重新输入：")
                else:
                    print("每张票1000元/人！")
                    money = input('请问您带了多少钱')
                    if money == "q" or money == "Q":
                        print("欢迎下次光临！")
                    else:
                        money = int(money)
                        money = money - 1000
                        if money <= 0:
                            print('再见，穷逼！')
                            break
                        while True:
                            gift1 = input("是否买点纪念品？")
                            if gift1 == '是' or gift1 == 'yes' or gift1 == 'Yes' or gift1 == 'y' or gift1 == 'Y':
                                print('我们有以下几种纪念品')
                                showCity(gift)
                                gift2 = input('请选择礼品类型:')
                                if gift2 == "q" or gift2 == "Q":
                                    print("欢迎下次光临！")
                                    break
                                elif gift2 not in gift:
                                    print("输入非法！请重新输入：")
                                else:
                                    print('我们有以下纪念品')
                                    showCity(gift[gift2])
                                    gift3 = input('请选择要购买的礼品:')
                                    if gift3 == "q" or gift3 == "Q":
                                        print("欢迎下次光临！")
                                        break
                                    elif gift3 not in gift[gift2]:
                                        print("输入非法！请重新输入：")
                                    else:
                                        money = money - gift[gift2][gift3]
                                        print('您的余额为:',money)
                                        if money <= 0:
                                            print('再见，穷逼！')
                                            break
                            else:
                                print('再见，穷逼！')
                                break
