from base import *


# ------------------------------------ FANGANGLE DATA ------------------------------------

## FANANGLE RADIATION
radiationDataFile = 'climate-data/radiation.csv'
rad = radiationData(radiationDataFile)

## FANANGLE TEMPERATURE
temperatureDataFile = 'climate-data/temp.csv' ### <<<<< Change this file when needed
temps = temperatureData(temperatureDataFile)

## FANANGLE ACTUAL RAINFALL
precipitationCsvFile = 'climate-data/rain.csv' ### <<<<< Change this file when needed
precp = precipitationData(precipitationCsvFile)

## FANGANGLE OBSERVED RAINFALL
observedCsvFile = 'observed/observed-mode-winter-2020-n31.csv' ### <<<<< Change this file when needed
observed = observedWeatherData(observedCsvFile)
df = observed[['date','amount']]



# -------------  merge all weather measurements ---------------
combined = pd.merge(rad, temps, how='outer', on=['date'])
combined = pd.merge(combined, precp, how='outer', on=['date'])
combined['PET'] = combined.apply(calculate_PET, axis=1)
# combined.to_csv('climate-data/combined.csv')


# merge with observed
combined_ob = pd.merge(combined, df, how='outer', on=['date'])
combined_ob['remaining'] = combined_ob.apply(calculateWaterRemaining, axis=1)
# combined_ob.to_csv('climate-data/combined_with_observed.csv')

combined_ob_only = combined_ob.dropna()
# combined_ob_only.to_csv('climate-data/combined_with_observed_only.csv')



## --------------- Create csv for MEASURED data alongside modal observed -------------
measuredClimateDataFile = 'measured-climate-data/pet10years-ayr-updated.csv'
measured = measuredClimateData(measuredClimateDataFile)
measured['av_temp'] = measured.apply(calculate_av_temp, axis=1)


# Add in measured rainfall
measuredRainFile = 'measured-climate-data/10-years-rainfall.csv'
measuredRain = measuredPrecipitationData(measuredRainFile)
measured = pd.merge(measured, measuredRain, how='outer', on=['date'])
measured['remaining'] = measured.apply(calculateWaterRemaining, axis=1)

# import code; code.interact(local=dict(globals(), **locals()))


# merge measured with observed
measuredCombined = pd.merge(measured, df, how='outer', on=['date'])
measuredCombined = measuredCombined.drop(['Unnamed: 0'], axis=1)
# measuredCombined.to_csv('measured-climate-data/measured-with-observed.csv')

measuredCombinedOnly = measuredCombined.dropna()
# measuredCombinedOnly.to_csv('measured-climate-data/measured-with-observed-only.csv')




