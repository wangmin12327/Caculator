import pytest
from get_data.get_data import GetData
from func.func import Caculator

"""
-------------------------------------------------------------
case_01: 用户输入运算数据a、b, 程序输出正确的结果

优先级：

前置条件：

测试步骤；
        1、输入数据a、b, 调用add()方法；
        2、输入数据a、b, 调用div()方法；

预期结果：
        1、程序输出a加b的结果；
        2、程序输出a除以b的结果；
--------------------------------------------------------------

作者：wang-min
创建时间：2024.04.15
"""


class TestCase:
    """
    测试用例类： 测试用例执行步骤
    """

    def setup_method(self):
        """
        执行用例的前置条件
        :return:
        """
        pass

    @pytest.mark.parametrize('a,b,expected', GetData.get_add_data())
    def test_add(self, a, b, expected):
        caculator = Caculator(a, b)
        assert caculator.add() == expected

    @pytest.mark.parametrize('a,b,expected', GetData.get_div_data())
    def test_div(self, a, b, expected):
        caculator = Caculator(a, b)
        assert caculator.div() == expected

    def teardown_method(self):
        """
        清除操作
        :return: 返回清除操作是否成功的结果
        """
        pass
