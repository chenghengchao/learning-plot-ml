# -*- coding: utf-8 -*-
import numpy as np
from sklearn.linear_model import LinearRegression


def createArray():
    x = [[0]*1]*6
    print x
    for i in range(6):
        x[i][0] = i+1
    print x #输出[[6], [6], [6], [6], [6], [6]]

    x = [[0]*1 for i in range(6)]
    print x
    for i in range(6):
        x[i][0] = i+1
    print x #[[1], [2], [3], [4], [5], [6]]
    return x

if __name__=='__main__':
    x = createArray()
    y = [[1], [2.1], [2.9], [4.2], [5.1], [5.8]]
    model = LinearRegression()
    model.fit(x, y)
    predicted = model.predict([13])[0]
    print predicted
    # 开放时间 门票价格 简介