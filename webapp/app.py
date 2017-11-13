import dash
import dash_core_components as dcc
import dash_html_components as html

import components
from utilities import automain, predict_rev, find_opt_price, get_model


# CONSTANTS
MODEL_FILE = '../model/model.csv'
MODEL = get_model(MODEL_FILE)
CSS_URLS = ['https://www.ocf.berkeley.edu/~hermish/files/scripts/core.css',
	'https://www.ocf.berkeley.edu/~hermish/files/scripts/test.css']

# APP & CREDENTIALS
app = dash.Dash()
for file in CSS_URLS:
	app.css.append_css({"external_url": file})


# APP STRUCTURE
app.layout = html.Div(children=[
	components.markdown[0],
	components.trends_module,
	components.markdown[1],
	components.price_module,
	components.markdown[2],
	components.booking_module
])


# CALLBACKS
@app.callback(
	dash.dependencies.Output('revenue-output', 'children'),
	[dash.dependencies.Input('price-button', 'n_clicks')],
	[dash.dependencies.State('long1', 'value'),
	dash.dependencies.State('lat1', 'value')])
def update_output(n_clicks, longitude, latitude):
	try:
		lon = int(longitude)
		lat = int(latitude)
	except ValueError:
		return 'Please enter a valid number!'
	predicted_rev = predict_rev(lon, lat, MODEL)
	return 'The expected revenue for this location is ${}'.format(predicted_rev)

@app.callback(
	dash.dependencies.Output('booking-output', 'children'),
	[dash.dependencies.Input('booking-button', 'n_clicks')],
	[dash.dependencies.State('long2', 'value'),
	dash.dependencies.State('lat2', 'value')])
def update_output(n_clicks, longitude, latitude):
	try:
		lon = int(longitude)
		lat = int(latitude)
	except ValueError:
		return 'Please enter a valid number!'
	optimal_price = find_opt_price(lon, lat, MODEL)
	return 'The optimal price for this location is ${}'.format(optimal_price)
		

# RUN
@automain
def main():
	app.run_server(debug=True)