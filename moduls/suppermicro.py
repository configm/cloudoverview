import os
import json
import yaml



class Suppermicro(object):
	"""
	Evry object is Microservice
	so it need:
	pod (yaml)
	Docker files
	"""
	def __init__(self, name):
		pass
	def push(self):
		pass
	def gui(self):
		pass


class Project(Suppermicro):
	def __init__(self, name):
		if name in os.listdir('data','projects'):
			self = self.lowde_from_pickel_file(name)
		pass

	def lowde_from_pickel_file(sels,name):
		pass



class application(object):
	def __init__(self):
		pass