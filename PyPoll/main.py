#Import operating system and csv
import os
import csv

#Open and read csv 
election_csv = os.path.join("election_data.csv")
with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    next(csvreader)

#Lists to store data
    voter_id = []
    candidate = []
    candidate_votes = {}

#Read through each row of csv
    for row in csvreader:

# Loop through column to add Voter IDs
        voter_id.append(row[0])
#Loop through column to add Candidate
        candidate_name = row[2]

#Lists candidates who received votes and lists votes per candidate
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_votes[candidate_name] = 0
        else: candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Calculate the total number of votes cast and print
total_votes_cast = len(voter_id)
print("Election Results")
print("---------------------------")
print(f"Total Votes: {len(voter_id)}")

#Print votes per candidate
print("---------------------------")


# calculate vote percentage and identify winner
vote= -100
for name in candidate:  
    if candidate_votes[name] > vote:
        vote = candidate_votes[name]
        winner = name
    print(f'{name} {":%.2f%%"%(candidate_votes[name]/len(voter_id)*100)} {"("}{str(candidate_votes[name])}{")"}') 
print("---------------------------")
    #print('-------------------------')
    
print(f'Winner: {winner}')
dashbreak = "---------------------------"

f = open('Election_Results.txt', 'w')
print("Election Results",file=f)
print("---------------------------")
print(f"Total Votes: {len(voter_id)}",file=f)

#Print votes per candidate
print("---------------------------")

# calculate vote percentage and identify winner
for name in candidate:  
    if candidate_votes[name] > vote:
        vote = candidate_votes[name]
        winner = name
    print(f'{name} {":%.2f%%"%(candidate_votes[name]/len(voter_id)*100)} {"("}{str(candidate_votes[name])}{")"}',file=f)
print("---------------------------", file=f)
    #print('-------------------------')
    
print(f'Winner: {winner}',file=f)
dashbreak = "---------------------------"

f.close()
