# -*- coding:utf-8 -*-
from Perceptron import Perceptron

def f(x):
	'''
	定义激活函数
	'''
	return 1 if x > 0 else 0


def get_training_dataset():
	'''
	基于and真值表构建训练数据
	'''
	input_vec = [[1,1], [0,0], [1,0], [0,1]]
	labels = [1, 0, 0, 0]
	return input_vec, labels


def train_and_perception():
	'''
	使用and真值表训练感知器
	'''
	p = Perceptron(2, f)
	# print p.weights, p.bias
	input_vec, labels = get_training_dataset()
	p.train(input_vec, labels, 10, 0.1)
	return p


if __name__ == '__main__':
	and_perception = train_and_perception()
	print and_perception

	print '1 and 1 = %d' % and_perception.predict([1, 1])
	print '0 and 0 = %d' % and_perception.predict([0, 0])
	print '1 and 0 = %d' % and_perception.predict([1, 0])
	print '0 and 1 = %d' % and_perception.predict([0, 1])
