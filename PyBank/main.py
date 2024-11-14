# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv #csv module is imported for reading/writing/handling csv files
import os #os module makes the file path compatible with any operating system

# File to load data from
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
#File to write the output in txt form
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define  and  initializing variables to track the financial data
total_months = 0 
total_net = 0 
Greatest_Increase = 0
Greatest_Decrease = 0
Increase_Month = 0
Decrease_Month = 0
# Add more variables to track other necessary financial data
Profit_Loss = []
Changes = []
Dates = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

# Stores the header row in a variable 'header'
    header = next(reader)
    
# Process each row of data
    for row in reader:
        
# Track the total. 
        total_months += 1           #As the row is iterated, the total_months variable is incremented
        total_net += int(row[1])    #This calculate the net total amount of Profit/Loss over the entire period
        Profit_Loss.append(int(row[1])) #A separate list Profit_Loss is created for column 1 of csv file
        Dates.append(str(row[0]))     #A separate list Dates is created for column 0 of csv file

    
# Track the average change
for rows in  range(1,len(Profit_Loss)):
    Consecutive_Difference = Profit_Loss[rows] - Profit_Loss[rows - 1]  #  difference between two consecutive rows are taken
    Changes.append(Consecutive_Difference) # a list 'Changes' is created which contains a list of consecutive differences
    average_change = round(sum(Changes)/len(Changes),2) # Average change = sum of 'Changes' list/total number of rows in 'changes' list.The output is rounded to 2 decimals
   

 # Calculate the greatest increase in profits (month and amount)
    for i in range(1,len(Profit_Loss)):
        Balance = Profit_Loss[i] - Profit_Loss[i-1] 
        if Balance > Greatest_Increase:         
            Greatest_Increase = Balance
            Increase_Month = Dates[i]
        
   

# Calculate the greatest decrease in losses (month and amount)
for j in range(1,len(Profit_Loss)):
        Balance = Profit_Loss[j] - Profit_Loss[j-1]
        if Balance < Greatest_Decrease:
            Greatest_Decrease = Balance 
            Decrease_Month = Dates[j]


# Generate the output summary
Financial_Analysis = (
    f"Financial Analysis\n"
    f"-----------------------------------\n" 
    f"Total Months : {total_months}\n"   
    f"Total: ${total_net}\n"
    f"Average Change : ${average_change}\n"
    f"Greatest Increase in Profits : {Increase_Month} (${Greatest_Increase})\n"
    f"Greatest Decrease in Profits : {Decrease_Month} (${Greatest_Decrease})"
    )

# Print the output

print(Financial_Analysis)


# Writing the results to a text file
with open(file_to_output , "w") as txt_file:
    txt_file.write(Financial_Analysis)
