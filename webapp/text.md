# AirBnB Optimization

## The Data
We can first visualize the listings data through a map, examining the AirBnB listings through a 
lens of average ratings and price. 

---
## Price Estimation
To estimate the weekely average income, we run a k-means clustering algorithm to find discrete 
geographic clusters of AirBnB properties, which may be more informative than simply using blanket
neighbourhoods. For each of these, we construct a linear model with parameters longitude and
latitude to estimate local price and volume. Pre-computing these models allows for efficient
predictions of AirBnB prices as a linear combination of these models.

---
## Booking Optimization
