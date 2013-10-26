"""
helper.py has to be located in the same directory
as manage.py in the Django app.

@author: 'Toni Sucic'
"""

import os
import os.path

class WrongDirectoryException(Exception):
	def __init__(self):
		super(WrongDirectoryException,
			self).__init__('manage.py was not found in this directory.')

def _is_managepy_in_this_dir():
	managepy_found = False
	files_by_name_in_this_dir = os.listdir(os.getcwd())
	for filename in files_by_name_in_this_dir:
		if filename.endswith('.py'):
			if filename == 'manage.py':
				managepy_found = True
		else:
			continue
	return managepy_found

# Raises exception if manage.py isn't located in this directory
def _check_if_managepy_is_in_this_dir():
	if not _is_managepy_in_this_dir():
		raise WrongDirectoryException()

# This function gives the relative path to the base directory in the
# Django app. For instance, get_relative_path_to_base_dir('static/') might yield
# 'C:/Users/Username/Desktop/django project/blog/static' on Windows.
# In this case 'blog/' is the base directory.
def get_relative_path_to_base_dir(path):
	return '{base_dir}/{path}'.format(base_dir=os.getcwd(), path=path)

# This gets called once this module is imported.
_check_if_managepy_is_in_this_dir()