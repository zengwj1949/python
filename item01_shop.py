product_list = [
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),
]

saving = input('Please input your money: ')
shopping_car = []
# 此方法检测字符串是否只由数字组成；
if saving.isdigit():
    saving = int(saving)
    while True:
       #打印商品内容；
        for i, v in enumerate(product_list,1):
            print(i, '>>>: ', v)
        choice = input('选择购买商品的编号[退出：q]: ')
        # 验证输入是否合法；
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(product_list):
                # 将用户选择的商品用choice取出来；
                p_item = product_list[choice-1]
                # 如果资金充足，用本金减去商品价格，并把商品加入购物车；
                if p_item[1] < saving:
                    saving-=p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，还剩%s'%saving)
                    print(p_item)
            else:
                print('商品编码不存在。')
        elif choice == 'q':
            print('--------------------您已购买了如下商品--------------------')
            # 循环遍历购物车里的商品，购物车中是已买商品；
            for i in shopping_car:
                print(i)
            print('您还剩下￥%s'%saving)
            break
        else:
            print('invalid input')
