binomial.conf.interval <- function(y, n) {
  z <- qnorm(.95)
  phat <- y/n
  se <- sqrt(phat * (1 - phat)/n)
  return(c(phat - z * se, phat + z * se))
}