# -*- coding:utf-8 -*-
class Perceptron(object):
	"""自己实现感知器"""
	def __init__(self, input_num, activator):
		'''
		初始化感知器。设置输入参数的个数，以及激活函数
		激活函数类型为 double->double
		'''
		self.activator = activator
		# 权重向量初始化为0，偏置项初始化为0
		self.weights = [0.0 for _ in range(input_num)]
		self.bias = 0.0
	

	def __str__(self):
		'''
		打印学习到的权重、偏置项
		'''
		return 'Weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)


	def predict(self, input_vec):
		'''
		输入向量，输出感知器的计算结果
		'''
		# reduce 函数的第三个参数表示初始值
		return self.activator(
			reduce(lambda a, b: a + b,
				map(lambda (x, w): x*w,
					zip(input_vec, self.weights))
				, 0.0) + self.bias)


	def train(self, input_vec, labels, iteration, rate):
		'''
		输入训练数据：一组向量、与每个向量对应的label；以及训练轮数，学习率
		'''
		for i in range(iteration):
			self._one_iteration(input_vec, labels, rate)


	def _one_iteration(self, input_vecs, labels, rate):
		'''
		一次迭代，把所有训练数据过一遍
		'''
		samples = zip(input_vecs, labels)
		for i, (input_vec, label) in enumerate(samples):
			output = self.predict(input_vec)
			self._update_weights(input_vec, output, label, rate)
			# print str(i) + "次迭代", self.weights



	def _update_weights(self, input_vec, output, label, rate):
		'''
		按照感知器规则更新权重
		'''
		delta = label - output
		self.weights = map(lambda (x, w): w + rate * delta * x,
			zip(input_vec, self.weights))
		self.bias += rate * delta