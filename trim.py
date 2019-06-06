def is_int(x):
    '''
    判断一个数值型的数字是否是真正的整数，而不是按照type去判断
    :param x: 输入的数字
    :return: 是否为整数
    '''
    x_split=math.modf(x)
    if x_split[0]==0:
        return True
    else:
        return False