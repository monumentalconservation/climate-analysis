import matplotlib.pyplot as plt
import numpy as np
import csv 
import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime
import seaborn as sns
import random


pd.options.mode.chained_assignment = None
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def quantify_rainfall(row):
  if row['tag'] == 'none':
    val = 1
  elif row['tag'] == 'minimal':
    val = 2
  elif row['tag'] == 'some':
    val = 2
  elif row['tag'] == 'a lot':
    val = 3
  elif row['tag'] == 'substantial':
    val = 4
  elif row['tag'] == 'extensive':
    val = 5
  else:
    return 
  return val

def createDFFromFile(CSVFilename):
    data = pd.read_csv(CSVFilename)
    data.date = pd.to_datetime(data.date, dayfirst=True)
    return data

def calculate_PET(row):
    # This is what calculates PET

    # Gets the sum of the min and max air temp, and divides by 2
    temp = row['av_temp']
    
    # Occording to Scott and that's good enough for me
    latent_heat_of_vapourisation = 2.260 #MJ/kg 
    
    T = (temp + 5) / 68
    
    PET = (1/latent_heat_of_vapourisation) * row['irad_amt'] * T
    return PET

def calculate_av_temp(row):
    av = (row['max_air_temp'] + row['min_air_temp']) / 2
    return av

def calculateWaterRemaining(row):
    remaining = row['prcp_amt'] - row['PET']
    return remaining


# returns df of precipitation data
def precipitationData(CSVFilename):
    data = pd.read_csv(CSVFilename, index_col=False)
    measured = data[['Date','Precipitation rate (mm/day)(HadREM3-GA705-r001i1p00000)']]
    measured.columns = ['date', 'prcp_amt']
    
    # Get rid of any sneaky whitespace that may ruin all the fun later
    # measured['prcp_amt'] = measured['prcp_amt'].str.split().str[0].str.replace(' ','').astype(float)
    measured.date = pd.to_datetime(measured.date, dayfirst=True)
    return measured

# returns df of tempterature data
def temperatureData(CSVFilename):
    data = pd.read_csv(CSVFilename, index_col=False)
    measured = data[['Date','Mean air temperature at 1.5m (¬∞C)(HadREM3-GA705-r001i1p00000)']]
    measured.columns = ['date', 'av_temp']
    
    # Get rid of any sneaky whitespace that may ruin all the fun later
    measured.date = pd.to_datetime(measured.date, dayfirst=True)
    return measured

# returns df of radiation data
def radiationData(CSVFilename):
    data = pd.read_csv(CSVFilename, index_col=False)
    measured = data[['Date','Net Surface short wave flux (W m-2)(HadREM3-GA705-r001i1p00000)']]
    measured.columns = ['date', 'irad_amt']
    
    # Get rid of any sneaky whitespace that may ruin all the fun later
    measured.date = pd.to_datetime(measured.date, dayfirst=True)
    return measured

def measuredPrecipitationData(CSVFilename):
    data = pd.read_csv(CSVFilename, index_col=False)
    data = data.drop_duplicates(subset=' ob_date', keep="last")
    measured = data[[' ob_date',' prcp_amt']]
    measured.columns = ['date', 'prcp_amt']
    
    # Get rid of any sneaky whitespace that may ruin all the fun later
    measured['prcp_amt'] = measured['prcp_amt'].str.split().str[0].str.replace(' ','').astype(float)
    measured.date = pd.to_datetime(measured.date, dayfirst=True)

    return measured


# returns observed weather
def observedWeatherData(CSVFilename):
  data = pd.read_csv(CSVFilename)
  # create new dataframe with just tag and data
  # this assumes that the data is clean, with circle 6 in the first column
  # import code; code.interact(local=dict(globals(), **locals()))

  observed = data[['date','tag']]

  observed['amount'] = observed.apply(quantify_rainfall, axis=1)
  observed.columns = ['date', 'rainfall', 'amount']
  ## Converts string date to datetime, making sure day is first 
  observed.date = pd.to_datetime(observed.date, dayfirst=True)
  return observed

def measuredClimateData(CSVFilename):
  measuredData = pd.read_csv(CSVFilename, index_col=False)
  measuredData.date = pd.to_datetime(measuredData.date, dayfirst=True)
  return measuredData


## Merge the two dataframes together to get a nice new one
def merge_observed_rainfall_with_precp(precp, observed):
  ## set the dataframe indexes
  precp.set_index('date', inplace=True)
  observed.set_index('date', inplace=True)

  # Get the mean of the observed groundwater
  average_observed = observed.groupby('date').mean().astype(int)

  # Get the mean of precipitation
  average_precp = precp.groupby('date').mean()

  ## merge the two datafremes
  combined = pd.merge(average_precp, average_observed, how='outer', on=['date'])
  return combined


## Merge the two dataframes together to get a nice new one
def merge_observed_rainfall_with_temp(temp, observed):
  ## double make sure datetime is set...
  temp.date = pd.to_datetime(temp.date, dayfirst=True)
  ## set the dataframe indexes
  temp.set_index('date', inplace=True)
  observed.set_index('date', inplace=True)

  # Get the mean of the observed groundwater
  average_observed = observed.groupby('date').mean().astype(int)

  # Get the mean of precipitation
  average_temp = temp.groupby('date').mean()

  ## merge the two datafremes
  combined = pd.merge(average_temp, average_observed, how='outer', on=['date'])
  combined = combined.sort_index()
  return combined


## Basic styles for all plots (could be moved out)
def plot_styles():
  fig, ax = plt.subplots(1, 1, figsize=(8, 5))

  # general formatting
  ax.spines['top'].set_visible(False)
  ax.spines['bottom'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.get_xaxis().tick_bottom()
  ax.get_yaxis().tick_left()
  return fig, ax