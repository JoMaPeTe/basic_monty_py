import csv
with open("datos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre","Edad"])
        writer.writerow(["Baldo","25"])
        writer.writerow(["Chechu","15"])

with open("datos.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
