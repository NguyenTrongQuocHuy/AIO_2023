#______________________________________________Step 1. Import the necessary libraries_____________________________________________________
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#______________________________________________Step 2. Import the dataset from this url___________________________________________________
url                         =   'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
occupation_data             =   pd.read_csv(url, delimiter='|')
#print(pure_data)

#______________________________________________Step 3. Assign it to a variable called users and use the 'user_id' as index________________
occupation_data             =   occupation_data.set_index('user_id')
#print(pure_data)

#______________________________________________Step 4. See the first 25 entries___________________________________________________________
print(occupation_data.head(25))

#______________________________________________Step 5. See the last 10 entries____________________________________________________________
print(occupation_data.iloc[occupation_data.shape[0]-10:occupation_data.shape[0]])
print(occupation_data.tail(10))
#______________________________________________Step 6. What is the number of observations in the dataset?_________________________________
print(f'Number of observation in dataset is {occupation_data.shape[0]}')

#______________________________________________Step 7. What is the number of columns in the dataset?______________________________________
print(f'Number of column in dataset is {occupation_data.shape[1]}')

#______________________________________________Step 8. Print the name of all the columns._________________________________________________
print(f'Name of all columns in dataset are {occupation_data.columns}')

#______________________________________________Step 9. How is the dataset indexed?________________________________________________________
print(f'Dataset was indexed as {occupation_data.index}')

#______________________________________________Step 10. What is the data type of each column?_____________________________________________
print(f'The datatype of each column are\n {occupation_data.dtypes}')

#______________________________________________Step 11. Print only the occupation column__________________________________________________
print(f'The occupation column is', occupation_data.occupation)

#______________________________________________Step 12. How many different occupations are in this dataset?_______________________________
