# **Financial Records Analysis**

[Resources](https://github.com/lovecy86/Financial-Record-Analysis/blob/main/PyBank/Resources/budget_data.csv)

[Financial Record Analysis Script](https://github.com/lovecy86/Financial-Record-Analysis/blob/main/PyBank/main.py)

[Result](https://github.com/lovecy86/Financial-Record-Analysis/blob/main/PyBank/analysis/budget_analysis.txt)

## **Overview**
This Python script analyzes financial records for a company using the budget_data.csv dataset, which contains two columns: Date and Profit/Losses. The script calculates key financial metrics, including the total number of months, net total profits/losses, average change in profits/losses, and the greatest increase and decrease in profits with their corresponding dates. This tool automates financial analysis, providing clear and actionable insights for business decision-making.

## **Prerequisites**
* Python 3.x installed.
* The budget_data.csv dataset, which includes two columns:
    * Date: The date of the financial record.
    * Profit/Losses: The profit or loss amount for that month (integer).
* Basic knowledge of running Python scripts from the command line or an IDE.

## **Analysis**
A Python script is created that analyzes the records to calculate each of the following values:
    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * The changes in "Profit/Losses" over the entire period, and then the average of those changes
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in profits (date and amount) over the entire period

## **Result**
![Result](PyBank/analysis.png)