import os
import csv

# import file
pybank_csv = os.path.join("/Users/valerie/Desktop/DA_VA/homework/3_Python/python-challenge/PyBank/Resources/budget_data.csv")

# define function with lists and variables
def fin_analysis():
    total_months_amount = 0
    profit_change = 0
    loss_change = 0
    total_months_list = []
    profit_change_list = []
    loss_change_list = []
    
    # loop through rows to add column 1 into new list
    for row in csv_reader:
        total_months_list.append(row[0])
        
    # use len to calculate total months in new list
    total_months_amount = len(total_months_list)
        
    # print out the financial analysis
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {total_months_amount}")
    #print(f"Average Change: {value}")
    #print(f"Greatest Increase in Profits: {value}")
    #print(f"Greatest Decrease in Profits: {value}")
    
    # need return because function parameter was empty
    return

# open and read csv file
with open(pybank_csv, 'r') as  csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    csv_header = next(csv_file)
    
    # run function within csv reader
    fin_analysis()