# Weather Data Visualizer

# === Import required libraries ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Make a folder for saved plots
os.makedirs("plots", exist_ok=True)

# =============================================================
# TASK 1 — Load the dataset
# =============================================================
# If user has a file named "weather.csv" in the same folder, it will use that.
# Otherwise, it will generate a small example dataset automatically.

if os.path.exists("weather.csv"):
    print("Loading weather.csv...")
    df = pd.read_csv("weather.csv")
else:
    print("weather.csv not found — creating example dataset...")
    dates = pd.date_range("2023-01-01", "2023-03-31")
    temp = 25 + np.random.randn(len(dates)) * 3
    humidity = 50 + np.random.randn(len(dates)) * 8
    rainfall = np.abs(np.random.randn(len(dates))) * 2

    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temp,
        "Humidity": humidity,
        "Rainfall": rainfall
    })

print("First 5 rows:")
print(df.head())

# =============================================================
# TASK 2 — Cleaning and processing
# =============================================================
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])  # remove invalid dates

# Fill missing numeric values with median
num_cols = ["Temperature", "Humidity", "Rainfall"]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

print("Cleaned data info:")
print(df.info())

# =============================================================
# TASK 3 — NumPy statistical analysis
# =============================================================
stats = {}
for col in num_cols:
    arr = df[col].values
    stats[col] = {
        "mean": np.mean(arr),
        "min": np.min(arr),
        "max": np.max(arr),
        "std": np.std(arr)
    }

print("Statistics:")
for k, v in stats.items():
    print(k, v)

# =============================================================
# TASK 4 — Matplotlib Visualizations
# =============================================================
# 1. Daily temperature line chart
plt.figure(figsize=(8,4))
plt.plot(df["Date"], df["Temperature"])
plt.title("Daily Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("plots/daily_temperature.png")
plt.close()

# 2. Monthly rainfall bar chart
monthly_rain = df.set_index("Date")["Rainfall"].resample("ME").sum()
plt.figure(figsize=(6,4))
plt.bar(monthly_rain.index.astype(str), monthly_rain.values)
plt.title("Monthly Rainfall")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/monthly_rainfall.png")
plt.close()

# 3. Scatter: humidity vs temperature
plt.figure(figsize=(6,4))
plt.scatter(df["Temperature"], df["Humidity"], alpha=0.6)
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.tight_layout()
plt.savefig("plots/humidity_vs_temperature.png")
plt.close()

# 4. Combined plot (Temperature + Rainfall)
plt.figure(figsize=(8,4))
plt.plot(df["Date"], df["Temperature"], label="Temperature")
plt.bar(df["Date"], df["Rainfall"], alpha=0.3, label="Rainfall")
plt.legend()
plt.title("Temperature + Rainfall Combined")
plt.tight_layout()
plt.savefig("plots/combined_plot.png")
plt.close()

# =============================================================
# TASK 5 — Grouping & Aggregation
# =============================================================
df.set_index("Date", inplace=True)
monthly = df.resample("ME").mean()
monthly.to_csv("monthly_summary.csv")

# =============================================================
# TASK 6 — Export cleaned data + report
# =============================================================
df.to_csv("cleaned_weather.csv")

with open("summary_report.txt", "w") as f:
    f.write("Weather Data Summary Report")
    f.write("===========================")
    for col, v in stats.items():
        f.write(f"{col} -> mean={v['mean']:.2f}, min={v['min']:.2f}, max={v['max']:.2f}, std={v['std']:.2f}\n")

print("All tasks completed. Files saved:")
print("- cleaned_weather.csv")
print("- monthly_summary.csv")
print("- summary_report.txt")
print("- plots/ (4 images)")
