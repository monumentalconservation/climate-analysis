from weekBefore import *


# ------------------------------------- GET DATA ----------------------------------- 

CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
observedOnly = createDFFromFile(CSVFilename)



CSVFilename = 'measured-climate-data/measured-with-observed.csv' ### <<<<< Change this file when needed
allData = createDFFromFile(CSVFilename)

# ---------------------------------------- end ---------------------------------------



# --------------------------------------- Rainfall ------------------------------------
# Get the weeks worth of rain for observed amounts
week_rain = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'prcp_amt')

## Seperate data into columns
none, some, a_lot, substantial, extensive = separate_observed_rainfall(week_rain)

plot_average_rainfall(none, some, a_lot, substantial, extensive)
plt.savefig('plots/measured/weekly/week-before-rain-average.png')
# ---------------------------------------- end ---------------------------------------



# ----------------------------------------- Temp -------------------------------------
# Get the weeks worth of rain for observed amounts
week_temp = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'av_temp')

## Seperate data into columns
none, some, a_lot, substantial, extensive = separate_observed_rainfall(week_temp)

plot_average_temp(none, some, a_lot, substantial, extensive)
plt.savefig('plots/measured/weekly/week-before-temp-average.png')
# ---------------------------------------- end ---------------------------------------



# ---------------------------------------- PET ---------------------------------------
# Get the weeks worth of rain for observed amounts
week_PET = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'PET')

## Seperate data into columns
none, some, a_lot, substantial, extensive = separate_observed_rainfall(week_PET)

plot_average_PET(none, some, a_lot, substantial, extensive)
plt.savefig('plots/measured/weekly/week-before-PET-average.png')
# ---------------------------------------- end ---------------------------------------


# ---------------------------------------- REMAINING ----------------------------------
# Get the weeks worth of rain for observed amounts
week_remaining = get_week_before_each_observation(observedOnly, allData, pd.DataFrame(), 'remaining')

## Seperate data into columns
none, some, a_lot, substantial, extensive = separate_observed_rainfall(week_remaining)

plot_remaining(none, some, a_lot, substantial, extensive)
plt.savefig('plots/measured/weekly/week-before-remaining-average.png')
# ---------------------------------------- end ---------------------------------------


# plt.show()