# AirBnB Optimization

## the data
> Graph some (any 3) interesting metrics, maps, or trends from the dataset

We first visualize the listings data on a map, using both a color scale, going
from red to green, and relative sizes of markers to visualize some combination
of number of rating, price or volume of bookings.

---
## price regression
> Given the geo-location (latitude and longitude) of a new property, estimate 
> the price an homeowner can competitively charge per night with Airbnb.

---
To estimate the value of a listing based on its latitude and longitude, we can 
choose one of many possible regression models. The default setting is k-nearest
neighbors regression, which estimates the price by "polling" the values of
nearby listing. However, below we can choose from linear regression, k-nearest
neighbors and support vector machine (SVM) regression. This provides a unique 
opportunity to visualize various regression models on (messy)
real world data.
