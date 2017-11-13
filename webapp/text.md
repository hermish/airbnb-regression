# AirBnB Optimization

## the data
> Graph some (any 3) interesting metrics, maps, or trends from the dataset

We can first visualize the listings data on a map, using a color scale from red
to green to indicate the average rating of each location, using the size of each
marker to represent the volume of bookings. We acn then also examine where
prices are the highest in San Francisco

---
## price estimation
> Given the geo-location (latitude and longitude) of a new property, estimate 
> the weekly average income the homeowner can make with Airbnb.

To estimate the weekely average income, we cluster the data points based on
neighbourhood. For each of these, we construct a linear model with parameters
longitude and latitude to estimate local price and volume. Pre-computing these
models allows for efficient predictions of AirBnB prices from these local
estimates, by then selecting the models which are most relevent to a particular
location.

---
## booking optimization
> Given the geo-location (latitude and longitude) of a property, what is the 
> ideal price per night that will yield maximum bookings or revenue?

We approch this problem very similarly; there seems to be no clear price-revenue
curve, hence we attempt to optimize the number of booking by simply suggesting
a competitive price.