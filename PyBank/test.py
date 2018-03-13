import os 
import csv

budget1_csv = "budget_data_1.csv"
budget2_csv = "budget_data_2.csv"

total_months = []
total_revenue = []
average_change = []
greatest_increase = []
greatest_decrease = []

with open(budget1_csv, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    numMonths = 0    
    revenue = 0

    next(csvreader)
    for row in csvreader:
        numMonths += 1
        revenue = revenue + int(row[1])
    total_months.append(numMonths)
    print("Total Months: " + str(numMonths)) 
    total_revenue.append(revenue)
    print("Total Revenue: $" + str(revenue))
    
    average = revenue/numMonths
    average_change.append(average)
    print("Average Revenue Change: $" + str(int(average)))
    
    print(min(row[1]))
        
   




