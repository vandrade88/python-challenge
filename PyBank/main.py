import os
import csv

# import file
pybank_csv = os.path.join("/Users/valerie/Desktop/DA_VA/homework/3_Python/python-challenge/PyBank/Resources/budget_data.csv")
pybank_text = os.path.join("/Users/valerie/Desktop/DA_VA/homework/3_Python/python-challenge/PyBank/Analysis/financial_analysis.txt")

# open and read csv file
with open(pybank_csv, 'r') as  csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)
    
# define variables
    row_count = 0
    total_amount = 0
    total_change = 0
    last_month = 0
    largest_increase = ['', 0]
    largest_decrease = ['', 0]
    
    # loop through rows starting with conditional to solve header issue
    for row in csv_reader:
        if row_count != 0:
            total_change += int(row[1]) - last_month
            average = total_change / row_count

        # month counter for total months    
        row_count += 1

        # total amount of profits/losses in column b
        total_amount += int(row[1])
        
        # calculate the difference between current and previous month's value
        monthly_change = int(row[1]) - last_month

        # conditional to find the largest increase and decrease + determine the corresponding date
        if monthly_change > largest_increase[1]:
            largest_increase[1] = monthly_change
            largest_increase[0] = row[0]
        
        if monthly_change < largest_decrease[1]:
            largest_decrease[1] = monthly_change
            largest_decrease[0] = row[0]

        # reset previous row's value for next loop
        last_month = int(row[1])

# define function for printing results
results = (
    f"\nFinancial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {row_count}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${round(average,2)}\n"
    f"Greatest Increase in Profits: {largest_increase[0]} (${largest_increase[1]})\n"
    f"Greatest Decrease in Profits: {largest_decrease[0]} (${largest_decrease[1]})\n"
)

# print results in terminal
print(results)

# export results to new text file
with open(pybank_text, "w") as text_file:
    text_file.write(results)