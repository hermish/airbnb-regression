import dash
import dash_core_components as dcc
import dash_html_components as html
from utilities import automain, get_credentials, get_markdown

TEXT_FILE = 'text.md'
CREDENTIAL_FILE = '../credentials/credentials.txt'
CSS_URL = 'https://www.ocf.berkeley.edu/~hermish/files/scripts/test.css'

app = dash.Dash()
credentials = get_credentials(CREDENTIAL_FILE)
# List of sections as markdown objects
markdown = get_markdown(TEXT_FILE)
app.layout = html.Div(children=[
	markdown[0],
	markdown[1],
	markdown[2]
])

app.css.append_css({"external_url": CSS_URL})

@automain
def main():
	app.run_server(debug=True)