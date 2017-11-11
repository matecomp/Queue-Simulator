# -*- coding: utf-8 -*-
import numpy as np
import collections as clt


class Queue(object):
	"""docstring for Queue"""
	def __init__(self, lamb=1.0):
		super(Queue, self).__init__()
		self.__params = self.make_params_dict(lamb, clt.deque())

	def make_params_dict(self, lamb, deque):
		return dict(zip(
			["lambda", "beta", "deque"],
			[lamb, 1/lamb, deque]
		))

	def get_params(self):
		return self.__params

	def get_len(self):
		return len(self.__params["deque"])

	def add_client(self, size=None):
		time_client = np.random.exponential(scale=self.__params["beta"], size=size)
		if size is None:
			self.__params["deque"].append(time_client)
		else:
			self.__params["deque"].extend(time_client)

	def pop_fcfs(self):
		if len(self.__params["deque"]) == 0:
			return None
		return self.__params["deque"].popleft()

	def pop_lcfs(self):
		if len(self.__params["deque"]) == 0:
			return None
		return self.__params["deque"].pop()


if __name__ == '__main__':
	print("Ops...")