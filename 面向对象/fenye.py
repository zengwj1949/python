
# 分页项目；
# 创建类；
class Pagenation(object):
    '''
    处理分页相关代码
    '''

    # 类中的特殊方法；
    def __init__(self, page, per_page_num = 10):
        """
        初始化
        :param page:输入需要查看的页面
        :param per_page_num:每次显示的行数
        """
        self.page = page
        self.per_page_num = per_page_num

    # 类的普通方法；
    def start(self):
        """
        计算索引的起始位置
        return:
        """
        return (self.page - 1) * self.per_page_num

    # 类的普通方法；
    def end(self):
        """
        计算索引的结束位置
        return
        """
        return self.page * self.per_page_num

# 建立空列表；
data_list = []

# 向空列表中添加需要查看的内容；
for i in range(1, 901):
    data_list.append('alex-%s' %i)

while True:
    page = int(input("请输入您所要查看的页码： "))
    obj = Pagenation(page)
    page_data_list = data_list[obj.start():obj.end()]

    for item in page_data_list:
        print(item)
