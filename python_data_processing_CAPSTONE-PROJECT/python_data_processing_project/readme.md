# Python Capstone Project

# Python Data Processing Capstone Project

This project demonstrates basic data ingestion, cleaning, processing, and visualization using Python.  
It follows a modular structure and uses separate files for loading data, processing data, and generating charts.

---

##  Project Objective

- Load and clean data from a CSV file  
- Perform summary statistics (min, max, mean, sum)  
- Visualize the data using Matplotlib  
- Save the cleaned data and chart output  
- Follow a modular Python structure for clean and maintainable code

---

## 📁 Folder Structure

python_data_processing_CAPSTONE-PROJECT/
│── main.py  
│── config.py  
│── utils.py  
│── requirements.txt  
│── README.md  
│
├── Data/  
│     ├── input.csv  
│     ├── cleaned_output.csv  
│     └── chart.png  
│
└── modules/  
      ├── data_loader.py  
      ├── processor.py  
      └── visualizer.py  

---

##  File Descriptions

### **main.py**
Main driver program which:
- Loads the data  
- Cleans the data  
- Calculates summary statistics  
- Generates visualization  
- Saves cleaned output  

---

### **config.py**
Contains file path configuration:
- INPUT_PATH  
- OUTPUT_PATH  

---

### **utils.py**
Helper utilities such as:
- A line separator function for clean console output  

---

### **modules/data_loader.py**
Functions:
- `load_data(path)` → loads CSV  
- `save_data(df, path)` → saves CSV  

---

### **modules/processor.py**
Functions:
- `clean_data(df)` → removes nulls & duplicates  
- `calculate_summary(df, column)` → returns min, max, mean, sum stats  

---

### **modules/visualizer.py**
Contains:
- `make_bar_chart(df, column)` → generates bar chart and saves as chart.png  

---

##  Output Files

- **cleaned_output.csv** → Cleaned dataset  
- **chart.png** → Visualization (bar chart)  
- Summary printed in terminal  

---

##  How to Run

### 1. Install required libraries:
