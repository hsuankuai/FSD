import math
import os

cmd = "cmd R BATCH LogisticGen.R"
os.system(cmd)

coefvar = []
coefreader = csv.reader("coef.csv")
column = [row[2] for row in reader]
coefvar.append(float(column))

expn = 0
i = 0
while i <= len(valvar) + 1:
    expn += valvar[i] * coefvar[i]
prob = math.exp(expn) / (1 + math.exp(expn))

if prob >= 0.5:
    print("该公司被认定为实施了IPO财务舞弊。")
else:
    print("该公司被认定为未实施IPO财务舞弊。")

os.remove(r'coef.csv')

'''
LogisticGen.R源代码：
#!/path/to/Rscript
samples = read.csv("samples.csv")
gen = glm(formula = isfraud~., data = samples, family = "binomial")
for (i in 1:7) write.csv(coef(gen)[i],"coef.csv")
'''