import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

import constants

# MARKDOWN MODULES
_sections = constants.markdown.split(constants.markdown_divider)
markdown_modules = [dcc.Markdown(sec) for sec in _sections]

# DATA MODULE
data_module = html.Div(
    id='data-module',
    children=[
        html.Div(
            id='data-options',
            children=[
                html.Div(
                    style={
                        'width': '30%',
                        'display': 'inline-block',
                        'margin-left': '20%'
                    },
                    children=[
                        html.Label(
                            htmlFor='drop-select-color',
                            children='Color Feature'
                        ),
                        dcc.Dropdown(
                            id='drop-select-color',
                            options=[
                                {'label': 'Number of Reviews', 'value': 'reviews'},
                                {'label': 'Price per Night', 'value': 'price'},
                                {'label': 'Availability', 'value': 'availability'}
                            ],
                            value='price',
                            clearable=True,
                            searchable=False
                        )
                    ]
                ),
                html.Div(
                    style={
                        'width': '30%',
                        'display': 'inline-block',
                        'margin-right': '20%'
                    },
                    children=[
                        html.Label(
                            htmlFor='drop-select-size',
                            style={'display': 'block'},
                            children='Size Feature'
                        ),
                        dcc.Dropdown(
                            id='drop-select-size',
                            options=[
                                {'label': 'Number of Reviews', 'value': 'reviews'},
                                {'label': 'Price per Night', 'value': 'price'},
                                {'label': 'Availability', 'value': 'availability'}
                            ],
                            clearable=True,
                            searchable=False
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id='data-graph-div'
        )
    ]
)


def update_data_module(color, size):
    length = len(constants.data)

    size_values = 5
    color_values = constants.colors['blue']
    if size is not None:
        size_values = constants.ordered[size] / length
        size_values = np.round(size_values * 10)
    if color is not None:
        color_values = constants.ordered[color] / length
        color_values = 1 - color_values if color == 'price' else color_values

    return dcc.Graph(
        id='data-graphs',
        figure=go.Figure(
            [
                go.Scattermapbox(
                    lat=constants.data['latitude'],
                    lon=constants.data['longitude'],
                    mode='markers',
                    marker=go.Marker(
                        color=color_values,
                        colorscale=constants.color_scales['default'],
                        size=size_values
                    ),
                    hoverinfo='none'
                )
            ],
            layout=go.Layout(
                title='Geographic Visualization',
                autosize=True,
                hovermode='closest',
                mapbox=dict(
                    accesstoken=constants.credentials['mapbox'],
                    bearing=0,
                    pitch=0,
                    center=dict(
                        lat=constants.average_lat,
                        lon=constants.average_lon
                    ),
                    zoom=10,
                    style='light'
                )
            )
        )
        # style={'width': '100%', 'height': 500}
    )


# REGRESSION MODULE
regression_module = html.Div(
    id='regression-module',
    children=[
        html.Div(
            id='regression-options',
            style={'padding-top': '10px', 'padding-bottom': '20px'},
            children=[
                html.Div(
                    style={
                        'width': '30%',
                        'display': 'inline-block',
                        'margin-left': '20%',
                        'padding-bottom': '5px'
                    },
                    children=[
                        html.Label(
                            htmlFor='drop-select-algorithm',
                            children='Algorithm'
                        ),
                        dcc.Dropdown(
                            id='drop-select-algorithm',
                            options=[
                                {'label': 'k-Nearest Neighbors', 'value': 'knn'},
                                {'label': 'Polynomial Regression', 'value': 'linear'},
                                {'label': 'SVM Regression', 'value': 'svm'}
                            ],
                            value='knn',
                            placeholder='Color',
                            clearable=False,
                            searchable=False
                        )
                    ]
                ),
                html.Div(
                    style={
                        'width': '30%',
                        'display': 'inline-block',
                        'margin-right': '20%'
                    },
                    children=[
                        html.Label(
                            htmlFor='drop-select-kernel',
                            children='Kernel'
                        ),
                        dcc.Dropdown(
                            id='drop-select-kernel',
                            options=[
                                {'label': 'Linear', 'value': 'linear'},
                                {'label': 'Polynomial (d = 3)',
                                 'value': 'poly'},
                                {'label': 'Radial Basis Function',
                                 'value': 'rbf'},
                            ],
                            value='linear',
                            clearable=False,
                            searchable=False
                        ),
                    ]
                ),
                html.Div(
                    style={
                        'width': '40%',
                        'display': 'inline-block',
                        'margin-right': '6.67%',
                        'margin-left': '3.33%'
                    },
                    children=[
                        html.Label(
                            htmlFor='slider-k',
                            children='Neighbors (k)'
                        ),
                        dcc.Slider(
                            id='slider-k',
                            min=0,
                            max=10,
                            value=5,
                            marks={num: 5 * num + 1 for num in range(10)}
                        )
                    ]
                ),
                html.Div(
                    style={
                        'width': '40%',
                        'display': 'inline-block',
                        'margin-left': '6.67%',
                        'margin-right': '3.33%'
                    },
                    children=[
                        html.Label(
                            htmlFor='slider-d',
                            children='Degree (d)'
                        ),
                        dcc.Slider(
                            id='slider-d',
                            min=0,
                            max=7,
                            value=4,
                            marks={num: num for num in range(6 + 1)}
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id='regression-graph-div'
        )
    ]
)


def update_regression_module(algorithm, k, degree, kernel):
    mesh_step = .005
    x_min = constants.training[:, 0].min() - .005
    x_max = constants.training[:, 0].max() + .005
    y_min = constants.training[:, 1].min() - .005
    y_max = constants.training[:, 1].max() + .005

    x_grid, y_grid = np.meshgrid(np.arange(x_min, x_max, mesh_step),
                                 np.arange(y_min, y_max, mesh_step))
    points = np.c_[x_grid.ravel(), y_grid.ravel()]

    if algorithm == 'knn':
        neigh = KNeighborsRegressor(n_neighbors=k)
        neigh.fit(constants.training, constants.labels)
        current_classifier = lambda test: neigh.predict(test)

    elif algorithm == 'linear':
        reg = LinearRegression(fit_intercept=False)
        poly = PolynomialFeatures(degree=degree)
        reg.fit(poly.fit_transform(constants.training), constants.labels)
        current_classifier = lambda test: reg.predict(poly.fit_transform(test))

    elif algorithm == 'svm':
        clf = SVR(kernel=kernel)
        clf.fit(constants.training, constants.labels)
        current_classifier = lambda test: clf.predict(test)

    z_predicted = current_classifier(points)
    return current_classifier, [
        dcc.Graph(
            id='regression-graph-1',
            style={'width': '50%', 'float': 'left'},
            figure=go.Figure(
                data=[
                    go.Contour(
                        x=np.arange(x_min, x_max, mesh_step),
                        y=np.arange(y_min, y_max, mesh_step),
                        z=z_predicted.reshape(x_grid.shape),
                        colorscale=constants.color_scales['red_blue'],
                        showscale=True,
                        contours=dict(
                            coloring='lines',
                            showlabels=False
                        ),
                        line=dict(
                            width=3
                        )
                    )
                ],
                layout=go.Layout(
                    title='Regression Contours',
                    autosize=True,
                    hovermode='closest',
                    xaxis=dict(
                        ticks='',
                        showticklabels=False,
                        showgrid=False,
                        zeroline=False,
                    ),
                    yaxis=dict(
                        ticks='',
                        showticklabels=False,
                        showgrid=False,
                        zeroline=False,
                    )
                )
            )
        ),
        dcc.Graph(
            id='regression-graph-2',
            style={'width': '50%', 'float': 'left'},
            figure=go.Figure(
                data=[
                    go.Surface(
                        x=np.arange(x_min, x_max, mesh_step),
                        y=np.arange(y_min, y_max, mesh_step),
                        z=z_predicted.reshape(x_grid.shape),
                        colorscale=constants.color_scales['red_blue'],
                        showscale=True
                    )
                ],
                layout=go.Layout(
                    title='Regression Surface',
                    autosize=True,
                    hovermode='closest',
                    scene={
                        'xaxis': {'title': 'latitude'},
                        'yaxis': {'title': 'longitude'},
                        'zaxis': {'title': 'price'}
                    }
                )
            )
        )
    ]


# PREDICTION MODULE:
prediction_module = html.Div(
    id='prediction-module',
    style={'text-align': 'center', 'padding': '20px 0'},
    children=[
        dcc.Input(
            id='latitude-input',
            placeholder='Latitude',
            type='text',
            value=''),
        dcc.Input(
            id='longitude-input',
            placeholder='Longitude',
            type='text',
            value=''),
        html.Button('Predict', id='submit-button'),
        html.Div(
            id='prediction-output',
            children=html.P(
                id='prediction-text'
            )
        )
    ]
)
