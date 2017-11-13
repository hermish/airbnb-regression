import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utilities import get_markdown, get_credentials, get_map_rating_data, get_map_revenue_data


# CONSTANTS
CREDENTIAL_FILE = 'credentials/credentials.txt'
MAP_RATING_DATA_FILE = 'model/map_ratings_data.csv'
MAP_REVENUE_DATA_FILE = 'model/map_revenue_data.csv'
CREDENTIALS = get_credentials(CREDENTIAL_FILE)
COLORSCALE = [[0, 'rgb(242,78,78)'],
	[0.25, 'rgb(247,129,69)'],
	[0.50, 'rgb(242,78,78)'],
	[0.75, 'rgb(160,176,70)'],
	[1.00, 'rgb(17,100,77)']]
GREY = 'rgb(220,220,220)'
PANCAKE = [[0, 'rgb(255,255,255)'],
	[0.2, 'rgb(229,252,194)'],
	[0.4, 'rgb(157,224,173)'],
	[0.8, 'rgb(69,173,168)'],
	[0.8, 'rgb(84,121,128)'],
	[1.0, 'rgb(89,79,79)']]


# TEXT SECTIONS
sections = get_markdown('text.md')
markdown = [dcc.Markdown(sec) for sec in sections]


# TRENDS MODULE
map_rating_data, lat_avg, lon_avg = get_map_rating_data(
	MAP_RATING_DATA_FILE)
map_revenue_data = get_map_revenue_data(MAP_REVENUE_DATA_FILE)

trends_module = html.Div(
	id='trend-module', 
	style={'display': 'inline-block'},
	children=[
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
					go.Histogram2d(
					    x=map_rating_data['lon'],
					    y=map_rating_data['lat'],
					    z=map_rating_data['price'],
					    histfunc='avg',
					    colorscale=PANCAKE,
					)
				],
				layout=go.Layout(
					title='Price as a function of Position',
					xaxis=dict(
       					title='Longitude (deg)'
       				),
       				yaxis=dict(
       					title='Latitude (deg)'
       				)
				)
			),
			style={'width': '100%', 'height': 500}
		)
	]
)

# PRICE MODULE
price_module = html.Div(
	id='price-module',
	style={'display': 'inline-block',
		'position': 'relative',
		'left': '12.5%'},
	children=[
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
		html.Button('Submit', id='price-button'),
		html.Div(id='revenue-output'),
		dcc.Graph(
			id='map-revenue-data',
			figure=go.Figure(
				data=[
					go.Scatter3d(
						z=map_revenue_data['rev'],
						x=map_revenue_data['lon'],
						y=map_revenue_data['lat'],
						marker=dict(
							size=1,
							opacity=0.05,
							color=map_revenue_data['rev'],
							symbol='square',
							colorscale='Viridis'
						),
						connectgaps=True,
						projection=dict(
							x=dict(
								show=True,
								scale=5
							),
							y=dict(
								show=True,
								scale=5
							)
						),
						line=dict(
							color=GREY
						)
					)
				],
				layout=go.Layout(
					title='Revenue as a function of Position',
					xaxis=dict(
       					title='Longitude'
       				),
       				yaxis=dict(
       					title='Latitude'
       				)
				)
			),
			style={'width': '100%', 'height': 500}
		)
	]
)

# BOOKING MODULE
booking_module = html.Div(
	id='booking-module',
	style={'display': 'inline-block',
		'position': 'relative',
		'left': '12.5%'},
	children=[
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
		html.Button('Submit', id='booking-button'),
		html.Div(id='booking-output'),
		dcc.Graph(
			id='map-booking-data',
			figure=go.Figure(
				data=[
					go.Scatter(
						x=map_revenue_data['cost'],
						y=map_revenue_data['price'],
						mode = 'markers'
					)
				],
				layout=go.Layout(
					title='Overall Revenue and Price Curve',
					xaxis=dict(
        				range=[0, 500],
        				title='Price ($)'
    				),
       				yaxis=dict(
       					title='Revenue ($)'
       				)
				)
			),
			style={'width': '100%', 'height': 500}
		)
	]
)

