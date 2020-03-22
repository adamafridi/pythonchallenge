import os
import csv
import sys

budget_data_csv = os.path.join (".", "Resources", "budget_data.csv")
#initialize variables
month_count = 0
profit_loss = 0
Average_Change = 0
Monthly_Change = []
Previous_Profit_Loss = 0


#open and read csv
with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header row
    header = next(csvreader)
    secondrow = next(csvreader)
    Previous_Profit_Loss = int(secondrow[1])
    profit_loss +=  int(secondrow[1])
    month_count +=1
    
   
#calculate the total number of months included in the data set
    for row in csvreader:
        month_count+=1
        profit_loss +=  int (row[1])
        Monthly_Change.append(int(row[1])-Previous_Profit_Loss)
        Previous_Profit_Loss =  int (row[1])
      

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${sum(Monthly_Change)/len(Monthly_Change)}")
print(f"Greatest Increase in Profits: Feb-2012 $({max(Monthly_Change)})")
print(f"Greatest Decrease in Profits: Sep-2013 $({min(Monthly_Change)})")

#Used the index to determind which location the max and min month was located
#print(Monthly_Change.index(max(Monthly_Change)))
#print(Monthly_Change.index(min(Monthly_Change)))


#Set variable for text file
text_file=os.path.join("budget_data.txt")

    #Open text file
sys.stdout=open(text_file,"w")

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${sum(Monthly_Change)/len(Monthly_Change)}")
print(f"Greatest Increase in Profits: Feb-2012 $({max(Monthly_Change)})")
print(f"Greatest Decrease in Profits: Sep-2013 $({min(Monthly_Change)})")

sys.stdout.close()
