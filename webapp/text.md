# AirBnB Optimization

## the data
> Graph some (any 3) interesting metrics, maps, or trends from the dataset

We can first visualize the listings data on a map, using a color scale from red
to green to indicate the average rating of each location, using the size of each
marker to represent the volume of bookings.

---
## price estimation
> Given the geo-location (latitude and longitude) of a new property, estimate 
> the weekly average income the homeowner can make with Airbnb.

To estimate the weekely average income, we cluster the data points based on
neighbourhood. For each of these, we construct a linear model with parameters
longitude and latitude to estimate local price and volume. Pre-computing these
models allows for efficient predictions of AirBnB prices from these local
estimates.

---
## booking optimization
> Given the geo-location (latitude and longitude) of a property, what is the 
> ideal price per night that will yield maximum bookings or revenue?
