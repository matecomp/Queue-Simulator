# -*- coding: utf-8 -*-
import numpy as np



class Server(object):
	"""docstring for Server"""
	def __init__(self, mu=1.0, start_time=0.0):
		super(Server, self).__init__()
		self.__is_empty = True
		self.__mu = mu
		self.__start_time = start_time
		self.__last_service = start_time
		self.__params = self.make_params_dict()

	def make_params_dict(self):
		return dict(zip(
			["is_empty","mu","start_time","last_service"],
			[self.__is_empty,self.__mu, self.__start_time, self.__last_service]
		))

	#Retorna os parâmetros da classe
	def get_params(self):
		return self.__params

	#Avisa quando o servitor está ocupado ou não
	def is_empty(self):
		return self.__params["is_empty"]

	#Este método executará o serviço e retornará o tempo de serviço
	def do_service(self, start_time):
		#Caso o servidor esteja ocupado, não faça o serviço
		assert self.__params["is_empty"]

		beta = 1 / self.__params["mu"]
		self.__params["is_empty"] = False
		self.__params["start_time"] = start_time
		self.__params["last_service"] = np.random.exponential(scale=beta, size=None)
		return self.__params["last_service"]

	#Dado o tempo atual da simulação, este método atualiza o servidor
	def update(self, time):
		self.__params["is_empty"] = time - self.__params["start_time"] >= self.__params["last_service"]


if __name__ == '__main__':
	print("Ops...")