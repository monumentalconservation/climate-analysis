from base import *

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
