import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("data/uac.csv")

# ==========================
# DATA CLEANING
# ==========================

df['Date'] = pd.to_datetime(df['Date'])

df['Children in HHS Care'] = (
    df['Children in HHS Care']
    .astype(str)
    .str.replace(',', '')
)

numeric_cols = [
    'Children apprehended and placed in CBP custody*',
    'Children in CBP custody',
    'Children transferred out of CBP custody',
    'Children in HHS Care',
    'Children discharged from HHS Care'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ==========================
# KPI CREATION
# ==========================

df['Transfer Efficiency Ratio'] = (
    df['Children transferred out of CBP custody']
    /
    df['Children in CBP custody']
)

df['Discharge Effectiveness Index'] = (
    df['Children discharged from HHS Care']
    /
    df['Children in HHS Care']
)

df['Pipeline Throughput Rate'] = (
    df['Children discharged from HHS Care']
    /
    df['Children apprehended and placed in CBP custody*']
)

df['Backlog Accumulation Rate'] = (
    df['Children apprehended and placed in CBP custody*']
    -
    df['Children discharged from HHS Care']
)

df['CBP Backlog'] = (
    df['Children in CBP custody']
    -
    df['Children transferred out of CBP custody']
)

df['HHS Backlog'] = (
    df['Children in HHS Care']
    -
    df['Children discharged from HHS Care']
)

rolling_std = (
    df['Children discharged from HHS Care']
    .rolling(7)
    .std()
)

df['Outcome Stability Score'] = (
    1 / (1 + rolling_std)
)

# ==========================
# SAVE CLEAN DATASET
# ==========================

df.to_csv(
    "output/cleaned_uac.csv",
    index=False
)

# ==========================
# CHART 1
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['Children apprehended and placed in CBP custody*'])
plt.title("Daily Apprehensions")
plt.savefig("images/chart1_daily_apprehensions.png")
plt.close()

# ==========================
# CHART 2
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['Children in CBP custody'],
         label='CBP')

plt.plot(df['Date'],
         df['Children in HHS Care'],
         label='HHS')

plt.legend()
plt.title("CBP vs HHS Population")
plt.savefig("images/chart2_cbp_vs_hhs.png")
plt.close()

# ==========================
# CHART 3
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['Children transferred out of CBP custody'],
         label='Transfers')

plt.plot(df['Date'],
         df['Children discharged from HHS Care'],
         label='Discharges')

plt.legend()
plt.title("Transfers vs Discharges")
plt.savefig("images/chart3_transfers_vs_discharges.png")
plt.close()

# ==========================
# CHART 4
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['Transfer Efficiency Ratio'])

plt.title("Transfer Efficiency Ratio")
plt.savefig("images/chart4_transfer_efficiency.png")
plt.close()

# ==========================
# CHART 5
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['Discharge Effectiveness Index'])

plt.title("Discharge Effectiveness Index")
plt.savefig("images/chart5_discharge_effectiveness.png")
plt.close()

# ==========================
# CHART 6
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['CBP Backlog'])

plt.title("CBP Backlog")
plt.savefig("images/chart6_cbp_backlog.png")
plt.close()

# ==========================
# CHART 7
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['HHS Backlog'])

plt.title("HHS Backlog")
plt.savefig("images/chart7_hhs_backlog.png")
plt.close()

# ==========================
# CHART 8
# ==========================

plt.figure(figsize=(12,5))
plt.plot(df['Date'],
         df['Outcome Stability Score'])

plt.title("Outcome Stability Score")
plt.savefig("images/chart8_outcome_stability.png")
plt.close()

print("Dataset Processed Successfully")
print("All Charts Generated Successfully")

# ==================================
# WEEKDAY ANALYSIS
# ==================================

df['Day'] = df['Date'].dt.day_name()

weekday_analysis = (
    df.groupby('Day')['Transfer Efficiency Ratio']
    .mean()
)

print("\nWeekday Analysis")
print(weekday_analysis)

# ==================================
# MONTHLY ANALYSIS
# ==================================

df['Month'] = df['Date'].dt.to_period('M')

monthly_analysis = (
    df.groupby('Month')
    ['Children discharged from HHS Care']
    .sum()
)

print("\nMonthly Placement Trend")
print(monthly_analysis)

# ==================================
# BOTTLENECK DETECTION
# ==================================

df['Transfer Alert'] = np.where(
    df['Transfer Efficiency Ratio'] < 0.50,
    'Delay',
    'Normal'
)

df['Placement Alert'] = np.where(
    df['Discharge Effectiveness Index'] < 0.30,
    'Delay',
    'Normal'
)

print("\nTransfer Alerts")
print(df['Transfer Alert'].value_counts())

print("\nPlacement Alerts")
print(df['Placement Alert'].value_counts())