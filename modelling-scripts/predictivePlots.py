from base import *

CSVFilename = 'predictions/1981-1990.csv' ### <<<<< Change this file when needed
p1981 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/1991-2000.csv' ### <<<<< Change this file when needed
p1991 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2001-2010.csv' ### <<<<< Change this file when needed
p2001 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2011-2020.csv' ### <<<<< Change this file when needed
p2011 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2021-2030.csv' ### <<<<< Change this file when needed
p2021 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2031-2040.csv' ### <<<<< Change this file when needed
p2031 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2041-2050.csv' ### <<<<< Change this file when needed
p2041 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2051-2060.csv' ### <<<<< Change this file when needed
p2051 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2061-2070.csv' ### <<<<< Change this file when needed
p2061 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/2071-2080.csv' ### <<<<< Change this file when needed
p2071 = pd.read_csv(CSVFilename, index_col=False)

CSVFilename = 'predictions/measured-2011-2020.csv' ### <<<<< Change this file when needed
measured = pd.read_csv(CSVFilename, index_col=False)

# Get all teh value counts together to compare
data = {
  '1981':  p1981['mode'].value_counts(),
  '1991':  p1991['mode'].value_counts(),
  '2001':  p2001['mode'].value_counts(),
  '2011':  p2011['mode'].value_counts(),
  '2021':  p2021['mode'].value_counts(),
  '2031':  p2031['mode'].value_counts(),
  '2041':  p2041['mode'].value_counts(),
  '2051':  p2051['mode'].value_counts(),
  '2061':  p2061['mode'].value_counts(),
  '2071':  p2071['mode'].value_counts(),
}

df = pd.DataFrame(data)


import code; code.interact(local=dict(globals(), **locals()))
# Split ranks b season to compare


