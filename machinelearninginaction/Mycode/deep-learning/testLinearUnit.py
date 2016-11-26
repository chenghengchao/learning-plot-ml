# -*- coding:utf-8 -*-
from lineunit import LinearUnit


def get_training_dataset():
	'''
	构造5个人的收入数据
	'''
	input_vec = [[5], [3], [8], [1.4], [10.1]]
	labels = [5500, 2300, 7600, 1800, 11400]
	return input_vec, labels


def train_linear_unit():
	'''
	训练线性单元
	'''
	lu = LinearUnit(1)
	# print p.weights, p.bias
	input_vec, labels = get_training_dataset()
	lu.train(input_vec, labels, 10, 0.01)
	return lu


if __name__ == '__main__':
	linear_unit = train_linear_unit()
	print linear_unit

	print 'Work 3.4 years, monthly salary = %.2f' % linear_unit.predict([3.4])
	print 'Work 15 years, monthly salary = %.2f' % linear_unit.predict([15])
	print 'Work 1.5 years, monthly salary = %.2f' % linear_unit.predict([1.5])
	print 'Work 6.3 years, monthly salary = %.2f' % linear_unit.predict([6.3])
