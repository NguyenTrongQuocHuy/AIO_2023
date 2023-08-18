import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class PandasDataAnalysisModule():
    def __init__(self,data_path_, index_label_, date_time_coverter_):
        self.data_path_             =   data_path_
        self.index_label_           =   index_label_
        self.date_time_coverter_    =   date_time_coverter_
        
    def prepareData(self):
        data_           =   pd.read_csv(self.data_path_)
        data_           =   data_.set_index(self.index_label_)
        if self.date_time_coverter_ == 1:
            data_.index =   pd.to_datetime(data_.index)
            return data_
        else:
            return data_
        
    def dataInfo(self):
        info_           =     self.prepareData().info()
        return info_

    def dataDescribe(self):
        describe_       =   self.prepareData().describe()
        return describe_
    

data_path   =   'opsd_germany_daily.csv'
data        =   PandasDataAnalysisModule(data_path, 'Date', 1)
#________________________________Normalize_Data___________________________________
opsd_daily  =   data.prepareData()
#______________________________Insert_some_columns_________________________________
opsd_daily['Year']      =   opsd_daily.index.year
opsd_daily['Month']     =   opsd_daily.index.month
opsd_daily['Week_Day']  =   opsd_daily.index.day_name()
#__________________________Describe_Info_SomeBasicParameters______________________
print(opsd_daily.describe())
print(opsd_daily.info())
#______________________________Conditional_Filtering______________________________
opsd_daily_conditional   =   opsd_daily[(opsd_daily['Consumption']>1000) & (opsd_daily['Year']>2015) & (opsd_daily['Wind']>opsd_daily['Wind'].quantile(0.95))]
print(opsd_daily_conditional)
opsd_daily['(Wind+Solar)/(Consumption)']    =   opsd_daily['Wind+Solar']/opsd_daily['Consumption']
print(opsd_daily)
#______________________________GroupBy_and_Evaluate_______________________________
opsd_daily_groupby_meanyear     =   opsd_daily[['Consumption','Wind','Solar','Wind+Solar','Year','(Wind+Solar)/(Consumption)']].groupby(['Year']).mean()
print(opsd_daily_groupby_meanyear)

def evaluateConsumption(year_consumption_):
    if year_consumption_ >= 1300 and year_consumption_ <= 1350:
        return 'normal'
    elif year_consumption_ > 1350:
        return 'too much'
    else:
        return 'low'
    
opsd_daily_groupby_meanyear['Evaluate Consumption']    =   opsd_daily_groupby_meanyear['Consumption'].apply(evaluateConsumption)
print(opsd_daily_groupby_meanyear)

#________________________Visualize_Time_Series_data_______________________________
fig, (ax0, ax1, ax2)         =   plt.subplots(3,1,layout='constrained',sharex=True)

ax0.plot(opsd_daily.index, opsd_daily['Consumption'], color='darkgreen', lw=0.5)
ax0.set_ylabel('GWh')
ax0.set_title('Total Power Consumption')

ax1.plot(opsd_daily.index, opsd_daily['Solar'], color='darkorange', lw=0.5)
ax1.set_ylabel('GWh')
ax1.set_title('Solar Power Consumption')

ax2.plot(opsd_daily.index, opsd_daily['Wind'], color='cyan', lw=0.5)
ax2.set_ylabel('GWh')
ax2.set_title('Wind Power Consumption')

plt.show()

#___________________________________Seasonality____________________________________________
opsd_daily_groupby_month    =   opsd_daily[['Consumption','Wind','Solar','Wind+Solar','Month','(Wind+Solar)/(Consumption)']]
opsd_daily_groupby_month    =   opsd_daily_groupby_month.set_index('Month')
print(opsd_daily_groupby_month)

figure, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

sns.set_theme(style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

sns.boxplot(x=opsd_daily_groupby_month.index,y=opsd_daily_groupby_month['Consumption'],palette="Spectral",ax=ax1)
ax1.set_ylabel("Total")

sns.boxplot(x=opsd_daily_groupby_month.index,y=opsd_daily_groupby_month['Solar'],palette="flare",ax=ax2)
ax2.set_ylabel("Solar")

sns.boxplot(x=opsd_daily_groupby_month.index,y=opsd_daily_groupby_month['Wind'],palette="husl",ax=ax3)
ax3.set_ylabel("Wind")

plt.show()

print(opsd_daily_groupby_month.describe())
#_____________________________________Frequencies___________________________________________
times_sample            =   pd.to_datetime(['2016-02-05', '2016-02-10', '2016-02-15'])

consump_sample          =   opsd_daily.loc[times_sample,['Consumption']].copy()

consump_freq            =   consump_sample.asfreq('D')

consump_freq['Forward_fill']   =   consump_freq.fillna(method='ffill')
print(consump_freq)
#______________________________________Resampling____________________________________________
opsd_daily_annual       =   opsd_daily[['Consumption','Wind','Solar','Wind+Solar','(Wind+Solar)/(Consumption)']].resample('Y').mean()
print(opsd_daily_annual)

#________________________________________Rolling_____________________________________________
opsd_daily_new          =   opsd_daily[['Consumption','Wind','Solar','Wind+Solar','(Wind+Solar)/(Consumption)']]
print(opsd_daily_new)

opsd_rolling_7d         =   opsd_daily_new['Consumption'].rolling(window=7,center=True,min_periods=7).mean().copy()
opsd_rolling_annual     =   opsd_daily_new['Consumption'].rolling(window=365,center=True,min_periods=365).mean().copy()

plt.plot(opsd_daily_new.index,opsd_daily_new['Consumption'],marker='.',color='cyan',markersize=2)
plt.plot(opsd_rolling_7d.index,opsd_rolling_7d,color='deeppink')
plt.plot(opsd_rolling_annual.index,opsd_rolling_annual,color='blue')
plt.show()


sns.set_theme(style="whitegrid")
sns.pairplot(opsd_daily[['Consumption','Wind','Solar','Wind+Solar','Year']], hue="Year", palette = "tab10")
plt.show()
