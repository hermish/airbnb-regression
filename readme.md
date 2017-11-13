# AirBnB Optimization

## Tools and Resources
Data analysis completed in R, with most source code provided. The app itself is 
created using Dash, a Python framework for building analytical web applications
atop Plotly.js, React, and Flask.

The primary assumption I made while analyzing the data is that the number of
unavailable days for each AirBnB is equal to the number of days it was booked,
at least over the coming 30 days. This clearly overcounts the number of days for
which there will be a guest, but we use this as our best estimate.

## Summary
### Visualizing the Data
> Graph some (any 3) interesting metrics, maps, or trends from the dataset

We visualized the listings data on a map, using a color scale from red to green 
to indicate the average rating of each location, using the size of each
marker to represent the volume of bookings. We acn then also examine where
prices are the highest in San Francisco

### Estimating Revenue
> Given the geo-location (latitude and longitude) of a new property, estimate 
> the weekly average income the homeowner can make with Airbnb.

To estimate the weekely average income, we clustered the data points based on
neighbourhood. For each of these, we construct a linear model with parameters
longitude and latitude to estimate local price and volume. Pre-computing these
models allows for efficient predictions of AirBnB prices from these local
estimates, by then selecting the model which are most relevent to a particular
location

### Booking Optimization
> Given the geo-location (latitude and longitude) of a property, what is the 
> ideal price per night that will yield maximum bookings or revenue?

We approched this problem very similarly; there seems to be no clear
price-revenue curve, hence we attempt to optimize the number of booking by
simply suggesting a competitive price.