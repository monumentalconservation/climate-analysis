from weekBefore import *
from boxplot import *

# ------------------------------------- GET DATA ----------------------------------- 

CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
observedOnly = createDFFromFile(CSVFilename)


CSVFilename = 'measured-climate-data/measured-with-observed.csv' ### <<<<< Change this file when needed
allData = createDFFromFile(CSVFilename)

# ---------------------------------------- end ---------------------------------------



# --------------------------------------- Rainfall ------------------------------------
# Get the weeks worth of rain for observed amounts
week_rain = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'prcp_amt')
week_rain['sum5day'] = week_rain.apply(lambda row: (row['1'] + row['2'] + row['3'] + row['4'] + row['5']) / 5, axis = 1) 

plot_just_daily_boxplot(week_rain, 'sum5day', "Precipitation (mm)", "Plot of Precipitation (mm)", 'Blues_r')
plt.savefig('plots/measured/boxplot/weekly/week-before-rain-boxplot.png')
# ---------------------------------------- end ---------------------------------------



# ----------------------------------------- Temp -------------------------------------
# Get the weeks worth of rain for observed amounts
week_temp = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'av_temp')
week_temp['sum5day'] = week_temp.apply(lambda row: (row['1'] + row['2'] + row['3'] + row['4'] + row['5']) / 5, axis = 1) 

plot_just_daily_boxplot(week_temp, 'sum5day', "Temperature (c)", "Plot of daily temperature when image taken", 'autumn')
plt.savefig('plots/measured/boxplot/weekly/week-before-temp-boxplot.png')
# ---------------------------------------- end ---------------------------------------



# ---------------------------------------- PET ---------------------------------------
# Get the weeks worth of rain for observed amounts
week_PET = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'PET')
week_PET['sum5day'] = week_PET.apply(lambda row: (row['1'] + row['2'] + row['3'] + row['4'] + row['5']) / 5, axis = 1) 

plot_just_daily_boxplot(week_PET, 'sum5day', "PET", "Plot of daily PET levels when image taken", 'rocket')
plt.savefig('plots/measured/boxplot/weekly/week-before-PET-boxplot.png')
# ---------------------------------------- end ---------------------------------------


# ---------------------------------------- REMAINING ----------------------------------
# Get the weeks worth of rain for observed amounts
week_remaining = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'remaining')
week_remaining['sum5day'] = week_remaining.apply(lambda row: (row['1'] + row['2'] + row['3'] + row['4'] + row['5']) / 5, axis = 1) 

plot_just_daily_boxplot(week_remaining, 'sum5day', "Remaining (mm)", "Plot of remaining (mm)  when image taken", 'viridis')
plt.savefig('plots/measured/boxplot/weekly/week-before-remaining-boxplot.png')
# ---------------------------------------- end ---------------------------------------



# import code; code.interact(local=dict(globals(), **locals()))
