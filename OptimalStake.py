
#imports the required library for the script
from openpyxl import load_workbook;
import scipy.stats


#loads the correct excel workbook and sheet (Currently a spreadsheet with random values between 0 and 60 in column A of 'Data tab)
#need to replace this with actual football game data showing the average time a goal is scored after another goal

wb = load_workbook(filename = '/Users/Josh/Python_test.xlsx')
ws = wb['Data']

#creates a python list called 'data' from a column in excel

data = []

for col in ws.columns[0]:
    data.append(col.value)

#sigtime tells me what percentile of the distribution a goal is scored in the ten minutes preceding a goal
#(versus all the times to next goal). We will want to know this in order to deduce our optimal bet size for each bet,
#as the starting point will be for example 'I am willing to lose half my total account value in a tail risk scenario with an expected 
#frequency of 5%, where 4 consecutive bets go against me'. 

sigtime = scipy.stats.percentileofscore(data,10)
print(sigtime)
