import os
import csv
import math

# variable initialization
totalMonth = 0 
totalNetProfitLoss = 0
changeNetProfitLoss = []
previousMonthProfitLoss = 0
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999999999999]


# path to collect data from budget_data.csvfile 
budgetCsvPath = os.path.join("PyBank", "Resources", "budget_data.csv")

# path to analysis file
analysisFilePath = os.path.join("PyBank", "analysis", "analysis.txt")

# open csv file
with open(budgetCsvPath) as budgetCsvFile:

    # read the csv file
    budgetCsvReader = csv.reader(budgetCsvFile, delimiter=',')
    
    # skip header row
    next(budgetCsvReader)

    # loop through easc row in csv file
    for row in budgetCsvReader:
        # calculate total months
        totalMonth += 1

        # calculate total net profit/loss
        totalNetProfitLoss = totalNetProfitLoss + int(row[1])

        # calculate net change from previous month
        netChange = int(row[1]) - previousMonthProfitLoss
        # add netchange to array for tracking purpose
        changeNetProfitLoss.append(netChange)

        # overwrite previous month value with current month
        previousMonthProfitLoss = int(row[1])

        # if netchange is greater than stored value then replace stored value with current change
        if netChange >greatestIncrease[1]:
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = netChange
        # if netchange is smaller than stored value then replace with current value
        if netChange < greatestDecrease[1]:
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = netChange


    # calculate net monthly avg 
    netMonthlyAvg = sum(changeNetProfitLoss)/len(changeNetProfitLoss)

with open(analysisFilePath, 'w') as analysisFile:
    analysisFile.write("Financial Analysis")
    analysisFile.write("\n----------------------------")
    analysisFile.write("\nTotal Months: " + str(totalMonth))    
    analysisFile.write("\nTotal: " + str(totalNetProfitLoss))
    analysisFile.write(f"\nAverage Change: {netMonthlyAvg:.2f}")
    analysisFile.write("\nGreatest Increase in Profits: " + greatestIncrease[0] + " $" + str(greatestIncrease[1]))
    analysisFile.write("\nGreatest Decrease in Profits: " + greatestDecrease[0] + " $" + "({})".format(math.fabs(greatestDecrease[1])) if greatestDecrease[1] < 0 else "{}".format(greatestDecrease[1]))
    analysisFile.close

with open(analysisFilePath, 'r') as analysisFileReader:
    print(analysisFileReader.read())

