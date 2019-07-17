import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

import components


EXTERNAL_CSS = ['https://www.ocf.berkeley.edu/~hermish/files/scripts/core.css',
    'https://www.ocf.berkeley.edu/~hermish/files/scripts/test.css']


app = dash.Dash(__name__, external_stylesheets=EXTERNAL_CSS)
app.layout = html.Div(children=[
    components.markdown_modules[0],
    components.data_module,
    components.markdown_modules[1],
    components.prediction_module,
    components.markdown_modules[2],
    components.regression_module
])


current_classifier = lambda test: test


@app.callback(Output('data-graph-div', 'children'),
              [Input('drop-select-color', 'value'),
               Input('drop-select-size', 'value')])
def update_data_module(color, size):
    return components.update_data_module(color, size)


@app.callback(Output('slider-k', 'disabled'),
              [Input('drop-select-algorithm', 'value')])
def disable_slider_k(algorithm):
    return algorithm != 'knn'


@app.callback(Output('slider-d', 'disabled'),
              [Input('drop-select-algorithm', 'value')])
def disable_slider_d(algorithm):
    return algorithm != 'linear'


@app.callback(Output('drop-select-kernel', 'disabled'),
              [Input('drop-select-algorithm', 'value')])
def disable_drop_kernel(algorithm):
    return algorithm != 'svm'


@app.callback(Output('regression-graph-div', 'children'),
              [Input('drop-select-algorithm', 'value'),
               Input('slider-k', 'value'),
               Input('slider-d', 'value'),
               Input('drop-select-kernel', 'value')])
def update_regression_module(algorithm, k, degree, kernel):
    global current_classifier
    current_classifier, output = components.update_regression_module(
        algorithm, 5 * k + 1, degree, kernel)
    return output


@app.callback(Output('prediction-text', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('latitude-input', 'value'),
               State('longitude-input', 'value')])
def update_output(_, latitude, longitude):
    try:
        latitude, longitude = float(latitude), float(longitude)
    except ValueError:
        return 'Please enter a valid number!'
    prediction = current_classifier([[latitude, longitude]])
    prediction = prediction[0]
    return 'The estimated price for this location is ${:.2f}'.format(prediction)


if __name__ == '__main__':
    app.run_server(debug=False)
