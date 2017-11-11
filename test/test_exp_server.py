# test_exp_server.py

# -*- coding: utf-8 -*-
from servers.exp_server import Server
import pytest

init_dict = dict(zip(
					["is_empty","mu","start_time","service"],
					[True, 1.0, 0.0, 0.0]
				))

def test_init():
	server = Server()
	print(server.get_params())
	assert server.get_params() == init_dict

def test_do_service():
	server = Server()
	time = server.do_service(0)
	assert server.is_empty() == False

def test_update_equal():
	server = Server()
	time = server.do_service(0)
	server.update(time)
	assert server.is_empty() == True

def test_update_greather():
	server = Server()
	time = server.do_service(0)
	server.update(time+1)
	assert server.is_empty() == True

def test_update_lower():
	server = Server()
	time = server.do_service(0)
	server.update(time-1)
	assert server.is_empty() == False