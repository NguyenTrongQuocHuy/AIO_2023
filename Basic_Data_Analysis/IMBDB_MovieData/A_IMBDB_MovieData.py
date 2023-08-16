import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#A.1____________________________________Preparing_data_set____________________________________________
dataset_path    =   'C:/Users/nguye/Desktop/230813_Data_Analysis_Exercise/dataset/IMDB_Movie_Data.csv'
dataset         =   pd.read_csv(dataset_path)                                   #reading data from .csv file
data_indexed    =   pd.read_csv(dataset_path, index_col='Title')                #defined indexed
print(data_indexed)

#A.2____________________________________Wiewing_data_set_5th_top_row__________________________________
print(data_indexed.head(5))
print(data_indexed[0:5])
print(data_indexed.loc['Guardians of the Galaxy':'Suicide Squad'])

#A.3______________________________Understand_basic_infomation_of_data_________________________________
print(data_indexed.info())
print(data_indexed.describe())

#A.4_____________________________Data_Selection_Index_Slicing_Data____________________________________
series_genre            =   data_indexed['Genre']
series_genre.reset_index(drop=True, inplace=True)
print(series_genre)
print(type(series_genre))

dataframe_genre_rating  =   data_indexed[['Genre','Rating']]
dataframe_genre_rating.reset_index(drop=True, inplace=True)
print(dataframe_genre_rating)
print(type(dataframe_genre_rating))

dataframe_rows          =   data_indexed.iloc[10:15]
print(dataframe_rows)
print(type(dataframe_rows))

dataframe_rows_columns  =   data_indexed.iloc[10:15][['Rank','Genre','Description','Director','Votes','Metascore']]
print(dataframe_rows_columns)
print(type(dataframe_rows_columns))

#A.5_____________________________Data_Selection_Based_on_Conditional_Filtering_________________________
filtered_data           =   data_indexed[(data_indexed['Year']>=2010) & (data_indexed['Year']<=2015) & (data_indexed['Rating']<6.0) & (data_indexed['Revenue (Millions)']>data_indexed['Revenue (Millions)'].quantile(0.95))]
print(filtered_data)

#A.6_______________________________________Group_by_Operation___________________________________________
groupby_data            =   data_indexed.groupby(['Director'])[['Rating']].mean()
print(groupby_data)
print(groupby_data.shape)
print(type(groupby_data))

selected_data           =   data_indexed[['Director','Rating']]
groupby_data_new        =   selected_data.groupby(['Director']).mean() 
print('here')
print(groupby_data_new) 
print(groupby_data_new.shape)
print(type(groupby_data_new))

#A.7_______________________________________Sorted_Operation______________________________________________
groupby_data            =   data_indexed.groupby(['Director'])[['Rating']].mean()
sorted_groupby_data     =   groupby_data.sort_values(['Rating'],ascending=False)[0:5]
print(sorted_groupby_data)
print(type(sorted_groupby_data))

selected_data           =   data_indexed[['Director','Rating']]
groupby_data_new        =   selected_data.groupby(['Director']).mean() 
sorted_groupby_data_new =   groupby_data_new.sort_values(['Rating'],ascending=False)[0:5]
print(sorted_groupby_data_new)
print(type(sorted_groupby_data_new))

#A.7_______________________________________Wiew_missing_value____________________________________________
data_null               =   data_indexed.isnull().sum()
print(data_null)

#A.8__________________________________Deal_with_missing_value____________________________________________
#---------------------------------------------------Deleting---------------------------------------------
data_null_deleted       =   data_indexed.dropna()
print(data_null_deleted.isnull().sum())

#----------------------------------------------Filling by interpolate------------------------------------
data_null_interpolate   =   data_indexed.interpolate()
print(data_null_interpolate.isnull().sum())
print(type(data_indexed))
print(data_indexed.isnull().sum())

#------------Filling by defined value (mean,median...etc) by two method (dataframe, series)--------------
revenue_mean            =   data_indexed['Revenue (Millions)'].mean()
metascore_mean          =   data_indexed['Metascore'].mean()
#process by dataframe
data_indexed[['Revenue (Millions)']]        =   data_indexed[['Revenue (Millions)']].fillna(revenue_mean)
data_indexed[['Metascore']]                 =   data_indexed[['Metascore']].fillna(metascore_mean)
print(data_indexed.isnull().sum())
#or process by dataseries
data_indexed['Revenue (Millions)'].fillna(revenue_mean,inplace=True)
data_indexed['Metascore'].fillna(metascore_mean,inplace=True)
print(data_indexed.isnull().sum())

#A.9__________________________________Apply_Function____________________________________________
def rating_group(rating_):
    if rating_ >= 7.5:
        return 'Good'
    elif 6 <= rating_ < 7.5:
        return 'Average'
    else:
        return 'Bad'

rating_group_column    =   data_indexed['Rating'].apply(rating_group)
print(rating_group_column)
data_indexed.insert(data_indexed.shape[1],'rating_group',rating_group_column)

#________________________________________________________________________________________________
data_director_mtscore   =   data_indexed[['Director','Metascore']]
data_director_mtscore   =   data_director_mtscore.groupby('Director').mean()
print(data_director_mtscore)
fig,ax                  =   plt.subplots()
ax.plot(data_director_mtscore.index, data_director_mtscore['Metascore'], c='cyan', lw=1)
plt.show()

