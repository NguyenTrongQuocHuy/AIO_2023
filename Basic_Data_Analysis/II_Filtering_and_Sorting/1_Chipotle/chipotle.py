#_________________________________________________________Step 1. Import the necessary libraries_________________________________________________
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#_________________________________________________________Step 2. Import the dataset from this [address]_________________________________________
#_________________________________________________________Step 3. Assign it to a variable called chipo.__________________________________________
url                     =   'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo                   =   pd.read_csv(url,delimiter='\t')
print(chipo)

#_________________________________________________________Step 4. How many products cost more than $10.00?_______________________________________
def deleteSymbol(price_):
    price_  =   price_[1:len(price_)]
    price_  =   float(price_)
    return price_

chipo['item_price']         =   chipo['item_price'].apply(deleteSymbol)
#solution1
print('Products has cost more than $10.00 are',(chipo[(chipo['item_price']>10)].groupby('item_price').sum()).shape[0])
#solution2
chipo_filtered              =   chipo.drop_duplicates('item_price')
print('Products has cost more than $10.00 are', chipo_filtered[(chipo['item_price']>10)].shape[0])

#_________________________________________________________Step 5. What is the price of each item?_____________________________________________
#_________________________________________________________print a data frame with only two columns item_name and item_price___________________
chipo_stp5                  =   chipo[['item_name','item_price']].set_index('item_name').drop_duplicates('item_price')
print(chipo_stp5)

#_________________________________________________________Step 6. Sort by the name of the item________________________________________________
chipo_stp6                  =   chipo.sort_values('item_name')
print(chipo_stp6)

#_________________________________________________________Step 7. What was the quantity of the most expensive item ordered?___________________
chipo_stp7                  =   chipo.sort_values('item_price',ascending=True)
print('The quantity of the most expensive item ordered is', int(chipo_stp7.tail(1).quantity.values))

#_________________________________________________________Step 8. How many times was a Veggie Salad Bowl ordered?_____________________________
print('Veggie Salad Bowl was order', chipo[(chipo['item_name']=='Veggie Salad Bowl')].shape[0],' times')

#_________________________________________________________Step 9. How many times did someone order more than one Canned Soda?_________________
print('someone order more than one Canned Soda', chipo[(chipo['item_name']=='Canned Soda') & (chipo['quantity']>1)].shape[0],' times')

