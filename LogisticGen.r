#!/path/to/Rscript
samples = read.csv("samples.csv")
gen = glm(formula = isfraud~., data = samples, family = "binomial")
for (i in 1:7) write.csv(coef(gen)[i],"coef.csv")


	