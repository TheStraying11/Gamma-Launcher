#!/usr/bin/python3
from PyQt5.QtWidgets import *
import json

app = QApplication(['Gamma Launcher'])

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

class init_json: #division class for initialising modpack_list.json
	with open('modpack_list.json') as json_file:
		modpack_list = json.load(json_file)
	json_file.close()
	with open('modpack_list.json', 'w') as outfile:
		modpack_list['modpacks'].sort(key=lambda x: x[0]["name"].lower())
		json.dump(modpack_list, outfile, indent=4)
	outfile.close()
	with open('modpack_list.json') as json_file:
		modpack_list = json.load(json_file)
	modpack_menu = QListWidget()

	for i in enumerate(modpack_list['modpacks']):
		modpack_menu.addItem(i[1][0]["name"])

class windows:

	class system: #division class for the first window where system type is defined
		system_definition_window = QWidget()

		layout_0 = QVBoxLayout()

		system_definition_input = QComboBox()
		system_definition_input.addItems(["Linux (Standalone)","Linux (Steam)", "MacOS (Standalone)","MacOS (Steam)", "Windows (Standalone)", "Windows (Steam)"])

		submit_button_0 = QPushButton('Submit')
		submit_button_0.clicked.connect(lambda: functions.submit_0())

		layout_0.addWidget(system_definition_input)
		layout_0.addWidget(submit_button_0)

		system_definition_window.setLayout(layout_0)
		system_definition_window.setGeometry(0,0,250,0)
		system_definition_window.show()

	class folder: #division class for 2nd window where folder path is defined
		folder_definition_window = QWidget()

		layout_1 = QVBoxLayout()

		data_folder_label = QLabel('Enter path to your factorio data folder. (where your mods go)')

		data_folder_input = QLineEdit()
		data_folder_input.setPlaceholderText('Enter path to your factorio data folder. (where your mods go)')
		browse_data = QPushButton('Browse')
		browse_data.clicked.connect(lambda: functions.browse_0())

		application_folder_label = QLabel("Enter path to your factorio application folder. (where the 'bin' folder is)")

		application_folder_input = QLineEdit()
		application_folder_input.setPlaceholderText("Enter path to your factorio application folder. (where the 'bin' folder is)")
		browse_application = QPushButton('Browse')
		browse_application.clicked.connect(lambda: functions.browse_1())

		submit_button_1 = QPushButton('Submit')
		submit_button_1.clicked.connect(lambda: functions.submit_1())

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

	class main: #division class for main window with all modpacks listed
		modpack_menu = init_json.modpack_menu

		main_window = QWidget()

		layout_2 = QHBoxLayout()

		add_button = QPushButton('Add from file')
		add_button.clicked.connect(lambda: functions.add_list())

		modpack_menu.itemClicked.connect(lambda: functions.list_click())

		list_vertical = QVBoxLayout()
		list_vertical.addWidget(modpack_menu)

		add_button_vertical = QVBoxLayout()
		add_button_vertical.addWidget(add_button)

		layout_2.addLayout(list_vertical)
		layout_2.addLayout(add_button_vertical)

		main_window.setLayout(layout_2)
		main_window.setGeometry(0,0,494,0)

	class add: #division class for 'add modpack from file' window
		add_window = QWidget()

		modpack_name_label = QLabel('Enter the name of your modpack')
		modpack_json_label = QLabel('Enter the path to your modpack.json')
		modpack_name_input = QLineEdit()
		modpack_json_input = QLineEdit()
		browse_json = QPushButton('Browse')
		browse_json.clicked.connect(lambda: functions.browse_2())
		submit_button_2 = QPushButton('Submit')
		submit_button_2.clicked.connect(lambda: functions.submit_2())

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

	class launch: #division class for the launch window
		launch_window = QWidget()

		layout_4 = QVBoxLayout()

class functions:
	def browse_0(): #browse button for data folder text box
		windows.folder.data_folder_input.setText(str(QFileDialog.getExistingDirectory()))

	def browse_1(): #browse button for application folder text box
		windows.folder.application_folder_input.setText(str(QFileDialog.getExistingDirectory()))

	def browse_2(): #browse button for json file text box
		windows.add.modpack_json_input.setText(QFileDialog.getOpenFileName()[0])

	def submit_0(): #submit button for system definition window
		wf = windows.folder

		windows.system.system_definition_window.hide()

		wf.data_folder_input.setText(path[windows.system.system_definition_input.currentText()][0])
		wf.application_folder_input.setText(path[windows.system.system_definition_input.currentText()][1])

		wf.folder_definition_window.show()

	def submit_1(): #submit button for folder definition window
		wf = windows.folder
		wf.folder_definition_window.hide()
		wf.application_folder_path = windows.folder.application_folder_input.text()
		wf.data_folder_path = windows.folder.data_folder_input.text()
		windows.main.main_window.show()

		print('data folder is '+wf.data_folder_path)
		print('application folder is '+wf.application_folder_path)

	def submit_2(): #submit button for 'add from file' window
		wa = windows.add
		modpack_list = init_json.modpack_list
		json_file = init_json.json_file
		modpack_menu = init_json.modpack_menu
		
		latest_modpack_name = wa.modpack_name_input.text()
		latest_modpack_json = wa.modpack_json_input.text()
		
		wa.modpack_json_input.setText('')
		wa.modpack_name_input.setText('')
		wa.add_window.hide()

		json_file.close()

		with open('modpack_list.json') as json_file:
			modpack_list = json.load(json_file)
		
		if ((latest_modpack_name and latest_modpack_json) != ''):
			modpack_list['modpacks'].append([{'name' : latest_modpack_name}, {'json' : latest_modpack_json}])
		json_file.close()
		
		with open('modpack_list.json', 'w') as outfile:
			modpack_list['modpacks'].sort(key=lambda x: x[0]["name"].lower())
			json.dump(modpack_list, outfile, indent=4)
		outfile.close()
		
		with open('modpack_list.json') as json_file:
			modpack_list = json.load(json_file)
		modpack_menu.clear()
		
		for i in enumerate(modpack_list['modpacks']):
			modpack_menu.addItem(i[1][0]["name"])

	def add_list(): #'add from file' button
		windows.add.add_window.show()

	def list_click(): #function triggered when clicking on a list item
		windows.launch.launch_window.show()

app.exec()