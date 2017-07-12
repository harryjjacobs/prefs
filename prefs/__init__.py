PREFERENCES_PATH = 'preferences'
import os

def add(name, value, overwite_existing=False):
	if not os.path.exists(PREFERENCES_PATH):
        	os.makedirs(PREFERENCES_PATH)
	if os.path.isfile(os.path.join(PREFERENCES_PATH, name)) and not overwite_existing:
		raise Exception('Preference already exists', '{0} has already been added. If you wish to overwrite it call with overwiteExisting=True or use the prefs.update method'.format(name))
	else:
		_save_to_file(os.path.join(PREFERENCES_PATH, name), value)

def remove(name):
	if os.path.exists(os.path.join(PREFERENCES_PATH, name)):
		os.remove(os.path.join(PREFERENCES_PATH, name))
	else:
		raise Exception('Could not remove preference', 'No preference with name {0} was found'.format(name))
		
def get(name):
	return _try_load_from_file(path.join(PREFERENCES_PATH, name))
	
def update(name, value, create_if_nonexistent=False):
	if os.path.exists(os.path.join(PREFERENCES_PATH, name)) or create_if_nonexistent:
		add(name, value, True)
	else:
		raise Exception('Could not update preference', 'Preference does not exist and create_if_nonexistent set to False. Set it to True if you want to create the preference or use the add method to add it first.')



def _try_load_from_file(name):
	if os.path.isfile(name):
		with open(name, 'r') as f:
			return f.read()
	else:
		raise Exception('Preference not found', '{0} has not been saved'.format(name))

def _save_to_file(name, value):
	with open(name, 'w+') as f:
		f.write(value)
