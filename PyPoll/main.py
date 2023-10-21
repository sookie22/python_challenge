import os
# Use "csv" module to read and process the CSV file
import csv

# Defining path to the CSV file
csv_path = r"C:\Users\sooki\python_challenge\PyPoll\Resources\election_data.csv"

# Variables
total_votes = 0
winner_votes = 0

# For storing the vote counts for candidates
candidates_vote_counts = {}
# For storing the name of the winning candidate
winner = ""
# For storing the percentage of vote for each candidate
vote_percentage = {}

# Read the CSV file
with open(csv_path, "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    # Loop through each row in the CSV file
    # Increment the total vote count by 1 as it goes
    # Candidate name in column 3 by Python starts counting from 0
    for row in csv_reader:
        total_votes += 1  
        candidate_name = row[2] 

        # If the candidate's name is already in the dict, increment by 1 to keep going
        # If not, add the name into the dict, then set to 1 again to repeat the process
        if candidate_name in candidates_vote_counts:
            candidates_vote_counts[candidate_name] += 1
        else:
            candidates_vote_counts[candidate_name] = 1

# If the current candidate's vote count is higher than the previous candidate's vote count
# Then update the current candidate's vote count as winner_votes
# Then the winner is the current candidate
for candidate, votes in candidates_vote_counts.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

    # To calculate the % of votes for the current candidate
    # Then store the % resulte into vote_percentage dict
    percentage = (votes / total_votes) * 100
    vote_percentage[candidate] = percentage

# For priting the results as per task
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates_vote_counts.items():
    print(f"{candidate}: {float(vote_percentage[candidate]):.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# For exporting the results to a .txt file
text_file_path = r"C:\Users\sooki\python_challenge\PyPoll\Analysis\election_results.txt"

with open(text_file_path, "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, votes in candidates_vote_counts.items():
        text_file.write(f"{candidate}: {float(vote_percentage[candidate]):.3f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")
