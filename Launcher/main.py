#!/usr/bin/python3
from PyQt5.QtWidgets import *
import json

global json_file
with open('modpack_list.json') as json_file:
	global modpack_list
	modpack_list = json.load(json_file)

#path['system'][0] is default data folder
#path['system'][1] is default application folder
path = {
    'Linux (Standalone)' : ['~/.Factorio','~/.Factorio'],
    'Linux (Steam)' : ['~/.Factorio','~/.local/share/Steam/steamapps/common/Factorio'],
    'MacOS (Standalone)' : ['~/Library/Application Support/factorio','/Applications/factorio.app/Contents'],
    'MacOS (Steam)' : ['~/Library/Application Support/factorio','~/Library/Application Support/Steam/steamapps/common/Factorio/factorio.app/Contents'],
    'Windows (Standalone)' : [r"%appdata%\Factorio",r"C:\Program Files\Factorio"],
    'Windows (Steam)' : [r"%appdata%\Factorio",r"C:\Program Files (x86)\Steam\steamapps\common\Factorio"]
}

app = QApplication(['Gamma Launcher'])

system_definition_window = QWidget()

layout_0 = QVBoxLayout()

system_definition_input = QComboBox()
system_definition_input.addItems(["Linux (Standalone)","Linux (Steam)", "MacOS (Standalone)","MacOS (Steam)", "Windows (Standalone)", "Windows (Steam)"])

submit_button_0 = QPushButton('Submit')
submit_button_0.clicked.connect(lambda: submit_0())

layout_0.addWidget(system_definition_input)
layout_0.addWidget(submit_button_0)

system_definition_window.setLayout(layout_0)
system_definition_window.setGeometry(0,0,250,0)
system_definition_window.show()

folder_definition_window = QWidget()

layout_1 = QVBoxLayout()

data_folder_label = QLabel('Enter path to your factorio data folder. (where your mods go)')

data_folder_input = QLineEdit()
data_folder_input.setPlaceholderText('Enter path to your factorio data folder. (where your mods go)')
browse_data = QPushButton('Browse')
browse_data.clicked.connect(lambda: browse_0())

application_folder_label = QLabel("Enter path to your factorio application folder. (where the 'bin' folder is)")

application_folder_input = QLineEdit()
application_folder_input.setPlaceholderText("Enter path to your factorio application folder. (where the 'bin' folder is)")
browse_application = QPushButton('Browse')
browse_application.clicked.connect(lambda: browse_1())

submit_button_1 = QPushButton('Submit')
submit_button_1.clicked.connect(lambda: submit_1())

default_continue_label = QLabel("If you don't know what this means, the defaults are probably fine.")

data_group = QHBoxLayout()
data_group.addWidget(data_folder_input)
data_group.addWidget(browse_data)

application_group = QHBoxLayout()
application_group.addWidget(application_folder_input)
application_group.addWidget(browse_application)

layout_1.addWidget(data_folder_label)
layout_1.addLayout(data_group)
layout_1.addWidget(application_folder_label)
layout_1.addLayout(application_group)
layout_1.addWidget(default_continue_label)
layout_1.addWidget(submit_button_1)

folder_definition_window.setLayout(layout_1)
folder_definition_window.setGeometry(0,0,494,0)

main_window = QWidget()

layout_2 = QHBoxLayout()

modpack_menu = QListWidget()
add_button = QPushButton('Add from file')
add_button.clicked.connect(lambda: add_list())

list_vertical = QVBoxLayout()
list_vertical.addWidget(modpack_menu)

add_button_vertical = QVBoxLayout()
add_button_vertical.addWidget(add_button)


layout_2.addLayout(list_vertical)
layout_2.addLayout(add_button_vertical)

main_window.setLayout(layout_2)
main_window.setGeometry(0,0,494,0)

add_window = QWidget()

modpack_name_label = QLabel('Enter the name of your modpack')
modpack_json_label = QLabel('Enter the path to your modpack.json')
modpack_name_input = QLineEdit()
modpack_json_input = QLineEdit()
browse_json = QPushButton('Browse')
browse_json.clicked.connect(lambda: browse_2())
submit_button_2 = QPushButton('Submit')
submit_button_2.clicked.connect(lambda: submit_2())



json_group = QHBoxLayout()
json_group.addWidget(modpack_json_input)
json_group.addWidget(browse_json)

layout_3 = QVBoxLayout()
layout_3.addWidget(modpack_name_label)
layout_3.addWidget(modpack_name_input)
layout_3.addWidget(modpack_json_label)
layout_3.addLayout(json_group)
layout_3.addWidget(submit_button_2)


add_window.setLayout(layout_3)
add_window.setGeometry(0,0,550,0)

def browse_0():
	data_folder_input.setText(str(QFileDialog.getExistingDirectory()))

def browse_1():
	application_folder_input.setText(str(QFileDialog.getExistingDirectory()))

def browse_2():
	modpack_json_input.setText(QFileDialog.getOpenFileName()[0])

def submit_0():
	system_definition_window.hide()
	data_folder_input.setText(path[system_definition_input.currentText()][0])
	application_folder_input.setText(path[system_definition_input.currentText()][1])
	folder_definition_window.show()

def submit_1():
	folder_definition_window.hide()
	application_folder_path = application_folder_input.text()
	data_folder_path = data_folder_input.text()
	main_window.show()
	print('data folder is '+data_folder_path)
	print('application folder is '+application_folder_path)

def submit_2():
	new_modpack_name = modpack_name_input
	new_modpack_json = modpack_json_input
	modpack_json_input.setText('')
	modpack_name_input.setText('')
	add_window.hide()
	global modpack_list
	global json_file
	modpack_list['modpacks'].append({new_modpack_name : new_modpack_json})
	json_file.close()
	with open('modpack_list.json', 'w') as outfile:
		json.dump(modpack_list, outfile)
	outfile.close()
	with open('modpack_list.json') as json_file:
		modpack_list = json.load(json_file)


def add_list():
	add_window.show()

app.exec()
