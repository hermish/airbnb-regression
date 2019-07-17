import json
import pandas as pd
import numpy as np

# STRINGS
credential_path = 'static/credentials.json'
data_path = 'static/listings.csv'
markdown_path = 'static/text.md'
markdown_divider = '\n---\n'

with open(credential_path) as file:
    credentials = json.load(file)
with open(markdown_path) as file:
    markdown = file.read()

# COLORS
color_scales = {
    'default': [
        [0, 'rgb(243,166,145)'],
        [0.25, 'rgb(249,216,158)'],
        [0.5, 'rgb(255,251,173)'],
        [1.00, 'rgb(193,228,158)']
    ],
    'red_blue': [
        [0.0, 'rgb(178,24,43)'],
        [0.125, 'rgb(214,96,77)'],
        [0.25, 'rgb(244,165,130)'],
        [0.375, 'rgb(253,219,199)'],
        [0.5, 'rgb(247,247,247)'],
        [0.625, 'rgb(209,229,240)'],
        [0.75, 'rgb(146,197,222)'],
        [0.875, 'rgb(67,147,195)'],
        [1.0, 'rgb(33,102,172)']
    ]
}

colors = {
    'blue': 'rgb(161,208,251)',
    'gray': 'rgb(220,220,220)'
}

# DATA PRE-PROCESSING
data = pd.read_csv(data_path)
average_lat = data['latitude'].mean()
average_lon = data['longitude'].mean()

ordered = {
    'price': np.argsort(data['price']),
    'reviews': np.argsort(data['number_of_reviews']),
    'availability': np.argsort(data['availability_365'])
}

training = np.array(data[['latitude', 'longitude']])
labels = np.array(data['price'])
