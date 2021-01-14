import os
import csv

# import file
pybank_csv = os.path.join("/Users/valerie/Desktop/DA_VA/homework/3_Python/python-challenge/PyBank/Resources/budget_data.csv")

# open and read csv file
with open(pybank_csv, 'r') as  csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    csv_header = next(csv_file)
    
# define variables
    row_count = 0
    total_amount = 0
    total_change = 0
    last_month = 0
    largest_increase = 0
    largest_decrease = 0
    monthly_change = 0
    
    # loop through rows starting with conditional to solve header issue
    for row in csv_reader:
        if row_count != 0:
            total_change += int(row[1]) - last_month
            average = total_change / row_count

        # month counter for total months    
        row_count += 1

        # total amount of profits/losses in column b
        total_amount += int(row[1])
        
        # calculates the difference between current and previous value
        monthly_change = int(row[1]) - last_month

        # max and min functions    
        largest_increase = max(largest_increase, monthly_change)
        largest_decrease = min(largest_decrease, monthly_change)
        
        # reset previous row's value for next loop
        last_month = int(row[1])

    # print out the financial analysis
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total_amount}")
    print(f"Average Change: ${round(average,2)}")
    print(f"Greatest Increase in Profits: ${largest_increase}")
    print(f"Greatest Decrease in Profits: ${largest_decrease}")