# Weather Data Visualizer – Delhi

A simple Python project that loads, cleans, analyzes, and visualizes Delhi weather data using **Pandas**, **NumPy**, and **Matplotlib**.

---

## Dataset
**File:** `weather.csv`

**Columns:**
- `date` – daily observation  
- `temperature` – °C  
- `humidity` – %  
- `rainfall` – mm  

Data reflects realistic Delhi winter patterns.

---

## Features
- Handle missing values  
- Convert dates and filter columns  
- Calculate basic statistics (mean, min, max, std)  
- Create plots (line, bar, scatter, combined)  
- Export cleaned data and figures  
- Summary report included (`markdown.md`)

---

## Requirements
Install required libraries:
```bash
pip install pandas numpy matplotlib
```

---

## How to Run
```bash
python weather.py
```