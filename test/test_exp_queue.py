# test_exp_queue.py

# -*- coding: utf-8 -*-
from queues.exp_queue import Queue
import collections as clt
import pytest

init_dict = dict(zip(
					["lambda","beta","deque"],
					[1.0, 1.0, clt.deque()]
				))
def test_init():
	queue = Queue()
	assert queue.get_params() == init_dict

def test_add_client():
	queue = Queue()
	queue.add_client()
	assert queue.get_len() == 1
	queue.add_client(20)
	assert queue.get_len() == 21

def test_pop_fcfs():
	queue = Queue()
	assert queue.pop_fcfs() == None
	time = queue.add_client()
	assert queue.pop_fcfs() != None
	queue.add_client(10)
	queue_temp = queue.get_params()["deque"]
	assert queue_temp[0] == queue.pop_fcfs()

def test_pop_lcfs():
	queue = Queue()
	assert queue.pop_lcfs() == None
	time = queue.add_client()
	assert queue.pop_lcfs() != None
	queue.add_client(10)
	queue_temp = queue.get_params()["deque"]
	assert queue_temp[-1] == queue.pop_lcfs()