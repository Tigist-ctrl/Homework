import os
import csv
from pathlib import Path

#employee_data = os.path.join(os.getcwd(), 'Resources/budget_data.csv')
budget_csv = os.path.join(Path(__file__).parent,"Resources","budget_data.csv")

#toal amount of months
file = open("budget_data.csv")
reader = csv.reader(budget_data.csv)
lines= len(list(reader))

total_monhs = csv.reader len(list(reader))
print(total_months)

with open (budget_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    for row in csv_reader:
        print(', '.join(row))











