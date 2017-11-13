# AirBnB Optimization

## Tools and Resources
Data analysis completed in R, with most source code provided. The app itself is 
created using Dash, a Python framework for building analytical web applications
atop Plotly.js, React, and Flask.

The primary assumption I made while analyzing the data is that the number of
unavailable days for each AirBnB is equal to the number of days it was booked, at
least over the coming 30 days. This clearly overcounts the number of days for
which there will be a guest, but we use this as our best estimate.