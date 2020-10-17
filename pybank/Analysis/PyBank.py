# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:35:49 2020

@author: ale_v
"""

#%% File budget
import os
import csv
#%% set path for file
CSVpath = os.path.join("..", "Resources", "budget.csv")
file_to_output=os.path.join("..", "Analysis", "budget.text")
#Financial Parameters
total_months=0
month_of_change=[]
net_change_list=[]
greatest_increase=["",0]
greatest_decrease=['',99999999999]
total_net=0
#read file
with open (CSVpath) as CSVfile:
    CSVreader=csv.reader(CSVfile)
    #read first header
    header=next(CSVreader)
    #extract first row
    first_row = next(CSVreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in CSVreader:
        #track the total
        total_months += 1
        total_net += int(row[1])
        #track the net change
        net_change = int(row[1])-prev_net
        prev_net=int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        #calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase [0]= row[0]
            greatest_increase [1]= net_change
            #calculate decrease 
        if net_change < greatest_decrease [1]:
            greatest_decrease [0]= row[0]
            greatest_decrease [1] = net_change
            #calculate average
net_monthly_avg = sum(net_change_list)/len(net_change_list)
            #generation output summary
output =(
    f"Financial Analysis/n"
    f"-----------------/n"
    f"Total Months: {total_months}/n"
    f"Total: ${total_net}/n"
    f"Average Change: ${net_monthly_avg:.2f}/n"
    f"greatest Increase in Profits: {greatest_increase [0]}, (${greatest_increase [1]})/n"
    f"greatest decrease in profits: {greatest_decrease[0]}, (${greatest_decrease [1]})/n")
                    #print to output
                    #export results
with open (file_to_output, 'w') as text_file:
    text_file.write(output)
                    
                    
            

       
 
         


