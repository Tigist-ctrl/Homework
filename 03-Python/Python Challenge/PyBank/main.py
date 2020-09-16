import os
import csv
from pathlib import Path

#employee_data = os.path.join(os.getcwd(), 'Resources/budget_data.csv')
budget_csv = os.path.join(Path(__file__).parent,"Resources","budget_data.csv")

print ("Financial Analysis")
print ("----------------------------")

#toal amount of months
total_months = sum(1 for row in budget_csv)
print ("Total Months:" + str(total_months -1)) #-1 to remove the header

#total amount of the changes in "Profit/Losses" over the entire period
total = df['Losses'].sum(budget_csv) 
print ("Total:" + str(total)

#total = sum (1 for row in ["Losses" in budget_csv])
#print ("Total:" + str(total)


#for row in budget_csv:
   # _dist = row[2]
 #   try: 
  #      _dist = float(_dist)
  #  except ValueError:
  #      _dist = 0

  #  dist += _dist

#csvpath = os.path.join("budget_data.csv")
#with open (budget_csv,'r') as csvfile:
    #csv_reader = csv.file(csv_reader, delimiter = ',')
    #csv_reader = next(csv_reader)
    #print(', '.join(row)