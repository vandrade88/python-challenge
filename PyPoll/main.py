import os
import csv

# import file
pypoll_csv = os.path.join("/Users/valerie/Desktop/DA_VA/homework/3_Python/python-challenge/PyPoll/Resources/election_data.csv")

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
            
    khan_percentage = round((khan/row_count)*100,3)
    correy_percentage = round((correy/row_count)*100,3)
    li_percentage = round((li/row_count)*100,2)
    otooley_percentage = round((otooley/row_count)*100,3)

    # print out the election results
    print("Election Results")
    print("----------------------------------")
    print(f"Total Votes: {row_count}")
    print("----------------------------------") 
    print(f"Khan: {khan_percentage}% ({khan})")
    print(f"Correy: {correy_percentage}% ({correy})")
    print(f"Li: {li_percentage}% ({li})")
    print(f"O'Tooley: {otooley_percentage}% ({otooley})")
    print("----------------------------------")
    print(f"Winner: {variable}")
    print("----------------------------------")