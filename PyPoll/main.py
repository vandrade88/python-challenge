import os
import csv

# import file
pypoll_csv = os.path.join("/Users/valerie/Desktop/DA_VA/homework/3_Python/python-challenge/PyPoll/Resources/election_data.csv")
pypoll_text = os.path.join("/Users/valerie/Desktop/DA_VA/homework/3_Python/python-challenge/PyPoll/Analysis/election_analysis.txt")

# open and read csv file
with open(pypoll_csv, 'r') as  csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)
    
# define variables
    total_votes = []
    khan_votes = []
    correy_votes = []
    li_votes = []
    otooley_votes = []
    
    row_count = 0
    total_votes_amount = 0
    
    # loop through rows
    for row in csv_reader:
        
        # row counter for voter ids column
        row_count += 1

        # make new list for each candidate
        if (row[2]) == "Khan":
            khan_votes.append(row[0])
            khan = len(khan_votes)
            
        elif (row[2]) == "Correy":
            correy_votes.append(row[0])
            correy = len(correy_votes)
        
        elif (row[2]) == "Li":
            li_votes.append(row[0])
            li = len(li_votes)
        
        elif (row[2]) == "O'Tooley":
            otooley_votes.append(row[0])
            otooley = len(otooley_votes)
            
    khan_per = (khan/row_count) *100
    correy_per = (correy/row_count) *100
    li_per = (li/row_count) *100
    otooley_per = (otooley/row_count) *100

    if (khan_per > correy_per) and (khan_per > li_per) and (khan_per > otooley_per):
        winner = "Khan"
    elif (correy_per > khan_per) and (correy_per > pct_Li) and (correy_per > pct_OTooley):
        winner = "Correy"
    elif (li_per > correy_per) and (li_per > khan_per) and (li_per > otooley_per):
        winner = "Li"
    elif (otooley_per > correy_per) and (otooley_per > pct_Khan) and (otooley_per > li_per ):
        winner = "O'Tooley"

    # define function for printing results
results = (
    f"\nElection Results\n"
    f"----------------------------------\n"
    f"Total Votes: {row_count}\n"
    f"----------------------------------\n"
    f"Khan: {round(khan_per, 3)}% ({khan})\n"
    f"Correy: {round(correy_per, 3)}% ({correy})\n"
    f"Li: {round(li_per, 3)}% ({li})\n"
    f"O'Tooley: {round(otooley_per, 3)}% ({otooley})\n"
    f"----------------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------------\n"
)

# print results in terminal
print(results)

# export results to new text file
with open(pypoll_text, "w") as text_file:
    text_file.write(results)