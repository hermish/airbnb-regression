import inspect
import pandas as pd

def automain(function):
    locale = inspect.stack()[1][0].f_locals
    module = locale.get("__name__", None)
    if module == "__main__":
        locale[function.__name__] = function
        function()
    return function

def get_credentials(filename):
	with open(filename) as file:
		data = file.readlines()
		pairs = [pair.split('|') for pair in data]
		credentials = {source: value for source, value in pairs}
		return credentials

def get_markdown(filename):
	with open(filename) as file:
		sections = []
		data = file.read().split('\n---\n')
		for section in data:
			sections.append(section)
		return sections

def get_map_rating_data(filename):
	data_frame = pd.read_csv(filename)
	return data_frame, data_frame['lat'].mean(),\
		data_frame['lon'].mean()