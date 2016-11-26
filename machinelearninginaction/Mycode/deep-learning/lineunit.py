# -*- coding:utf-8 -*-
from Perceptron import Perceptron

f = lambda x: x
class LinearUnit(Perceptron):
	"""实现线性单元的类"""
	def __init__(self, input_num):
		# super(LinearUnit, self).__init__()
		Perceptron.__init__(self, input_num, f)	