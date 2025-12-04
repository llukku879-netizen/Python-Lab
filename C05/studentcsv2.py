import csv
with open('Studentcsv')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("name")
    print("---")
    for i in data:
          print(i['Name']) 
