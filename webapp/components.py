import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utilities import get_markdown, get_credentials, get_map_rating_data

CREDENTIAL_FILE = '../credentials/credentials.txt'
MAP_RATING_DATA_FILE = '../model/map_ratings_data.csv'
CREDENTIALS = get_credentials(CREDENTIAL_FILE)
COLORSCALE = [[0, 'rgb(242,78,78)'],
	[0.25, 'rgb(247,129,69)'],
	[0.50, 'rgb(242,78,78)'],
	[0.75, 'rgb(160,176,70)'],
	[1.00, 'rgb(17,100,77)']]

# TEXT SECTIONS
sections = get_markdown('text.md')
markdown = [dcc.Markdown(sec) for sec in sections]

# TRENDS MODULE
map_rating_data, lat_avg, lon_avg = get_map_rating_data(
	MAP_RATING_DATA_FILE)

trends_module = html.Div(id='trend-module', children=[
	dcc.Graph(
		id='map-rating-data',
		figure=go.Figure(
			data=[
				go.Scattermapbox(
					lat=map_rating_data['lat'],
					lon=map_rating_data['lon'],
					mode='markers',
					marker=go.Marker(
						color=map_rating_data['color'],
						colorscale=COLORSCALE,
						size=map_rating_data['size']
					)
				)
			],
			layout=go.Layout(
				title='Geographic Visualization of Volume and Ratings',
				autosize=True,
				hovermode='closest',
				mapbox=dict(
					accesstoken=CREDENTIALS['mapbox'],
					bearing=0,
					pitch=0,
					center=dict(
            			lat=lat_avg,
            			lon=lon_avg
            		),
					zoom=10,
					style='light'
				)
			)
		),
		style={'width': '100%', 'height': 500}
	),
	dcc.Graph(
		id='map-price-data',
		figure=go.Figure(
			data=[
				go.Mesh3d(
					x=map_rating_data['lon'],
					y=map_rating_data['lat'],
					z=map_rating_data['price'],
					color='90EE90',
					opacity=0.50
				)	
			],
			layout=go.Layout(
				title='Price as a function of Position'
			)
		),
		style={'width': '100%', 'height': 500}
	)
])

# PRICE MODULE
price_module = html.Div(id='price-module', children=[
	dcc.Input(
		id='long1',
		placeholder='latitude',
		type='text',
		value=''),
	dcc.Input(
		id='lat1',
		placeholder='longitude',
		type='text',
		value=''),
	html.Button('Submit', id='price-button')
])

# BOOKING MODULE
booking_module = html.Div(id='booking-module', children=[
	dcc.Input(
		id='long2',
		placeholder='latitude',
		type='text',
		value=''),
	dcc.Input(
		id='lat2',
		placeholder='longitude',
		type='text',
		value=''),
	html.Button('Submit', id='price-button')
])

