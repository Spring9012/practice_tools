def is_int(x):
    '''
    判断一个数值型的数字是否是真正的整数，而不是按照type去判断
    :param x: 输入的数字
    :return: 是否为整数
    '''
    import math
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



def timing_func(f):
    '''
    :param f:需要增加功能的原始函数
    :return:装饰过的函数
    '''
    def timing(*args,**kwargs):
        print(time.strftime('%Y-%m-%d %H:%M:%S'),'开始')
        start=time.perf_counter()
        test=f(*args,**kwargs)
        print('花费时间{:2f}mins'.format((time.perf_counter()-start)/60))
        return test
    return timing


def iterator_list(lists):
    '''lists:需要遍历的列表list，如：[list1,list2.list3]'''
    try:
        import reduce
    except:
        from functools import reduce
    
    def myfunc(list1,list2):
        return [i+[j] if type(i) is list else [i,j] for i in list1 for j in list2]
    
    return reduce(myfunc,lists)


def bin_func(x,bin_cut_point):
    '''
    x:需要找到分组的值
    bin_cut_point：cut off的值的list，已经排序完成
    return:左开右闭
    '''
    order=np.searchsorted(bin_cut_point,x)
    if order==0:
        return '(-inf,'+str(bin_cut_point[0])+']'
    elif order==len(bin_cut_point):
        return '('+str(bin_cut_point[-1])+',inf)'
    else:
        return '('+str(bin_cut_point[order-1])+','+str(bin_cut_point[order])+']'