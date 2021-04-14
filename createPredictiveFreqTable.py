from base import *

def get_rank(number, ranked_series):
  if number > 0 and number < ranked_series[0]:
    rank = 1
  elif (number > ranked_series[0]) and (number < ranked_series[1]):
    rank = 2
  elif number > ranked_series[1] and number < ranked_series[2]:
    rank = 3
  elif number > ranked_series[2] and number < ranked_series[3]:
    rank = 4
  elif number > ranked_series[3] and number < ranked_series[4]:
    rank = 5
  else:
    print("something went wrong!")
  return rank

# is given a bin number - returns likely rank according to random number
def predict_rank(row):
    number = random.uniform(0, 1)
    cbin = str(int(row))

    ranked_series = cum[cbin]
    rank = get_rank(number, ranked_series)
    return rank



# ------------------------------ data ---------------------------

# get original bin edges
CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)
df = data[['date','PET','amount']]
results, bin_edges = pd.qcut(df["PET"],q=10,labels=False,precision=0,retbins=True)

# get culmulative frequency table
CSVFilename = 'for-modeling/cumulative-freqency.csv' ### <<<<< Change this file when needed
cum = pd.read_csv(CSVFilename, index_col=False)



# Get the modelled climate data
CSVFilename = 'climate-data/pet_all.csv'
PETData = createDFFromFile(CSVFilename)
PETData = PETData.drop(['Unnamed: 0'], axis=1)
PETData = PETData.set_index('date')

# select only the decade we want
dataConcat = pd.concat([PETData['Jan 2080':'Dec 2089']])

# Create new df and preds
nConcat = df[['date']]




# iterate over the bin
for x in ['1','2','3','4','5','6','7','8','9','10','11','12']:
    print(x)
    # Assign it to abin - accodring to the first threshold
    binName = 'bin-' + x
    predName = 'pred-' + x
    dataConcat[binName] = pd.cut(dataConcat[x], bins=bin_edges, labels=False, include_lowest=True)
    dataConcat = dataConcat.dropna()  
    dataConcat[predName] = dataConcat.apply(lambda row: predict_rank(row[binName]), axis=1)

preds = dataConcat[['pred-1','pred-2','pred-3','pred-4','pred-5','pred-6','pred-7','pred-8','pred-9','pred-10','pred-11','pred-12']]
preds['mode'] = preds.mode(axis=1)[0]
pred = preds[['mode']]

pred.to_csv('predictions/2080-2089.csv')
# import code; code.interact(local=dict(globals(), **locals()))







