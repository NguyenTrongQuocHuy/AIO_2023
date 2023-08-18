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
#solution1
print(f'there are {len(set(occupation_data.occupation))} occupations in the dataset')
#solution2
print(f'there are {occupation_data.occupation.nunique()} occupations in the dataset')

#______________________________________________Step 13. What is the most frequent occupation?_____________________________________________
lst_freq_in_occupation          =   occupation_data.occupation.value_counts()
the_most_freq_in_occupation     =   lst_freq_in_occupation.head(1)
print(f'The most frequent occupation is {the_most_freq_in_occupation.index[0]}, it has {the_most_freq_in_occupation[0]} times')

#______________________________________________Step 14. Summarize the DataFrame.__________________________________________________________
print(occupation_data.describe()) #notice: by default only numeric column is/are returned

#______________________________________________Step 15. Summarize all the columns_________________________________________________________
print(occupation_data.describe(include = 'all')) #notice: if include all, all columns is/are returned

#______________________________________________Step 16. Summarize only the occupation column______________________________________________
print(occupation_data.occupation.describe())

#______________________________________________Step 17. What is the mean age of users?____________________________________________________
print(f'The mean age of user is {occupation_data.age.mean()} yo')

#______________________________________________Step 18. What is the age with least occurrence?____________________________________________
least_freq_age             =   occupation_data.age.value_counts().tail() #tail in default will select 5 bottoms
print(f'The age with least occurrence is/are {least_freq_age.index[0]}')