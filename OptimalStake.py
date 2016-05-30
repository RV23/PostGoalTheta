
#imports the required library for the script
from openpyxl import load_workbook;
import scipy.stats


#loads the correct excel workbook and sheet (Currently a spreadsheet with random values between 0 and 60)_
#need to replace this with actual football game data showing the average time a goal is scored after another goal

wb = load_workbook(filename = '/Users/Josh/Python_test.xlsx')
ws = wb['Data']

#creates a python list from a column in excel

data = []

for col in ws.columns[0]:
    data.append(col.value)

#sigtime tells me what percentage of the time a goal is scored in the ten minutes preceding a goal

sigtime = scipy.stats.percentileofscore(data,10)
print(sigtime)