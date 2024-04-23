import allure
import pytest
from get_data.get_data import GetData
from func.func import Caculator

"""
-------------------------------------------------------------
case_04: 用户输入运算数据a、b，运算规则不合法

优先级：

前置条件：

测试步骤；
        1、输入数据a、b, b=0，调用div()方法；

预期结果：
        1、程序输出异常类型，并输出异常提示：除数不能为0；
--------------------------------------------------------------

作者：wang-min
创建时间：2024.04.23
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

    @allure.title("用户输入运算数据a、b，运算规则不合法")
    @pytest.mark.test_zero_division_error
    @pytest.mark.xfail
    @pytest.mark.parametrize('a,b,expected', GetData.get_zero_division_error())
    def test_zero_division_error(self, a, b, expected):
        """
        测试div()函数对除数为0的异常进行异常提示
        :param a: 模拟用户输入的数据 a
        :param b: 模拟用户输入的数据 b
        :param expected: 输出异常类型ZeroDivisionError，并输出异常提示：除数不能为0
        :return: 返回异常类型ZeroDivisionError，并输出异常提示：除数不能为0
        """
        caculator = Caculator(a, b)
        assert caculator.div() == expected

    def teardown_method(self):
        """
        清除操作
        :return: 返回清除操作是否成功的结果
        """
        pass
