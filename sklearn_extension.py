def onehot_encoder(X, X_name=None)->pd.DataFrame:
    '''
    :param X:需要独热编码的原序列
    :param X_name:原序列的列名，方便编码后进行重命名
    :return: 独热编码之后的新数据框
    '''
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder

    X = np.array(X.fillna('NAN'))
    laber_encoder = LabelEncoder()
    integer_encoded = laber_encoder.fit_transform(X)

    onehot_encoder = OneHotEncoder(sparse=False, categories='auto')
    integer_encoded = integer_encoded.reshape(-1, 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    onehot_encoded = pd.DataFrame(onehot_encoder.fit_transform(integer_encoded))

    if X_name:  # 列名重命名
        onehot_encoded.columns = [X_name + '_' + laber_encoder.inverse_transform([i])[0,] for i in
                                  onehot_encoded.columns]
    return onehot_encoded
