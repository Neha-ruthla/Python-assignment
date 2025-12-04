# Weather Data Visualizer

This project analyzes daily weather data using Python and generates meaningful insights through data cleaning, statistical analysis, and visualizations. It demonstrates a complete workflow of loading raw data, cleaning it, processing it, and creating multiple weather-related graphs.

---

## 📁 Project Structure

weather-data-visualizer-yourname/
│
├── data/
│ └── raw_weather_data.csv
│
├── modules/
│ ├── data_loader.py
│ ├── data_cleaner.py
│ └── visualizer.py
│
├── outputs/
│ ├── cleaned_weather_data.csv
│ ├── temp_trend.png
│ ├── rainfall_bar.png
│ ├── humidity_scatter.png
│ └── combined_plot.png
│
├── main.py
├── README.md
├── summary_report.md
└── requirements.txt


---

##  Technologies Used

- **Python**
- **Pandas** – for data loading and cleaning  
- **NumPy** – for numeric/statistical operations  
- **Matplotlib** – for data visualization  
- **VS Code / PyCharm** – as the development environment  

---

##  Features of the Project

###  Load Weather Data  
CSV file is loaded using a custom loader function.

###  Clean the Data  
- Removed blank rows  
- Converted date column  
- Filled missing numeric values  
- Removed invalid entries  

###  Perform Statistical Analysis  
Includes:  
- Average temperature  
- Highest & lowest temperature  
- Total rainfall  
- Average humidity  

###  Generate Visualizations  
The following charts are generated and saved in the **outputs/** folder:

1. **Temperature Trend (Line Chart)**  
2. **Monthly Rainfall (Bar Chart)**  
3. **Humidity vs Temperature (Scatter Plot)**  
4. **Combined Plot (Line + Scatter)**  

---

##  How to Run the Project

### 1️ Install the required libraries
