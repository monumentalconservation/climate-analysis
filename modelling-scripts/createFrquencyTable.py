from base import *

# df must include 'amount' column
def create_frequency_table(df, column):
  df['quantile'] = pd.qcut(df[column],q=10,precision=0)
  df['quantile_no'] = pd.qcut(df[column],q=10,labels=False,precision=0)
  frequency = pd.crosstab(index=df['amount'], columns=df['quantile']) 
  return frequency


def create_relative_freuqncy_table(df):
  ndf = df.copy()
  ndf.columns = [0,1,2,3,4,5,6,7,8,9]
  ndf['0rf'] = ndf.apply(lambda row: row[0]/(ndf[0].sum()), axis = 1) 
  ndf['1rf'] = ndf.apply(lambda row: row[1]/(ndf[1].sum()), axis = 1) 
  ndf['2rf'] = ndf.apply(lambda row: row[2]/(ndf[2].sum()), axis = 1) 
  ndf['3rf'] = ndf.apply(lambda row: row[3]/(ndf[3].sum()), axis = 1) 
  ndf['4rf'] = ndf.apply(lambda row: row[4]/(ndf[4].sum()), axis = 1) 
  ndf['5rf'] = ndf.apply(lambda row: row[5]/(ndf[5].sum()), axis = 1) 
  ndf['6rf'] = ndf.apply(lambda row: row[6]/(ndf[6].sum()), axis = 1) 
  ndf['7rf'] = ndf.apply(lambda row: row[7]/(ndf[7].sum()), axis = 1) 
  ndf['8rf'] = ndf.apply(lambda row: row[8]/(ndf[8].sum()), axis = 1) 
  ndf['9rf'] = ndf.apply(lambda row: row[9]/(ndf[9].sum()), axis = 1) 

  relFre = ndf[['0rf','1rf','2rf','3rf','4rf','5rf','6rf','7rf','8rf','9rf']].copy()

  return relFre


CSVFilename = './measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)
df = data[['date','PET','amount']]

# create frequency table
fre = create_frequency_table(df, 'PET')
# fre.to_csv('for-modeling/freqency.csv')

relFre = create_relative_freuqncy_table(fre)
# relFre.to_csv('for-modeling/relative-freqency.csv')

cum = relFre.cumsum()
cum.columns = ['0','1','2','3','4','5','6','7','8','9']
cum.to_csv('for-modeling/cumulative-freqency.csv')

