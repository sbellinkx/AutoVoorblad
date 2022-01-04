from openpyxl import Workbook
import os
import pandas as pd 
cwd = os.path.abspath('') 
files = os.listdir(cwd) 

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

df = pd.DataFrame()
for file in files: 
    if file.endswith(".xlsx"):
        df = df.append(pd.read_excel(file), ignore_index=True)
df.Head()

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)