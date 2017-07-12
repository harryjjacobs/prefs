PREFERENCES_PATH = 'preferences'
import os.path

def add(name, value, overwite_existing=False):
	if not path.exists(PREFERENCES_PATH):
        	os.makedirs(PREFERENCES_PATH)
	if path.isfile(path.join(PREFERENCES_PATH, name)) and not overwite_existing:
		raise Exception('Preference already exists', '{0} has already been added. If you wish to overwrite it call with overwiteExisting=True or use the prefs.update method'.format(name))
	else:
		_save_to_file(path.join(PREFERENCES_PATH, name), value)

def remove(name):
	os.remove(path.join(PREFERENCES_PATH, name))
		
def get(name):
	return _try_load_from_file(path.join(PREFERENCES_PATH, name))
	
def update(name, value, throw):
	add(name, value, True)

def _try_load_from_file(name):
	if path.isfile(name):
		with open(name, 'r') as f:
			return f.read()
	else:
		raise Exception('Preference not found', '{0} has not been saved'.format(name))

def _save_to_file(name, value):
	with open(name, 'w+') as f:
		f.write(value)
