import os
import csv

budget_data_csv = os.path.join (".", "Resources", "budget_data.csv")
month_count = 0
profit_loss = 0
Average Change = 0
#open and read csv
with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header row
    header = next(csvreader)
    #calculate the total number of months included in the data set
    for row in csvreader:
        month_count+=1
        profit_loss +=  int (row[1])
        average change = - (row[1])
#print(month_count)
#print(profit_loss)
print(average)
print(f"Total Months: {month_count}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ")





  
 
    
