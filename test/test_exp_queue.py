# test_exp_queue.py

# -*- coding: utf-8 -*-
from queues.exp_queue import Queue
import collections as clt
import pytest

init_dict = dict(zip(
					["lambda","beta","start_time", "deque"],
					[1.0, 1.0, 0.0, clt.deque()]
				))
def test_init():
	queue = Queue()
	assert queue.get_params() == init_dict

def test_gets():
	queue = Queue()
	assert queue.get_len() == 0
	assert queue.get_time() == 0.0

def test_add_client_and_get_len():
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

def test_update():
	queue = Queue()
	l1 = queue.get_len()
	assert queue.get_time() == 0.0
	queue.update(10.0)
	l2 = queue.get_len()
	assert queue.get_time() == 10.0
	assert l1 <= l2
	queue.update(10000.0)
	l3 = queue.get_len()
	assert queue.get_time() == 10000.0
	assert l2 <= l3