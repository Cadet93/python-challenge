#Module for collections
import collections

# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#create lists and dictionaries
allcandidates = []
candidates = []


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        #create lists with data from the csv for all voter_ids and all candidates
        allcandidates.append(row[2])

        if row[2] not in candidates:
            candidates.append(row[2])
    
    #create dictionary with candidates vote totals
    candidates_dict = {}
    
    #Populate vote totals into a dictionary for each candidate
    for candidates in allcandidates:
        if candidates not in candidates_dict:
            candidates_dict[candidates] = 1
        else:
            candidates_dict[candidates] +=1

#save the path where you want the export file created
#save_path = '~/Desktop/Bootcamp Files/Python Homework/python-challenge/PyPoll/Resources'

#name_of_file = "election_results.txt"

#complete_name = os.path.join(save_path, name_of_file)
    
#create export txt file
output_file = open('election_results.txt', 'w')

#print header and total votes
print(f'Election Results \n-------------------- \nTotal Votes: {len(allcandidates)} \n--------------------')
output_file.write(f'Election Results \n-------------------- \nTotal Votes: {len(allcandidates)} \n-------------------- \n')
    
#determine and print each candidate's vote percentage
for key, value in candidates_dict.items():
    print (f'{key} = {round(value/len(allcandidates)*100, 0)}% ({value})')
    output_file.write(f'{key} = {round(value/len(allcandidates)*100, 0)}% ({value}) \n')
    
print(f'-------------------- \nWinner: {max(candidates_dict, key = candidates_dict.get)} \n-------------------')
output_file.write(f'-------------------- \nWinner: {max(candidates_dict, key = candidates_dict.get)} \n-------------------')


    
    

    
        


        



