import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

url         =   'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
#_______________________________Assign it to a variable called chipo____________________________________________________
chipo   =   pd.read_csv(url,delimiter='\t')
#_______________________________See the first 10 entries________________________________________________________________
print(chipo.head(10))
#_______________________________What is the number of observations in the dataset?______________________________________
print(f'Number of observation in dataset = {chipo.shape[0]}')
print(chipo.info())
#_______________________________What is the number of columns in the dataset?___________________________________________
print(f'Number of Column in dataset = {chipo.shape[1]}')
print(chipo.info())
#________________________________Print the name of all the columns______________________________________________________
print(f'Name of Columns are {chipo.columns}')
#________________________________How is the dataset indexed?____________________________________________________________
print(f'Dataset indexed is {chipo.index}\nAs type is {type(chipo.index)}')
#________________________________Which was the most-ordered item?_______________________________________________________
chipo_1                 =   chipo[['item_name','quantity']].groupby('item_name').sum()
chipo_1                 =   chipo_1.sort_values('quantity',ascending=False)
chipo_1['item_name']    =   chipo_1.index
chipo_1                 =   chipo_1.reset_index(drop=True)
print(f'The most-ordered item in item_name has pure data info: {chipo_1.iloc[0]}')
print('The most ordered item in item_name is:',chipo_1.iloc[0]['item_name'],'\nWith the quantity is:',chipo_1.iloc[0]['quantity'])
#________________________________For the most-ordered item, how many items were ordered?________________________________
print('The most ordered item in item_name is:',chipo_1.iloc[0]['item_name'],'\nWith the quantity is:',chipo_1.iloc[0]['quantity'])
#________________________________What was the most ordered item in the choice_description column?_______________________
chipo_2                 =   chipo.groupby('choice_description').sum()
chipo_2                 =   chipo_2.sort_values('quantity',ascending=True)
chipo_2['choice description name']  =   chipo_2.index
print('The most ordered item in choice description is:',chipo_2.iloc[-1]['choice description name'],'\nWith the quantity is:',chipo_2.iloc[-1]['quantity'])
#________________________________How many items were ordered in total?___________________________________________________
print('There are', chipo['quantity'].sum(), 'items were ordered in total')
#________________________________Turn the item price into a float________________________________________________________
print(chipo['item_price'].dtype)

def removeDollarSymbol(obj_):
    cleaned_obj_        =   obj_[1:len(obj_)]
    return cleaned_obj_

chipo['item_price']                       =   chipo['item_price'].apply(removeDollarSymbol)
chipo['item_price']                       =   chipo['item_price'].astype(float)
print(chipo)
#________________________________Check the item price type________________________________________________________________
print(chipo['item_price'].dtype)
#________________________________Create a lambda function and change the type of item price_______________________________
lambda x: float(x[1:len(x)])
#________________________________How much was the revenue for the period in the dataset?__________________________________
chipo['revenue']         =   chipo['quantity'] * chipo['item_price']
print(chipo)
print(f'The revenue for the period in the dataset is',chipo['revenue'].sum())
#________________________________How many orders were made in the period?_________________________________________________
#solution#1
print('There are',chipo['order_id'].iloc[-1],'orders were made in period')
#solution#2 : or (like chipo.index :)) )
orders  =   chipo.order_id.value_counts().count()
print(f'There are {orders} orders were made in period')
#________________________________What is the average revenue amount per order?_____________________________________________
#solution#1
average_revenue =   (chipo.revenue.sum())/(chipo.order_id.value_counts().count())
print(f'The average revenue amount per order is {average_revenue}')
#________________________________How many different items are sold?________________________________________________________
chipo_3                 =   chipo.groupby('item_name').sum()
nos_diff_items          =   chipo_3.shape[0]
print(f'There are {nos_diff_items} different items are sold')
