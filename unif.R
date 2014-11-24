
unifmean <- function(n,m,a) {
  datas <- c(1:n)
  for(i in 1:n){
    datas[i] <- mean(runif(m)*a)
  }
  return(datas)
}
