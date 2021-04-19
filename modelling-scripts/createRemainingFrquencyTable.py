from base import *
from createFrquencyTable import create_frequency_table, create_relative_freuqncy_table


CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)
df = data[['date','remaining','amount']]

# create frequency table
fre = create_frequency_table(df, 'remaining')
# fre.to_csv('for-modeling/freqency.csv')

relFre = create_relative_freuqncy_table(fre)
# relFre.to_csv('for-modeling/relative-freqency.csv')

cum = relFre.cumsum()
cum.columns = ['0','1','2','3','4','5','6','7','8','9']
# cum.columns = ['0','1','2','3','4','5','6']
cum.to_csv('for-modeling/cumulative-freqency-remaining.csv')



  
