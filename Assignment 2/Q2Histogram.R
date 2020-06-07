# Megan Chu
# PID: A12814536
# Assignment 2
# 4/25/18
setwd("C:/Users/megan/OneDrive/Documents/UCSD Year 3/BENG 182/Assignment 2")

#replace file name accordingly for P1 and P2
data <- read.table("lengthsP1.txt", header = TRUE)

LocalAlignmentLength <- data$lengths
p <- hist(LocalAlignmentLength, breaks = 10, plot = FALSE)
plot(p, xlim = c(0, 20), ylim = c(0, 300), col = rgb(0,0,1,1/4),  
            main="Histogram of Q2 P1", labels = TRUE)

data <- read.table("lengthsP2.txt", header = TRUE)

LocalAlignmentLength <- data$lengths
p <- hist(LocalAlignmentLength, breaks = 10, plot = FALSE)
plot(p, xlim = c(0, 20), ylim = c(0, 300), col = rgb(0,0,1,1/4),  
            main="Histogram of Q2 P2", labels = TRUE)
