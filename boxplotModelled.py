from boxplot import *


CSVFilename = 'climate-data/combined_with_observed_only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)

# ----------------------------------- Plot PET boxplot -------------------------------------
plot_just_daily_boxplot(data, 'PET', 'PET', 'Plot of daily PET levels when image taken','rocket')
plt.savefig('plots/modelled/boxplot/pet-boxplot.png')
# ----------------------------------------- end --------------------------------------------


# ---------------------------------- Plot temp boxplot -------------------------------------
plot_just_daily_boxplot(data, 'av_temp', 'Temperature (c)', 'Plot of daily temperature when image taken','autumn')
plt.savefig('plots/modelled/boxplot/temp-boxplot.png')
# ----------------------------------------- end --------------------------------------------


# ----------------------------------- Plot Precipitation boxplot ---------------------------
plot_just_daily_boxplot(data, 'prcp_amt', 'Precipitation (mm)', 'Plot of precipitation (mm)  when image taken', "Blues_r")
plt.savefig('plots/modelled/boxplot/rain-boxplot.png')
# ----------------------------------------- end --------------------------------------------

# ----------------------------------- Plot Precipitation boxplot ---------------------------
plot_just_daily_boxplot(data, 'remaining', 'Remaining (mm)', 'Plot of remaining (mm)  when image taken', "viridis")
plt.savefig('plots/modelled/boxplot/remaining-boxplot.png')
# ----------------------------------------- end --------------------------------------------