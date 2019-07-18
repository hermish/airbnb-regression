# AirBnB Regression

> Visualization of common machine learning regression algorithms on San
> Francisco AirBnB listing data.

See the application hosted [here](http://airbnb-reg-v1.herokuapp.com/). For
comparison, [here](http://airbnb-reg-v0.herokuapp.com/) is the original
version of the web application.

## About

This web application was built almost completely in Python, using
[Dash](https://plot.ly/dash/), a Python framework for building analytical web 
applications atop React and Flask. Dash plays particular well with
[plotly](https://plot.ly/), which was used to create the live visualizations.

![Map Image](https://github.com/hermish/airbnb-regression/blob/master/docs/maps.png?raw=true)
![Regression Image](https://github.com/hermish/airbnb-regression/blob/master/docs/regression.png?raw=true)

The data was imported and analyzed using [pandas](https://pandas.pydata.org/), 
while the regression models were built with [scikit-learn](https://scikit-learn.org),
a common Python machine learning library. Specifically, the application
showcases the polynomial regression, k-nearest neighbors and support vector
machine regression (SVR) models available in scikit-learn.

## Installation

To install and run this web application locally, following the steps below
after downloading the repository. First, we need to ensure the correct
dependencies are installed, which are listed in `production/requirements.txt`.
This can be done from the terminal with the following command.

```
pip install -r production/requirements.txt
```

After installing the appropriate dependencies, navigate to the app folder and
start the server by simply running `app.py`. Now the application should be
running locally: visit `http://localhost:8050/` to see it.

```
cd app
python app.py
```

## History

The the original version of the web application was initially built for the
CapitalOne Software Engineering summit. As part of the challenge, we were
required to build a web application which explored the following questions.

1. Graph some (any 3) interesting metrics, maps, or trends from the dataset.
2. Given the geo-location (latitude and longitude) of a new property, estimate
the weekly average income the homeowner can make with Airbnb.
3. Given the geo-location (latitude and longitude) of a property, what is the 
ideal price per night that will yield maximum bookings or revenue?

After taking a machine learning class, I decided that the data would
be perfect for visualizing various machine learning regression algorithms since
a 3D plot had a clear interpretation: it represents a price map over San
Francisco.
