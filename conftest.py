import pytest


# 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
# 在conftest.py配置里写方法可以实现数据共享，不需要import导入，可以跨文件共享

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_configure(config):
    config.addinivalue_line("markers",
                            "test_normal: mark test functions that test data type errors")
    config.addinivalue_line("markers",
                            "test_data_type_error: mark test functions that test data type errors")
    config.addinivalue_line("markers",
                            "test_data_range: mark test functions that test data type errors")
    config.addinivalue_line("markers",
                            "test_zero_division_error: mark test functions that test data type errors")


# 通过@pytest.fixture实现测试装置以及参数化
@pytest.fixture(scope="session", autouse=True)
def open_caculator():
    print("\n打开计算器app操作")
    yield
    close_caculator()


def close_caculator():
    print("\n关闭计算器app操作")
