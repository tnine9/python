import _thread
import time

egg_tart_cabinet = 0  # 蛋挞柜子
cashier = 0


# 厨师类
class Cook(_thread):
    egg_tart = 0

    def run(self) -> None:
        global egg_tart_cabinet
        global cashier
        the_limit = time.time()
        while True:

            times = time.time()
            if egg_tart_cabinet >= 500:
                time.sleep(3)
            else:
                egg_tart_cabinet = egg_tart_cabinet + 1
                self.egg_tart = self.egg_tart + 1
            if times - the_limit >= 60:
                break


class Customer(_thread):
    money = 5000
    buy = 0

    def run(self) -> None:
        global egg_tart_cabinet
        global cashier
        the_limit = time.time()
        while True:
            times = time.time()
            if egg_tart_cabinet <= 0:
                time.sleep(2)
            else:
                egg_tart_cabinet = egg_tart_cabinet - 10
                cashier = cashier + 3
                self.money = self.money - 3
                self.buy = self.buy + 1
            if (times - the_limit >= 60) or (self.money <= 0):
                break


cook1 = Cook()
cook2 = Cook()
cook3 = Cook()
customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
customer4 = Customer()
customer5 = Customer()
customer6 = Customer()
cook1.start()
cook2.start()
cook3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()
cook1.join()
cook2.join()
cook3.join()
customer1.join()
customer2.join()
customer3.join()
customer4.join()
customer5.join()
customer6.join()
print('第一个厨师卖了%s个蛋挞，他的工资是%s！' % (cook1.egg_tart, cook1.egg_tart * 1.5))
print('第二个厨师卖了%s个蛋挞，他的工资是%s！' % (cook2.egg_tart, cook2.egg_tart * 1.5))
print('第三个厨师卖了%s个蛋挞，他的工资是%s！' % (cook3.egg_tart, cook3.egg_tart * 1.5))
print('顾客一买了%s个蛋挞！' % customer1.buy)
print('顾客二买了%s个蛋挞！' % customer2.buy)
print('顾客三买了%s个蛋挞！' % customer3.buy)
print('顾客四买了%s个蛋挞！' % customer4.buy)
print('顾客五买了%s个蛋挞！' % customer5.buy)
print('顾客六买了%s个蛋挞！' % customer6.buy)
print('柜子里还剩%s个蛋挞！' % egg_tart_cabinet)
