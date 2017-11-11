# main.py

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import collections as clt
from queues.exp_queue import Queue
from servers.exp_server import Server

time = 0
queue = Queue()
server = Server(mu=100)


if __name__ == '__main__':

	service_time = 0.0
	queue_size = list()
	#while(1):
	for i in range(100000):
		# Se o servidor estiver vazio, o cliente sairá 
		# instantaneamente da fila
		# Se o servidor estiver ocupado, vamos progredir o tempo
		# de serviço e atualizar o sistema após o tempo de serviço
		if server.is_empty() == True:
			client_time = queue.pop_fcfs()
			if client_time is None:
				queue.add_client()
				client_time = queue.pop_fcfs()
				service_time = server.do_service(client_time + time)
			else:
				service_time = server.do_service(time)
		else:
			time += service_time
			server.update(time)
			queue.update(time)
			queue_size.append(queue.get_len())

	plt.plot(range(len(queue_size)), queue_size)
	plt.show()
	print(queue_size[-1])