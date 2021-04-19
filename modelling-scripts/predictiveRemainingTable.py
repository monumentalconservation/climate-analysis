from createPredictiveTable import *


# ------------------------------ data ---------------------------

# get original bin edges
CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)
df = data[['date','remaining','amount']]
bin_edges = create_bin_edges(df, "remaining")


# get culmulative frequency table
CSVFilename = 'for-modeling/cumulative-freqency-remaining.csv' ### <<<<< Change this file when needed
cum = pd.read_csv(CSVFilename, index_col=False)


# Get the modelled climate data
CSVFilename = 'climate-data/remaining_all.csv'
weatherData = createDFFromFile(CSVFilename)
weatherData = weatherData.drop(['Unnamed: 0'], axis=1)
weatherData = weatherData.set_index('date')


pred = create_predictive_decade(weatherData, '2001', '2010', bin_edges)

pred.to_csv('predictions/remaining/1991-2000.csv')




