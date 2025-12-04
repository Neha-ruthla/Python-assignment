import pandas as pd
from modules.data_loader import load_data
from modules.data_cleaner import clean_data
from modules.visualizer import (
    plot_temperature,
    plot_rainfall,
    plot_humidity,
    plot_combined
)

# 1) Load data
df = load_data("data/raw_weather_data.csv")

# 2) Clean data
cleaned_df = clean_data(df)

# 3) Save cleaned dataset
cleaned_df.to_csv("outputs/cleaned_weather_data.csv", index=False)

# 4) Generate plots
plot_temperature(cleaned_df, "outputs/temp_trend.png")
plot_rainfall(cleaned_df, "outputs/rainfall_bar.png")
plot_humidity(cleaned_df, "outputs/humidity_scatter.png")
plot_combined(cleaned_df, "outputs/combined_plot.png")

print("All tasks completed! Check the outputs folder.")
