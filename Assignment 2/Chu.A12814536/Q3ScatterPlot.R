# Megan Chu
# PID: A12814536
# Assignment 2
# 4/25/18

setwd("C:/Users/megan/OneDrive/Documents/UCSD Year 3/BENG 182/Assignment 2")

data <- read.table("Q3means.txt", header = TRUE)

plot(data$P, data$means, col = rgb(0,0,1,1), 
            main = "ScatterPlot of Q3 Means", xlab = "Parameter P (mismatch = indel)", 
            ylab = "Mean lP(n)")