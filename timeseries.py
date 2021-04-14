# Timeseries for rain, temp and PET with observed

from base import *




# Plot temp across whole year
def plot_timeseries(data, column_name, label, color, section):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    data.reset_index()
    ax.scatter(data.index, data['amount'], s = 30, color = '#F18805', alpha = 0.75, label="Observed")
    ax.set_xlabel('Date')
    ax.set_ylabel('Observed water level')
    fig.autofmt_xdate()
    # fig.set_size_inches(18.5, 10.5)
    ax.invert_yaxis()

    # set interval on y axis - 
    loc = ticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals
    ax.yaxis.set_major_locator(loc)

    ax2 = ax.twinx()
    # put weather data here!
    ax2.plot(data.index, data[column_name], color = color, label=label)
    ax2.set_ylabel(label, color=color)
    if section == False:
        # highlight section of plot
        ax2.axvspan(date2num(datetime(2018,7,1)), date2num(datetime(2019,8,1)), 
                label="Project not running",color="#F0A202", alpha=0.3)

    lines_1, labels_1 = ax.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    # Put a legend in
    ax2.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.45, 1.12),
            fancybox=False, ncol=5)




# ------------------------------------ FANGANGLE DATA ------------------------------------
## Get combined data into DF
CSVFilename = 'climate-data/combined_with_observed.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)
data = data.drop(['Unnamed: 0'], axis=1)
data.date = pd.to_datetime(data.date, dayfirst=True)
data = data.set_index('date')

dataConcat = pd.concat([data['June 2017':'Dec 2020']])
# ----------------------------------------- end --------------------------------------------

# ------------------------------------ June 2017 - 2018 ------------------------------------
dataConcat2017 = pd.concat([data['June 2017':'September 2018']])
# ----------------------------------------- end --------------------------------------------


# ------------------------------------ September 2019 - 2020 -------------------------------
dataConcat2019 = pd.concat([data['September 2019':'September 2020']])
# ----------------------------------------- end --------------------------------------------





# ------------------------------- Plot rainfall timeseries --------------------------------
plot_timeseries(dataConcat, 'prcp_amt', 'Precipitation (mm)', '#2660A4', False)
plt.savefig('plots/modelled/timeseries/observerved-rain-timeseries.png')

plot_timeseries(dataConcat2017, 'prcp_amt', 'Precipitation (mm)', '#2660A4', True)
plt.savefig('plots/modelled/timeseries/observerved-rain-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'prcp_amt', 'Precipitation (mm)', '#2660A4', True)
plt.savefig('plots/modelled/timeseries/observerved-rain-timeseries-2019.png')

# ----------------------------------------- end --------------------------------------------

# ------------------------------- Plot temp timeseries --------------------------------
plot_timeseries(dataConcat, 'av_temp', 'Temperature (c)', '#62A8AC', False)
plt.savefig('plots/modelled/timeseries/observerved-temp-timeseries.png')

plot_timeseries(dataConcat2017, 'av_temp', 'Temperature (c)', '#62A8AC', True)
plt.savefig('plots/modelled/timeseries/observerved-temp-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'av_temp', 'Temperature (c)', '#62A8AC', True)
plt.savefig('plots/modelled/timeseries/observerved-temp-timeseries-2019.png')
# ----------------------------------------- end --------------------------------------------

# ------------------------------- Plot PET timeseries --------------------------------
plot_timeseries(dataConcat, 'PET', 'PET', '#3B3561', False)
plt.savefig('plots/modelled/timeseries/observerved-pet-timeseries.png')

plot_timeseries(dataConcat2017, 'PET', 'PET', '#3B3561', True)
plt.savefig('plots/modelled/timeseries/observerved-pet-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'PET', 'PET', '#3B3561', True)
plt.savefig('plots/modelled/timeseries/observerved-pet-timeseries-2019.png')
# ----------------------------------------- end --------------------------------------------


# ------------------------------- Plot remaining timeseries --------------------------------
plot_timeseries(dataConcat, 'remaining', 'Remaining water (m)', '#52c468', False)
plt.savefig('plots/modelled/timeseries/observerved-remaining-timeseries.png')

plot_timeseries(dataConcat2017, 'remaining', 'Remaining water (m)', '#52c468', True)
plt.savefig('plots/modelled/timeseries/observerved-remaining-timeseries-2017.png')

plot_timeseries(dataConcat2019, 'remaining', 'Remaining water (m)', '#52c468', True)
plt.savefig('plots/modelled/timeseries/observerved-remaining-timeseries-2019.png')
# ----------------------------------------- end --------------------------------------------


# plt.show()