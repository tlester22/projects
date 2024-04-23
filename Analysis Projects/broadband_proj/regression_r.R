# reading in the cleaned PUMS data csv file
myData <- read.table("../../../../OneDrive/Documents/PUMS_multiple_var.csv", header = TRUE, sep=",")

summary(myData)

myReg1=lm(HISPEED~HINCP+GRPIP+PAP+FES, data=myData)

summary(myReg1)

myReg2 = lm(HISPEED~HINCP+GRPIP+PAP+FES+FS, data=myData)

summary(myReg2)