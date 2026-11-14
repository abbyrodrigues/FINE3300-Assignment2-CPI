# FINE 3300 Assignment 2 – Consumer Price Index & Inflation Calculator

Student: Abigail Rodrigues  (220400172)
Course: FINE 3300 – Python for Finance Professionals  
Term: Fall 2026

## Introduction
My replication of this project uses monthly Consumer Price Index (CPI) data from the Bank of Canada over the past years to create a graph and an inflation calculator.  
The calculator accepts both month and year.

## Files in this repository
- `cpi_calculator.py` – this is the main Python program
- `cpi_data.csv` – this is the monthly CPI data which was downloaded from the Bank of Canada website
- `cpi_graph.png` – this is the graph created by the program
- `README.md` – this file which details pertinent information

## How to run the project
1. Make sure that you have Python installed
2. Make sure to also install the required libraries (if needed):
pip install pandas matplotlib numpy

3. Make sure `cpi_data.csv` is in the same folder as the Python file
4. Run the program:

python3 cpi_calculator.py

## CPI Graph

![CPI Graph](cpi_graph.png)

### Short commentary on the CPI
The blue line shows the Consumer Price Index level (2002 = 100).  
The red line shows the year-over-year percentage change (annual inflation).  
The black dotted line marks the base level of 100.

Some interesting points:
- Prices were very low in the early 1900s.
- Noticed there was high inflation during the 1970s and early 1980s.
- Inflation stayed relatively low and stable for many years after the mid-1990s.
- There was a clear rise in inflation after 2021.
- The most recent data (2026) shows inflation moving closer to the Bank of Canada’s 2% target.

## Sample Calculator Output

Bank of Canada Style Inflation Calculator

Enter the price of the goods/services (example: 100 or 49.99): $100

Enter the first date (format YYYY-MM, example: 2000-09): 2000-09

Enter the second date (format YYYY-MM, example: 2024-06): 2020-09

Results

$100.00 in 2000-09 is equivalent to $142.46 in 2020-09P

ercentage change:          +42.46%

Difference in years:        20.0 years

Average annual rate:        1.79%
CPI in 2000-09:               96.1

CPI in 2020-09:               136.9

(All money values rounded to the nearest penny)


## Data Source
Bank of Canada Valet API  
https://www.bankofcanada.ca/valet/observations/STATIC_INFLATIONCALC/csv  

Original series: Statistics Canada V41690973 (Total CPI, 2002 = 100)