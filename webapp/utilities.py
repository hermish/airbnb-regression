import inspect
import pandas as pd
import numpy as np


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


def get_map_revenue_data(filename):
	data_frame = pd.read_csv(filename)
	return data_frame
	return get_model(filename)


def get_model(filename):
	return get_map_revenue_data(filename)


def predict_rev(lon, lat, model):
	distances = []
	for index, row in model.iterrows():
		dist = (lon - row['lon']) ** 2 + (lat - row['lat']) ** 2
		if not dist:
			return row['rev']
		distances.append(1 / dist)
	weights = [val / sum(distances) for val in distances]
	rev = 0
	for index, row in model.iterrows():
		rev += weights[index] * row['rev']
	return rev


def find_opt_price(lon, lat, model):
	distances = []
	for index, row in model.iterrows():
		dist = (lon - row['lon']) ** 2 + (lat - row['lat']) ** 2
		if not dist:
			return row['price']
		distances.append(1 / dist)
	weights = [val / sum(distances) for val in distances]
	price = 0
	for index, row in model.iterrows():
		price += weights[index] * row['price']
	return price
