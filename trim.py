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

def sum_row(data,col_name=None):
    '''
    :param data:
    :param col_name:
    :return:指定的列每行的和
    '''
    if col_name:
        return data[col_name].apply(lambda x:sum([i if pd.notnull(i) else 0 for i in x]),axis=1)
    else:
        return data.apply(lambda x:sum([i if pd.notnull(i) else 0 for i in x]),axis=1)