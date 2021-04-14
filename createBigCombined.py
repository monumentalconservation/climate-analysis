from base import *

def calculate_PET_columwise(temp, irad_amt):
    # This is what calculates PET
    
    # Occording to Scott and that's good enough for me
    latent_heat_of_vapourisation = 2.260 #MJ/kg 
    
    T = (temp + 5) / 68
    
    PET = (1/latent_heat_of_vapourisation) * irad_amt * T
    return PET

# ------------------------------------ FANGANGLE DATA ------------------------------------

## FANANGLE TEMPERATURE
temperatureDataFile = 'climate-data/temp_all.csv' ### <<<<< Change this file when needed
temps = createDFFromFile(temperatureDataFile)
temps.columns = ['date', '1t','2t','3t','4t','5t','6t','7t','8t','9t','10t','11t','12t']

## FANANGLE RADIATION
radiationDataFile = 'climate-data/radiation_all.csv'
rad = createDFFromFile(radiationDataFile)
rad.columns = ['date', '1r','2r','3r','4r','5r','6r','7r','8r','9r','10r','11r','12r']



# -------------  merge all weather measurements ---------------

ndf = rad[['date']]

ndf['1'] = calculate_PET_columwise(temps['1t'], rad['1r'])
ndf['2'] = calculate_PET_columwise(temps['2t'], rad['2r'])
ndf['3'] = calculate_PET_columwise(temps['3t'], rad['3r'])
ndf['4'] = calculate_PET_columwise(temps['4t'], rad['4r'])
ndf['5'] = calculate_PET_columwise(temps['5t'], rad['5r'])
ndf['6'] = calculate_PET_columwise(temps['6t'], rad['6r'])
ndf['7'] = calculate_PET_columwise(temps['7t'], rad['7r'])
ndf['8'] = calculate_PET_columwise(temps['8t'], rad['8r'])
ndf['9'] = calculate_PET_columwise(temps['9t'], rad['9r'])
ndf['10'] = calculate_PET_columwise(temps['10t'], rad['10r'])
ndf['11'] = calculate_PET_columwise(temps['11t'], rad['11r'])
ndf['12'] = calculate_PET_columwise(temps['12t'], rad['12r'])
# import code; code.interact(local=dict(globals(), **locals()))
ndf.to_csv('climate-data/pet_all.csv')


