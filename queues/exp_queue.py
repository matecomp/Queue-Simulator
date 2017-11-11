# -*- coding: utf-8 -*-
import numpy as np
import collections as clt


class FCFS(object):
	"""docstring for FCFS"""
	def __init__(self, servers=list()):
		super(FCFS, self).__init__()
		self.servers = servers
		self.queue = clt.deque()

	def add_client(self, time_client):
		self.queue.append(time_client)
