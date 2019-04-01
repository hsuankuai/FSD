import os
import csv

cmd = 'java -jar tabula.jar 01.pdf -p all -n -o 01.csv'
os.system(cmd)
with open("01.csv") as csvfile:
    reader = csv.reader(csvfile)
    txtfile = open("01.txt", "w")
    for row in reader:
        txtfile.write(str(row)[2:-2])