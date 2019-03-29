import os
import json
import redis
import pickle

def get_list_of(type_of):
	os.makedirs(os.path.join('data'), exist_ok=True)
	os.makedirs(os.path.join('data', 'micsrv'), exist_ok=True)
	os.makedirs(os.path.join('data', 'micsrv', type_of), exist_ok=True)
	return os.listdir(os.path.join('data', 'micsrv', type_of))

def get_project_dict(pname):
	proj_fl = open(os.path.join('data', 'micsrv', 'project', pname), 'rb')
	object_to_return = pickle.load(proj_fl).__dict__
	return object_to_return

def vcs_in_place(vcs_path,vcs):
	print(vcs_path + vcs)
	return True

class Micsrv(object):
	"""
	Evry object is Microservice
	so it need:
	pod (yaml)
	Docker files
	"""
	def __init__(self,obj_type , name):
		self.name = name
		pass
	def load(self):
		pass
	def save(self):
		pass
	def gui(self):
		pass
	def get_list(self):
		return (os.listdir(os.path.join('data', 'micsrv', self.type_of())))

	def deploy(self):
		pass


class Project(Micsrv):
	def __init__(self, name):
		self.name = name
		self.obj_type = 'project'

	def create(self, vcs_type, vcs_path): # a new
		self.vcs_type = vcs_type
		self.vcs_path = vcs_path
		self.obj_type = 'project'
#		self.look_for_jenkins()
		pr_file = open(os.path.join('data', 'micsrv', self.obj_type, self.name), 'wb')
		pickle.dump(self, pr_file, pickle.HIGHEST_PROTOCOL)
		pr_file.close()


	def load(self, vcs_type, vcs_path): # open an excisting project
		self.vcs_type = vcs_type
		self.vcs_path = vcs_path
		self.obj_type = 'project'
		self.look_for_jenkins()


	def lowde_from_pickel_file(sels,name):
		pass



class application(object):
	def __init__(self, name):
		pass