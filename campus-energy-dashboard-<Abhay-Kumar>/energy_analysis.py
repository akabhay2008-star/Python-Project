# ======================================
# ENERGY ANALYSIS PROJECT 
# ======================================

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


# ============================================================
# TASK 1: DATA INGESTION + VALIDATION
# ============================================================

def load_dataset():
    data_folder = Path("data/")
    files = list(data_folder.glob("*.csv"))
    combined = []

    if not files:
        print("No CSV files found in /data/ folder!")
        return pd.DataFrame()

    for file in files:
        try:
            df = pd.read_csv(file, on_bad_lines="skip")
            df["building"] = file.stem

            # Standardize column names
            df.columns = df.columns.str.lower()

            combined.append(df)

        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    df_combined = pd.concat(combined, ignore_index=True)
    print("Data Loaded Successfully!")
    return df_combined


# ============================================================
# TASK 2: AGGREGATION FUNCTIONS
# ============================================================

def calculate_daily_totals(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df.resample("D", on="timestamp")["kwh"].sum()


def calculate_weekly_totals(df):
    return df.resample("W", on="timestamp")["kwh"].sum()


def building_summary(df):
    return df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])


# ============================================================
# TASK 3: OBJECT ORIENTED MODELING
# ============================================================

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh


class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

    def total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        return f"{self.name} consumed {self.total_consumption()} kWh"


class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_building(self, building):
        self.buildings[building.name] = building

    def get_total_campus_consumption(self):
        return sum(b.total_consumption() for b in self.buildings.values())


# ============================================================
# TASK 4: VISUAL DASHBOARD (MATPLOTLIB)
# ============================================================

def create_dashboard(daily, weekly, df):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    # Plot 1: Daily Line Chart
    ax[0].plot(daily.index, daily.values)
    ax[0].set_title("Daily Energy Consumption")
    ax[0].set_xlabel("Date")
    ax[0].set_ylabel("kWh")

    # Plot 2: Weekly Bar Chart
    ax[1].bar(weekly.index.astype(str), weekly.values)
    ax[1].set_title("Weekly Energy Usage")
    ax[1].set_xlabel("Week")
    ax[1].set_ylabel("kWh")
    ax[1].tick_params(axis='x', rotation=45)

    # Plot 3: Scatter Chart
    ax[2].scatter(df["timestamp"], df["kwh"])
    ax[2].set_title("Scatter: Timestamp vs kWh")
    ax[2].set_xlabel("Timestamp")
    ax[2].set_ylabel("kWh")

    plt.tight_layout()
    plt.savefig("dashboard.png")
    print("Dashboard saved as dashboard.png")


# ============================================================
# TASK 5: EXPORT DATA + SUMMARY REPORT
# ============================================================

def save_outputs(df, summary, daily, weekly):
    df.to_csv("cleaned_energy_data.csv", index=False)
    summary.to_csv("building_summary.csv")

    total_consumption = df["kwh"].sum()
    highest_building = summary["sum"].idxmax()
    peak_time = df.loc[df["kwh"].idxmax(), "timestamp"]

    report_text = (
        f"Energy Summary Report\n"
        f"---------------------------\n"
        f"Total Campus Consumption: {total_consumption} kWh\n"
        f"Highest Consuming Building: {highest_building}\n"
        f"Peak Load Time: {peak_time}\n"
        f"\nDaily Trend: Saved in dashboard.png\n"
        f"Weekly Trend: Saved in dashboard.png\n"
    )

    with open("summary.txt", "w") as f:
        f.write(report_text)

    print("Output files saved:")
    print("- cleaned_energy_data.csv")
    print("- building_summary.csv")
    print("- summary.txt")


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    df = load_dataset()
    if df.empty:
        return

    # Aggregations
    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_totals(df)
    summary = building_summary(df)

    # Dashboard
    create_dashboard(daily, weekly, df)

    # Output Files
    save_outputs(df, summary, daily, weekly)

    print("\nScript Completed Successfully!")


if __name__ == "__main__":
    main()

