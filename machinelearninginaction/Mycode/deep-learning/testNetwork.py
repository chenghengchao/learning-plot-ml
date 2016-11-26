# -*- coding:utf-8 -*-
from network import *
import struct


class Loader(object):
	"""数据加载父类"""
	def __init__(self, path, count):
		'''
		初始化加载器
		path: 数据文件路径
		count: 文件中的样本个数
		'''
		self.path = path
		self.count = count


	def get_file_content(self):
		'''
		读取文件内容
		'''
		f = open(self.path, 'rb')
		content = f.read()
		f.close()
		return content


	def to_int(self, byte):
		'''
		将unsigned byte字符转换为整数
		'''

		return struct.unpack('B', byte)[0]

	
class ImageLoader(Loader):
	"""图像数据加载器"""
	def get_picture(self, content, index):
		start = index * 28 * 28 + 16
		picture = []
		for i in range(28):
			picture.append([])
			for j in range(28):
				picture[i].append(
					self.to_int(content[start + i * 28 + j]))
		return picture


	def get_one_sample(self, picture):
		'''
		内部函数，将图像转化为样本的输入向量
		'''
		sample = []
		for i in range(28):
			for j in range(28):
				sample.append(picture[i][j])
		return sample


	def load(self):
		'''
		加载数据文件，获得全部样本的输入向量
		'''
		content = self.get_file_content()
		data_set = []
		for index in range(self.count):
			data_set.append(
				self.get_one_sample(
					self.get_picture(content, index)))
		return data_set

class LabelLoader(Loader):
	"""数据标签加载器"""
	def load(self):
		'''
		加载数据文件，获得全部样本的标签向量
		'''
		content = self.get_file_content()
		labels = []
		for index in range(self.count):
			labels.append(self.norm(content[index + 8]))
		return labels


	def norm(self, label):
		'''
		内部函数，将一个值转换为10维标签向量
		'''
		label_vec = []
		label_value = self.to_int(label)
		for i in range(10):
			if i == label_value:
				label_vec.append(0.95)
			else:
				label_vec.append(0.05)
		return label_vec


def get_training_data_set():
	'''
	获得训练数据集
	'''
	image_loader = ImageLoader('train-images.idx3-ubyte', 60000)
	label_loader = LabelLoader('train-labels.idx1-ubyte', 60000)
	print "train data load finished ..."
	return image_loader.load(), label_loader.load()


def get_test_data_set():
	'''
	获得测试数据集
	'''
	image_loader = ImageLoader('t10k-images.idx3-ubyte', 10000)
	label_loader = LabelLoader('t10k-labels.idx1-ubyte', 10000)
	print "test data load finished ..."
	return image_loader.load(), label_loader.load()


def get_result(vec):
    # vec是一个10维向量
	max_value_index = 0
	max_value = 0
	for index in len(vec):
	    if vec[i] > max_value:
	        max_value = vec[i]
	        max_value_index = i
	return max_value_index


def evaluate(network, test_data_set, test_labels):
	correct = 0
	total = len(test_data_set)

	for i in range(total):
	    label = get_result(test_labels[i])
	    predict = get_result(network.predict(test_data_set[i]))
	    if label == predict:
	        correct += 1
	return float(correct) / float(total)


def train_and_evaluate():
	last_error_ratio = 1.0
	epoch = 0
	train_data_set, train_labels = get_training_data_set()
	test_data_set, test_labels = get_test_data_set()
	network = Network([784, 300, 10])
	while True:
		epoch += 10
		network.train(train_data_set, train_labels, 0.1, 10)
		error_ratio = evaluate(network, test_data_set, test_labels)
		print 'after epoch %d, error ratio is %f' % (epoch, error_ratio)
		if error_ratio > last_error_ratio:
		    break
		else:
		    last_error_ratio = error_ratio


if __name__ == '__main__':
	train_and_evaluate()