from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from bank import transfer_accounts

da = [
    ['1', 111111, '周洋', 1, 0],  # 正常测试
    # 密码测试
    ['1', '111111', '周洋', 1, 1],
    ['1', 11111, '周洋', 1, 1],
    ['1', 111111, '周洋', 1, 0],
    ['1', 1111111, '周洋', 1, 1],
    ['1', 222222, '周洋', 1, 1],
    # 金额测试
    ['1', 111111, '周洋', 1, 0],
    ['1', 111111, '周洋', 0, 2],
    ['1', 111111, '周洋', -1, 2],
    ['1', 111111, '周洋', 10000000000, 2],
    ['1', 111111, '周洋', -10000000000, 2],
    ['1', 111111, '周洋', '1', 2],
    # 账户测试
    ['1', 111111, '1', 1, 3],
    [1, 111111, '周洋', 1, 3],
    ['周洋', 111111, 1, 1, 3],
    ['2', 222222, '周洋', 2, 3],
    ['周洋', 222222, '2', 2, 3],
    #限额测试
    ['3', 111111, '4', 49999, 0],
    ['4', 111111, '3', 50000, 0],
    ['3', 111111, '4', 50001, 4],
    ['3', 111111, '4', 2, 4],
    ['3', 111111, '4', 1, 0],
    ['5', 111111, '6', 19999, 0],
    ['6', 111111, '5', 20000, 0],
    ['5', 111111, '6', 20001, 4],
    ['5', 111111, '6', 2, 4],
    ['5', 111111, '6', 1, 0],
]


@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def testAdduser(self, a, b, c, d, e):
        s = transfer_accounts(a, b, c, d)

        self.assertEqual(s, e)
