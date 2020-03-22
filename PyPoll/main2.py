import os
import csv
import sys

election_data_csv = os.path.join (".", "Resources", "election_data.csv")
#initialize variables
Vote_count = 0
Candidate_names = []


#open and read csv
with open (election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header row
    header = next(csvreader)
    

#calculate the total number of vote included in the data set
    for row in csvreader:
        Vote_count+=1
        Candidate_names = (row[2])
      
    print("Election Results")
    print("-------------------")
    print(f"Total Votes: {Vote_count}")
    print(f"Candidate Names: {Candidate_names}")