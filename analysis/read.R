location <- "../data/listings.csv"
  
read_listings <- function(filename) {
  data <- read.csv(filename, stringsAsFactors=FALSE)
  data
}


