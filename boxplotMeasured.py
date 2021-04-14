from base import *

from boxplot import add_n_obs, plot_just_daily_boxplot



CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)

# ----------------------------------- Plot PET boxplot -------------------------------------
plot_just_daily_boxplot(data, 'PET', 'PET', 'Plot of daily PET levels when image taken','rocket')
plt.savefig('plots/measured/boxplot/pet-boxplot.png')
# ----------------------------------------- end --------------------------------------------


# ---------------------------------- Plot temp boxplot -------------------------------------
plot_just_daily_boxplot(data, 'av_temp', 'Temperature (c)', 'Plot of daily temperature when image taken','autumn')
plt.savefig('plots/measured/boxplot/temp-boxplot.png')
# ----------------------------------------- end --------------------------------------------


# ----------------------------------- Plot Precipitation boxplot ---------------------------
plot_just_daily_boxplot(data, 'prcp_amt', 'Precipitation (mm)', 'Plot of precipitation (mm)  when image taken', "Blues_r")
plt.savefig('plots/measured/boxplot/rain-boxplot.png')
# ----------------------------------------- end --------------------------------------------

# ----------------------------------- Plot Precipitation boxplot ---------------------------
plot_just_daily_boxplot(data, 'remaining', 'Remaining (mm)', 'Plot of remaining water (mm)  when image taken', "viridis")
plt.savefig('plots/measured/boxplot/remaining-boxplot.png')
# ----------------------------------------- end --------------------------------------------
# plt.show()