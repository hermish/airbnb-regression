# AirBnB Optimization

## the data
> Graph some (any 3) interesting metrics, maps, or trends from the dataset

We can first visualize the listings data on a map, examining the AirBnB listings through a lens
of average ratings and price. We might also be interested in the availabilities of these listings
looking backward.

---
## price estimation
> Given the geo-location (latitude and longitude) of a new property, estimate the weekly average 
> income the homeowner can make with Airbnb.

To estimate the weekely average income, we run a k-means clustering algorithm to find discrete 
geographic clusters of AirBnB properties, which may be more informative than simply using blanket
neighbourhoods. For each of these, we construct a linear model with parameters longitude and
latitude to estimate local price and volume. Pre-computing these models allows for efficient
predictions of AirBnB prices as a linear combination of these models.

---
## booking optimization
> Given the geo-location (latitude and longitude) of a property, what is the ideal price per night 
> that will yield maximum bookings or revenue?
