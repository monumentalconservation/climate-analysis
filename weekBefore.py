from base import *


# iterate through each row in observed rainfall, find the same date in given weather type data
# and find the last 7 days. then save it 
def get_week_before_each_observation(observed_weather_df, measured_weather_df, newdf, specific_weather_column_name):
    for index, row in observed_weather_df.iterrows():

        rain_date = measured_weather_df.loc[measured_weather_df['date'] == row['date']]

        if not rain_date.empty:
            ## get time series
            end = rain_date.index[0]
            start = end - 7
            series = measured_weather_df.iloc[start:end][specific_weather_column_name]
            
            columns = ['amount','1','2','3','4','5','6','7']
            data = [row['amount']] + series.tolist()

            # create new dataframe
            ndf = pd.DataFrame([data],columns=columns)

            # adds it to the combined one
            newdf = newdf.append(ndf, ignore_index=True) 

    return newdf



# Seprate observed rainfall and it's 7 days weather into 5 different dfs
def separate_observed_rainfall(weeklydf):
    none = weeklydf.loc[weeklydf['amount'] == 1]
    some = weeklydf.loc[weeklydf['amount'] == 2]
    a_lot = weeklydf.loc[weeklydf['amount'] == 3]
    substantial = weeklydf.loc[weeklydf['amount'] == 4]
    extensive = weeklydf.loc[weeklydf['amount'] == 5]

    none = none.drop(columns=['amount'])
    some = some.drop(columns=['amount'])
    a_lot = a_lot.drop(columns=['amount'])
    substantial = substantial.drop(columns=['amount'])
    extensive = extensive.drop(columns=['amount'])

    return none, some, a_lot, substantial, extensive


## plots the average of all rainfall
def plot_average_rainfall(none, some, a_lot, substantial, extensive):
	fig, ax = plot_styles()

	plt.xticks([0, 1, 2,3,4,5,6],['6','5','4','3','2','1','Image taken'], fontsize=14)
	plt.yticks(range(0, 20, 1), fontsize=14)
	ax.set_xlabel('Days before image taken')
	ax.set_ylabel('Daily rainfall (mm)')
	ax.set_title('Average daily rainfall over week before images taken')
	plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

	# Actually plot the stuff
	plt.plot(none.columns, none.mean(), color='#225b91',lw=2.5, label='none')
	plt.plot(some.columns, some.mean(), color='#4884af',lw=2.5, label='some')
	plt.plot(some.columns, a_lot.mean(), color='#79abc9',lw=2.5, label='a lot')
	plt.plot(some.columns, substantial.mean(), color='#b3cede',lw=2.5, label='substantial')
	plt.plot(some.columns, extensive.mean(), color='#dae6f1',lw=2.5, label='extensive')

	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles, labels, loc='center right',bbox_to_anchor=(1.1, 0.5))



## plots the average of the temperature for each category
def plot_average_temp(none, some, a_lot, substantial, extensive):
	fig, ax = plot_styles()

	plt.xticks([0, 1, 2,3,4,5,6],['6','5','4','3','2','1','Image taken'], fontsize=14)
	# plt.yticks(np.arange(0, 5, 1), fontsize=14)
	# ax.set(xlim=(0, 7), ylim=(2.5, 5.5))
	ax.set_xlabel('Days before image taken')
	ax.set_ylabel('Daily max temp (c)')
	ax.set_title('Average daily temperature over week before images taken')
	plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
	
	ax.spines['bottom'].set_visible(True)
	ax.spines['bottom'].set_linewidth(0.5)

	# Actually plot the stuff
	plt.plot(none.columns, none.mean(), color='#df3f20',lw=2.5, label='none')
	plt.plot(some.columns, some.mean(), color='#df6020',lw=2.5, label='some')
	plt.plot(some.columns, a_lot.mean(), color='#df8020',lw=2.5, label='a lot')
	plt.plot(some.columns, substantial.mean(), color='#df9f1f',lw=2.5, label='substantial')
	plt.plot(some.columns, extensive.mean(), color='#dfc01f',lw=2.5, label='extensive')

	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles, labels, loc='center right',bbox_to_anchor=(1.1, 0.5))


def plot_average_PET(none, some, a_lot, substantial, extensive):
	fig, ax = plot_styles()

	ax.spines['bottom'].set_visible(True)
	ax.spines['left'].set_visible(True)

	plt.xticks([0, 1, 2,3,4,5,6],['6','5','4','3','2','1','Image taken'], fontsize=14)
	ax.set_xlabel('Days before image taken')
	ax.set_ylabel('Daily PET (mm)')
	ax.set_title('Daily PET for week before images taken')
	plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

	# Actually plot the stuff
	plt.plot(none.columns, none.mean(), color='#e8af92',lw=2.5, label='none')
	plt.plot(some.columns, some.mean(), color='#db6e59',lw=2.5, label='some')
	plt.plot(a_lot.columns, a_lot.mean(), color='#b43058',lw=2.5, label='a lot')
	plt.plot(substantial.columns, substantial.mean(), color='#772b58',lw=2.5, label='substantial')
	plt.plot(extensive.columns, extensive.mean(), color='#3b203e',lw=2.5, label='extensive')

	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles, labels, loc='center right',bbox_to_anchor=(1.1, 0.5))


def plot_remaining(none, some, a_lot, substantial, extensive):
	fig, ax = plot_styles()

	ax.spines['bottom'].set_visible(True)
	ax.spines['left'].set_visible(True)

	plt.xticks([0,1,2,3,4,5,6],['6','5','4','3','2','1','Image taken'], fontsize=14)
	ax.set_xlabel('Days before image taken')
	ax.set_ylabel('Water remaining (mm)')
	ax.set_title('Daily water remaining for week before images taken')
	plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

	# Actually plot the stuff
	plt.plot(none.columns, none.mean(), color='#471669',lw=2.5, label='none')
	plt.plot(some.columns, some.mean(), color='#37588c',lw=2.5, label='some')
	plt.plot(a_lot.columns, a_lot.mean(), color='#20968b',lw=2.5, label='a lot')
	plt.plot(substantial.columns, substantial.mean(), color='#5fc961',lw=2.5, label='substantial')
	plt.plot(extensive.columns, extensive.mean(), color='#eee519',lw=2.5, label='extensive')

	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles, labels, loc='center right',bbox_to_anchor=(1.1, 0.5))