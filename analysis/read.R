location <- "../data/listings.csv"
model_output <- "../model/map_ratings_data.csv"
revenue_output <- "../model/map_revenue_data.csv"
cleaned_output <- "../model/cleaned_data.csv"
model_output <- "../model/model.csv"
neighbourhoods <- "../data/neighbourhoods.csv"
  
read_listings <- function(filename) {
  listings <- read.csv(filename, stringsAsFactors=FALSE)
  listings
}

get_map_ratings_data <- function(listings, model_output) {
  ratings <- data.frame(listings$review_scores_rating)
  mean_rating <- mean(listings$review_scores_rating, na.rm=TRUE)
  ratings[is.na(ratings)] <- mean_rating
  
  prices <- as.numeric(gsub('[$,]', '', listings$price))
  price_per <- prices / listings$accommodates
  
  new_data <- data.frame(
    listings$latitude,
    listings$longitude,
    11 - listings$availability_30 %/% 3,
    ratings,
    price_per
    # log10(price_per)
  )
  colnames(new_data) <- c('lat', 'lon', 'size', 'color', 'price')
  write.csv(new_data, model_output)
  new_data
}

get_map_revenue_data <- function(listings, revenue_output) {
  ratings <- data.frame(listings$review_scores_rating)
  mean_rating <- mean(listings$review_scores_rating, na.rm=TRUE)
  ratings[is.na(ratings)] <- mean_rating
  
  prices <- as.numeric(gsub('[$,]', '', listings$price))
  size <- 30 - listings$availability_30

  new_data <- data.frame(
    listings$latitude,
    listings$longitude,
    size,
    price_per,
    size * prices
  )
  colnames(new_data) <- c('lat', 'lon', 'price', 'cost', 'rev')
  write.csv(new_data, revenue_output)
  new_data
}


strip_outliers <- function(listings, cleaned_output) {
  prices <- as.numeric(gsub('[$,]', '', listings$price))
  size <- 30 - listings$availability_30
  
  new_data <- data.frame(
    listings$latitude,
    listings$longitude,
    size,
    price_per,
    size * prices,
    listings$neighbourhood_cleansed
  )
  colnames(new_data) <- c('lat', 'lon', 'size', 'cost', 'rev', 'loc')
  cleaned <- new_data[!new_data$cost %in% boxplot.stats(new_data$cost)$out, ]
  
  write.csv(cleaned, cleaned_output)
  cleaned
}