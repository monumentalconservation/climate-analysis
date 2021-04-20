from createPredictiveTable import *
# ------------------------------ data ---------------------------

# get original bin edges
CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)
df = data[['date','PET','amount']]
bin_edges = create_bin_edges(df, "PET")


# get culmulative frequency table
CSVFilename = 'for-modeling/cumulative-freqency.csv' ### <<<<< Change this file when needed
cum = pd.read_csv(CSVFilename, index_col=False)



# Get the modelled climate data
CSVFilename = 'climate-data/pet_all.csv'
PETData = createDFFromFile(CSVFilename)
PETData = PETData.drop(['Unnamed: 0'], axis=1)
PETData = PETData.set_index('date')

pred = create_predictive_decade(PETData, '2001', '2010', bin_edges)
# pred.to_csv('predictions/1981-1990.csv')