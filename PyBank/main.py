#Python Homework Script for PyBank
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#module for average calculation
import statistics

csvpath = os.path.join('Resources', 'budget_data.csv')

#create list variables for date and profit_loss values
dates = []
profit_loss = []
change = []

#function to calculate average change
#def averageOfList(num):
    #sumOfNumbers = 0
    #for t in num:
        #sumOfNumbers = sumOfNumbers + t

    #avg = sumOfNumbers / len(num)
    #return avg

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        dates.append(row[0])
        profit_loss.append(int(row[1]))
        
    #print(dates)
    #print(profit_loss)


    #Print Title
    print("Financial Analysis")

    #print the number of months
    print(dates)
    print(len(dates))
    #print the over all profit/loss of the period
    print(sum(profit_loss))

    for value in range(len(profit_loss)-1):
        change_amount = int(profit_loss[value+1]) - int(profit_loss[value])
        change.append(change_amount)
        
    #avg_change = statistics.mean(change)
    #print(change)
    #total = 0
    #for i in change:
    #    total = total + i
    #print(change[0] + change[1])
    #print(total)


    #print(averageOfList(change))

    avg_change = round(statistics.mean(change), 2)
    print(avg_change)
    print(max(change))
    print(min(change))

#create file handler variable to represent the file
output_file = open("analysis.txt", 'w')

output_file.write(f'"Financial Analysis"  \n "------------------"')



