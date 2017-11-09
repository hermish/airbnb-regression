location <- "../data/listings.csv"
model_output <- "../model/map_ratings_data.csv"
  
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
    log10(price_per)
  )
  colnames(new_data) <- c('lat', 'lon', 'size', 'color', 'price')
  write.csv(new_data, model_output)
  new_data
}