import yaml


class GetData:
    """
    获取数据类： 用于获取测试数据的函数
              get_add_data()：静态方法，获取用于测试add()函数的测试数据
              get_div_data()：静态方法，获取用于测试div()函数的测试数据
    """

    @staticmethod
    def get_add_data():
        """
        获取用于测试add()函数的测试数据
        :return: 返回数据结构：[[1,1,2]]
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/add_data.yaml', 'r', encoding="UTF-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_add_data_error():
        """
        获取用于测试add()函数的异常测试数据
        :return:
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/add_data_error.yaml', 'r', encoding="UTF-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_div_data():
        """
        获取用于测试div()函数的测试数据
        :return: 返回数据结构：[[10,5,2]]
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/div_data.yaml', 'r', encoding="UTF-8") as f:
            data = yaml.safe_load(f)
            return data

