# FINE 3300 - Assignment 2
# Consumer Price Index and Inflation Calculator

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# PART 1 - LOAD THE DATA

# Read the CSV file. The Bank of Canada file has header rows we need to skip.
df = pd.read_csv("cpi_data.csv", skiprows=8)

# Rename the columns so they are easier to work with
df.columns = ["date", "cpi"]

# Turn the date column into real dates that Python understands
df["date"] = pd.to_datetime(df["date"])

# Sort just in case (oldest to newest)
df = df.sort_values("date").reset_index(drop=True)

print("Data loaded successfully!")
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print(f"\nTotal months of data: {len(df)}")

# PART 2 - CALCULATE YEAR-OVER-YEAR % CHANGE

# This calculates the percentage change compared to the same month one year ago
df["yoy_pct"] = df["cpi"].pct_change(periods=12) * 100

# PART 3 - CREATE THE GRAPH

fig, ax1 = plt.subplots(figsize=(12, 6))

# Left axis shows the CPI level
color1 = "tab:blue"
ax1.set_xlabel("Year")
ax1.set_ylabel("CPI (2002 = 100)", color=color1)
ax1.plot(df["date"], df["cpi"], color=color1, label="CPI Level")
ax1.tick_params(axis="y", labelcolor=color1)

# Draw a dotted horizontal line at the base year level (100)
ax1.axhline(y=100, color="black", linestyle="--", linewidth=1.5, label="Base Level (2002 = 100)")

# Right axis shows the annual percentage change
ax2 = ax1.twinx()
color2 = "tab:red"
ax2.set_ylabel("Annual % Change", color=color2)
ax2.plot(df["date"], df["yoy_pct"], color=color2, alpha=0.7, label="Annual % Change")
ax2.tick_params(axis="y", labelcolor=color2)

# Title and legend
plt.title("Canada Consumer Price Index (CPI) and Annual Inflation Rate\n1914 – Present", fontsize=14)
fig.legend(loc="upper left", bbox_to_anchor=(0.12, 0.88))

# Make the graph look a bit cleaner
plt.grid(True, alpha=0.3)
fig.tight_layout()

# Save the graph as a PNG file
plt.savefig("cpi_graph.png", dpi=150)
print("\nGraph saved as cpi_graph.png")


# PART 4 - INFLATION CALCULATOR

def get_cpi_for_date(year, month):
    """
    Look up the CPI value for a specific year and month.
    Returns the CPI number or None if that date is not in the data.
    """
    # Find rows that match this year and month
    match = df[(df["date"].dt.year == year) & (df["date"].dt.month == month)]
    
    if len(match) == 0:
        return None
    else:
        return match["cpi"].values[0]


def run_calculator():
    print("\nBank of Canada Style Inflation Calculator")
    print("(Enhanced – now accepts month and year)")
    
    # Get price from user
    while True:
        try:
            price_str = input("\nEnter the price of the goods/services (example: 100 or 49.99): $")
            price = float(price_str.replace(",", "").replace("$", "").strip())
            if price <= 0:
                print("Price must be positive. Try again.")
                continue
            break
        except:
            print("That is not a valid number. Please try again.")
    
    # Get first date
    while True:
        date1_str = input("Enter the first date (format YYYY-MM, example: 2000-09): ").strip()
        try:
            year1 = int(date1_str[:4])
            month1 = int(date1_str[5:7])
            if month1 < 1 or month1 > 12:
                print("Month must be between 01 and 12.")
                continue
            cpi1 = get_cpi_for_date(year1, month1)
            if cpi1 is None:
                print(f"No data found for {year1}-{month1:02d}. Check the date is between 1914-01 and the latest available month.")
                continue
            break
        except:
            print("Wrong format. Please use YYYY-MM (example: 2015-03)")
    
    # Get second date 
    while True:
        date2_str = input("Enter the second date (format YYYY-MM, example: 2024-06): ").strip()
        try:
            year2 = int(date2_str[:4])
            month2 = int(date2_str[5:7])
            if month2 < 1 or month2 > 12:
                print("Month must be between 01 and 12.")
                continue
            cpi2 = get_cpi_for_date(year2, month2)
            if cpi2 is None:
                print(f"No data found for {year2}-{month2:02d}. Check the date is between 1914-01 and the latest available month.")
                continue
            break
        except:
            print("Wrong format. Please use YYYY-MM (example: 2023-11)")
    
    # Do the calculations (same formulas the Bank of Canada uses) 
    # New price = old price * (CPI2 / CPI1)
    new_price = price * (cpi2 / cpi1)
    
    # Percentage change
    pct_change = ((new_price - price) / price) * 100
    
    # Number of years between the two dates (approximate)
    years_diff = (year2 - year1) + (month2 - month1) / 12.0
    
    # Annual rate of change (compound annual growth rate)
    if years_diff != 0:
        annual_rate = ((cpi2 / cpi1) ** (1 / years_diff) - 1) * 100
    else:
        annual_rate = 0.0
    
    # Print the results
    print("\nResults")
    print(f"${price:,.2f} in {year1}-{month1:02d} is equivalent to ${new_price:,.2f} in {year2}-{month2:02d}")
    print()
    print(f"Percentage change:          {pct_change:+.2f}%")
    print(f"Difference in years:        {years_diff:.1f} years")
    print(f"Average annual rate:        {annual_rate:.2f}%")
    print()
    print(f"CPI in {year1}-{month1:02d}:               {cpi1:.1f}")
    print(f"CPI in {year2}-{month2:02d}:               {cpi2:.1f}")
    print("(All money values rounded to the nearest penny)")


# Run the calculator
run_calculator()

# Optional: let the user run it again
while True:
    again = input("\nDo you want to calculate another amount? (yes/no): ").lower().strip()
    if again in ["yes", "y"]:
        run_calculator()
    else:
        print("Done. Thank you!")
        break