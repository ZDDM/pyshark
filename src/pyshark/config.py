import pyshark
import py
import os

CONFIG_PATH = os.path.join(os.path.dirname(pyshark.__file__), 'config.ini')

def get_config():
	if os.path.isfile(CONFIG_PATH):
		return py.iniconfig.IniConfig(CONFIG_PATH)
	else:
		return None
