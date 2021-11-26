class Cup():
    height = 0
    volume = ''
    color = ''
    texture = ''

    def water(self):
        print('一个%scm高的%s色的%s杯子装了%s容积的水' % (self.height, self.color, self.texture, self.volume))


a = Cup
a.height = 20
a.volume = 200
a.color = '黑'
a.texture = '不锈钢'
a().water()


class computer():
    screen = 0
    price = 10
    cpu = ''
    memory = ''
    time = 0

    def typewriting(self):
        print('我用%s元的%s寸大屏电脑打字' % (self.price, self.screen))

    def play_the_game(self):
        print('我用%scpu的大屏电脑打了%s小时游戏' % (self.cpu, self.time))

    def see(self):
        print('我用%s内存的大屏电脑看视频' % self.memory)


b = computer
b.screen = 200
b.price = 10
b.cpu = 'I5 9400'
b.memory = '10000T'
b.time = 20
b().typewriting()
b().play_the_game()
b().see()
