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

    #create output file
    output_file = open("analysis.txt", 'w')

    #Print Title
    print(f'Financial Analysis \n--------------------')
    output_file.write(f'Financial Analysis \n------------------\n')

    #print the number of months
    print(f'Total Months:  {len(dates)}')
    output_file.write(f'Total Months:  {len(dates)} \n')

    #print the over all profit/loss of the period
    print(f'Total: ${sum(profit_loss)}')
    output_file.write(f'Total: ${sum(profit_loss)} \n')

    #determine monthly profit/loss changes and add to a list
    for value in range(len(profit_loss)-1):
        change_amount = int(profit_loss[value+1]) - int(profit_loss[value])
        change.append(change_amount)
        
    #assign average change, max profit, and greatest loss values and print them to terminal and output file
    avg_change = round(statistics.mean(change), 2)
    print(f'Average Change: ${(avg_change)}')
    output_file.write(f'Average Change: ${(avg_change)} \n')

    #determine greatest profit and it's corresponding month
    g_increase = max(change)
    gi_index = change.index(max(change))+1 
    gi_month = dates[gi_index]

    #determine greatest loss and it's corresponding month
    g_decrease = min(change)
    gd_index = change.index(min(change))+1 
    gd_month = dates[gd_index]

    print(f'Greatest Increase in Profits: {gi_month} (${max(change)})')
    output_file.write(f'Greatest Increase in Profits: {gi_month} (${max(change)}) \n')
    print(f'Greatest Decrease in Profits: {gd_month} (${min(change)})')
    output_file.write(f'Greatest Decrease in Profits: {gd_month} (${min(change)}) \n')







