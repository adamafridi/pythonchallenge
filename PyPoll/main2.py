import os
import csv
import sys
import operator

election_data_csv = os.path.join (".", "Resources", "election_data.csv")
#initialize variables
Vote_count = 0
Candidate_names = []
Candidate_votes = {}


#open and read csv
with open (election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header row
    header = next(csvreader)
    

#calculate the total number of votes included in the data set
    for row in csvreader:
        Vote_count+=1
        Candidate_name = (row[2])
        if Candidate_name not in Candidate_names :
            Candidate_names.append(Candidate_name)
            Candidate_votes[Candidate_name] = 0
        Candidate_votes[Candidate_name] = Candidate_votes[Candidate_name]+1
    Winning_Candidate = max(Candidate_votes.items(), key = operator.itemgetter(1))[0]
    print("Election Results")
    print("-------------------")
    print(f"Total Votes: {Vote_count}")
    print(f"Candidate Names: {Candidate_names}")
    print(f"Candidate Votes: {Candidate_votes}")
    print(f"Winning Candidate: {Winning_Candidate}")

