import os
# Use "csv" module to read and process the CSV file
import csv

# Defining path to the CSV file
csv_path = r"C:\Users\sooki\python_challenge\PyBank\Resources\budget_data.csv"


# Variables
# For counting the number of months
total_months = 0 
# For storing the net total profit/loss over the period
net_total = 0 
# For storing the profit from the previous month
profit_previous = 0


# Lists
# For storing the profit change every month
profit_changes = []
# For storing the dates that corresponding to the profit_change
dates = []


# Open the CSV file and read the file contents
# "next" is used to skip the header at row 1 
with open(csv_path, "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    # For all the rows in this csv file, starting from the 1st and 2nd column
    for row in csv_reader:
        date = row[0]
        profit = int(row[1])

        # increament the count of total month by 1 to keep track of the count of total month
        total_months = total_months + 1
        # add the profit/loss for current month to net_total
        net_total = net_total + profit

        # As the total number of months change, calculte the change in profit from previous month and store it
        # Keep track of the date for the change
        if total_months > 1:
            change = profit - profit_previous
            profit_changes.append(change)
            dates.append(date)

        # profit from previous month be replaced by the new profit from current month
        profit_previous = profit

# Calculate the avg of profit_changes
avg_change = float(sum(profit_changes) / len(profit_changes))
# Calculate the greatest increase in profits amount over the entire period
great_increase = max(profit_changes)
# Calculate the greatest decrease in profits amount over the entire period
great_decrease = min(profit_changes)

# Getting the dates that correspond to both great_increase and great_decrease
date_great_increase = dates[profit_changes.index(great_increase)]
date_great_decrease = dates[profit_changes.index(great_decrease)]


# Generating final result as per task
print("Financial Analysis")
print("---------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Chnage: ${avg_change}")
print(f"Greatest Increase in Profits: {date_great_increase} (${great_increase})")
print(f"Greatest Decrease in Profits: {date_great_decrease} (${great_decrease})")

text_file_path = r"C:\Users\sooki\python_challenge\PyBank\Analysis\financial_analysis.txt"

with open(text_file_path, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("---------------------------\n")
    text_file.write(f"Total months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${avg_change}\n")
    text_file.write(f"Greatest Increase in Profits: {date_great_increase} (${great_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {date_great_decrease} (${great_decrease})\n")
