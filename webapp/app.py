import dash
import dash_core_components as dcc
import dash_html_components as html

import components
from utilities import automain

# CONSTANTS
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


# RUN
@automain
def main():
	app.run_server(debug=True)