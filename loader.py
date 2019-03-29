#!/usr/local/bin/python
import os
import json
from flask import Flask, render_template, request, flash, send_from_directory
from colorama import Fore, Back, Style, init
init()
import logging
from termcolor import *

import requests
from moduls.micsrv import *
from moduls.micsrv import Project
from requests import get
import requests
import config

app = Flask(__name__)
app.debug = config.debug
app.secret_key = config.secret_key

SITE_NAME = 'http://ec2-35-183-235-130.ca-central-1.compute.amazonaws.com:8000/'



@app.route('/cm', methods=['POST', 'GET'])
def cm():
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	#response = requests.get(SITE_NAME, headers=headers)
	return render_template('index.html')



@app.route('/icons/aws/<type_dir>/<file_name>')
def custom_static(type_dir, file_name):
	return send_from_directory(os.path.join('static', 'icons', 'aws', type_dir), file_name)




@app.route('/starttocolectcloudmapper', methods=['POST', 'GET'])
def starttocolectcloudmapper():
	json_to_send = request.get_json()
	print(json_to_send)
	flash(str(request.form))
	return projects()

	

@app.route('/crete_project', methods=['POST', 'GET'])
def crete_project():
	print(request.form)
	pname = request.form['pname']
	vcs_type = request.form['vcs_type']
	vcs_path = request.form['vcs_path']
	if pname == '':
		flash('Can not create new a project (no name is given)')
	elif vcs_type == '':
		flash('Can not create new a project (no VCS type is given)')
	elif vcs_path == '' :
		flash('Can not create new a project (no VCS Path is given)')
	else:
		new_project = Project(pname)
		new_project.create( vcs_type, vcs_path)
		return
	return projects()

@app.route('/projects', methods=['POST', 'GET'])
def projects():
	projects_list = get_list_of('project')
	return render_template('projects.html', projects_list=projects_list)


@app.route('/load_project/<project_name>/', methods=['POST', 'GET'])
def load_project(project_name):
	project_form = get_project_dict(project_name)
	return render_template('load_project.html', project_form=project_form)

@app.route('/addcloudmapper/')
def addcloudmapper():
	projects_list = []
	for project_file in get_list_of('project'):
		projects_list.append(project_file)
	return render_template('addcloudmapper.html')


@app.route('/containers', methods=['POST', 'GET'])
def containers():
	containers_list = os.listdir(os.path.join('data', 'containers'))
	return render_template('containers.html', containers_list=containers_list)




@app.route('/jenkins', methods=['POST', 'GET'])
def jenkinss():
	jenkins_list = os.listdir(os.path.join('data', 'jenkins'))
	return render_template('jenkins.html', jenkins_list=jenkins_list)


@app.route('/new_project', methods=['POST', 'GET'])
def new_project():
	return render_template('new_project.html')


@app.route('/open_project', methods=['POST', 'GET'])
def open_project(project_name=None):
	try:
		cprint('project_name', 'green')
		cprint(request.form['project_name'], 'green')
		if project_name == None:
			project_name = request.form['project_name']
			cprint(project_name, 'green')
		file_to_create = project_name
	except:
		cprint(project_name, 'red')
		pass
	file_to_create_hendler = open(os.path.join('data', 'projects', str(project_name)), 'r')
	project_as_text = file_to_create_hendler.read()
	file_to_create_hendler.close()
	projects_list = []
	for project_file in get_list_of('projects'):
		projects_list.append(project_file)
	option_selection_list = json.dumps(project_as_text)
	option_list=json.loads(open(os.path.join('data', 'option', 'option_list.json'), 'r').read())
	print('project_as_text=' + str(project_as_text) + ', projects_list=' + str(projects_list) + ', option_selection_list=' + str(option_selection_list) + ', option_list=' + str(option_list), 'green')
	return render_template('open_project.html', project_as_text=project_as_text, projects_list=projects_list, option_selection_list=option_selection_list, option_list=option_list)




@app.route('/')
def Hiall():
	projects_list = []
	for project_file in get_list_of('project'):
		projects_list.append(project_file)
	return render_template('home.html')



if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	try :
		pid_file = open('pid', 'r')
		os.kill(int(pid_file.read()))
		pid_file.close()
	except:
		logging.warning('No service pid file or no service with pid in this file ... \n in any way the app can run :) for now ')
		pass
	pid_file = open('pid', 'w')
	pid_file.write(str(os.getpid()))
	pid_file.close()
	app.run(debug=config.debug, host=config.host_open, port=config.port)
