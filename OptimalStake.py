
#imports the required library for the script
from openpyxl import load_workbook;
import scipy.stats
from decimal import *

#loads the correct excel workbook and sheet (Currently a spreadsheet with random values between 0 and 60)_
#need to replace this with actual football game data showing the average time a goal is scored after another goal

wb = load_workbook(filename = '/Users/Josh/Python_test.xlsx')
ws = wb['Data']

#creates a python list (called data) from a column in excel

data = []

for col in ws.columns[0]:
    data.append(col.value)

#sigtime tells me what percentage of the time a goal is scored in the ten minutes preceding a goal
#(versus all the times to next goal). We will want to know this in order to deduce our optimal bet size for each bet,
#as the starting point will be for example 'I am willing to lose half my total account value in a tail risk scenario with an expected
#frequency of 5%, where x consecutive bets go against me (defined by sigtime)'.

sigtime = Decimal(scipy.stats.percentileofscore(data,10)/100)
print(sigtime)

#Looks at account value. Currently set to £100 default but can be called with betfair wrapper.

Freq = Decimal(0.05)
AccountVal = 100
Acceptedloss = Decimal(0.5)

stakeval = Decimal((AccountVal * Acceptedloss)/ (sigtime / Freq))

print(stakeval)
