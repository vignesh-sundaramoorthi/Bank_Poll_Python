#Import modules 

import os
import csv

# Set the path for the CSV file 

PyPollcsv = os.path.join('Resources','election_data.csv')

# Create the lists to store data. 
all_candidates=[]
voted_candidates=[]
count=0
vote_count=[]
vote_percent=[]

# Open the CSV using the set path PyBankcsv

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conducting the ask
    for row in csvreader:
        count= count + 1
        all_candidates.append(row[2])
    #To perfom unique value subsetting
    for each in set(all_candidates):
        # Build an array of each unique candidiates
        voted_candidates.append(each)
        # Assign a variable to hold the counts of unique candidates
        total=all_candidates.count(each)
        vote_count.append(total)
        # calculating percentage
        percentage=(total/count)*100
        vote_percent.append(percentage)

    winning_vote_count=max(vote_count)
    winner=voted_candidates[vote_count.index(winning_vote_count)]

    print("Election Results")
    print("-----------------------------------------------------")
    print("Total Votes:"+ str(count))
    print("-----------------------------------------------------")
    for n in range(len(voted_candidates)):
        print(voted_candidates[n]+":"+str(vote_percent[n])+"% ("+str(vote_count[n])+")") 
    print("-----------------------------------------------------")
    print("The winner is: " + winner)
    print("-----------------------------------------------------")

with open('election_analysis.txt', 'w') as text:

    text.write("Election Results"+"\n")
    text.write("-----------------------------------------------------"+"\n")
    text.write("Total Votes:"+ str(count)+"\n")
    text.write("-----------------------------------------------------"+"\n")
    for n in range(len(voted_candidates)):
        text.write(voted_candidates[n]+":"+str(vote_percent[n])+"% ("+str(vote_count[n])+")"+"\n") 
    text.write("-----------------------------------------------------"+"\n")
    text.write("The winner is: " + winner+"\n")
    text.write("-----------------------------------------------------"+"\n")



