#Import modules 

import os
import csv

# Set the path for the CSV file 

PyBankcsv = os.path.join('Resources','budget_data.csv')

# Create the lists to store data. 

# Initial profits set to 0 to handle edge case when comparing with previous month (when index=0)
profits = [0]
change_profits = []
total_profits = 0
count = 1
avg_change_profits = 0
months= []



# Open the CSV using the set path PyBankcsv

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conducting the ask
    for row in csvreader:    
       months.append(row[0])
       profit = int(row[1])
       profits.append(profit)
       # count 1  profits = [0, 867884]
       change_profits.append(profit-profits[count-1])
       count= count + 1
    # counts is one more than number of records due to initisation with 1
    avg_change_profits = sum(change_profits)/(count-1)
    max_profit = max(change_profits)
    min_profit = min(change_profits)

    min_index= change_profits.index(min_profit)
    max_index= change_profits.index(max_profit)
    # Get corresponding months of 
    min_month = months[min_index]
    max_month = months[max_index]
    # print(avg_change_profits)
    # print(min_profit,min_month)
    # print( max_profit,max_month)
    total_profits= sum(profits)
    print("Financial Analysis")
    print("--------------------------------------")
    # Using count variable outside loop after its completion
    print("Total Months: " + str(count-1))
    print("Total Profits: " + "$" + str(total_profits))
    print("Average Change: " + "$" + str(int(avg_change_profits)))
    print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_profit) + ")")
    print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_profit)+ ")")
# Export into csv
with open('financial_analysis.txt', 'w') as text:
  text.write("Financial Analysis"+ "\n")
  text.write("------------------------------------"+ "\n")
  text.write("Total Months: " + str(count-1)+ "\n")
  text.write("Total Profits: " + "$" + str(total_profits)+ "\n")
  text.write("Average Change: " + "$" + str(int(avg_change_profits))+ "\n")
  text.write("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_profit) + ")"+ "\n")
  text.write("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_profit)+ ")"+ "\n")

