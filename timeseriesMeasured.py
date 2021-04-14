from base import *
from timeseries import plot_timeseries


# ------------------------------------ FANGANGLE DATA ------------------------------------
## Get combined data into DF
CSVFilename = 'measured-climate-data/measured-with-observed.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)

data.date = pd.to_datetime(data.date, dayfirst=True)
data = data.set_index('date')

dataConcat = pd.concat([data['June 2017':'Dec 2020']])
# import code; code.interact(local=dict(globals(), **locals()))
# ----------------------------------------- end --------------------------------------------

# ------------------------------------ June 2017 - 2018 ------------------------------------
dataConcat2017 = pd.concat([data['June 2017':'June 2018']])
# ----------------------------------------- end --------------------------------------------


# ------------------------------------ September 2019 - 2020 -------------------------------
dataConcat2019 = pd.concat([data['September 2019':'September 2020']])
# ----------------------------------------- end --------------------------------------------








# ------------------------------- Plot rainfall timeseries --------------------------------
plot_timeseries(dataConcat, 'prcp_amt', 'Precipitation (mm)', '#2660A4', False)
plt.savefig('plots/measured/timeseries/observerved-rain-timeseries.png')

plot_timeseries(dataConcat2017, 'prcp_amt', 'Precipitation (mm)', '#2660A4', True)
plt.savefig('plots/measured/timeseries/observerved-rain-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'prcp_amt', 'Precipitation (mm)', '#2660A4', True)
plt.savefig('plots/measured/timeseries/observerved-rain-timeseries-2019.png')

# ----------------------------------------- end --------------------------------------------

# ------------------------------- Plot temp timeseries --------------------------------
plot_timeseries(dataConcat, 'av_temp', 'Temperature (c)', '#62A8AC', False)
plt.savefig('plots/measured/timeseries/observerved-temp-timeseries.png')

plot_timeseries(dataConcat2017, 'av_temp', 'Temperature (c)', '#62A8AC', True)
plt.savefig('plots/measured/timeseries/observerved-temp-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'av_temp', 'Temperature (c)', '#62A8AC', True)
plt.savefig('plots/measured/timeseries/observerved-temp-timeseries-2019.png')
# ----------------------------------------- end --------------------------------------------

# ------------------------------- Plot PET timeseries --------------------------------
plot_timeseries(dataConcat, 'PET', 'PET', '#3B3561', False)
plt.savefig('plots/measured/timeseries/observerved-pet-timeseries.png')

plot_timeseries(dataConcat2017, 'PET', 'PET', '#3B3561', True)
plt.savefig('plots/measured/timeseries/observerved-pet-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'PET', 'PET', '#3B3561', True)
plt.savefig('plots/measured/timeseries/observerved-pet-timeseries-2019.png')
# ----------------------------------------- end --------------------------------------------

# ------------------------------- Plot remaining timeseries --------------------------------
plot_timeseries(dataConcat, 'remaining', 'Remaining (mm)', '#52c468', False)
plt.savefig('plots/measured/timeseries/observerved-remaining-timeseries.png')

plot_timeseries(dataConcat2017, 'remaining', 'Remaining (mm)', '#52c468', True)
plt.savefig('plots/measured/timeseries/observerved-remaining-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'remaining', 'Remaining (mm)', '#52c468', True)
plt.savefig('plots/measured/timeseries/observerved-remaining-timeseries-2019.png')
# ----------------------------------------- end --------------------------------------------