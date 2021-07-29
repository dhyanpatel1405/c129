import csv
d1=[]
d2=[]

with open('dataset_1.csv','r')as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        d1.append(row)


with open('dataset_2.csv','r')as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        d2.append(row)

h1=d1[0]
h2=d2[0]
p_d1=d1[1:]
p_d2=d2[1:]

header=h1+h2
planet_data=[]

for index,data_row in enumerate(p_d1):
    planet_data.append(p_d1[index]+p_d2[index])

with open('projectresult.csv','a+')as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)
#done