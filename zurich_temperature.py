import csv
import matplotlib.pyplot as plt 
from pathlib import Path 
from datetime import datetime

path = Path("weather_data/meteo_2025.csv")
lines = path.read_text(encoding="utf-8").splitlines() 
reader = csv.reader(lines) 
header_row = next(reader)

# Get the index of the needed information
for index, element in enumerate(header_row):
    print(index, element) 


# extract data
temperatures, dates = [], []
for row in reader:
    date = datetime.strptime(row[0][:10], "%Y-%m-%d")
    if row[4] == "°C":
        try:
            value = float(row[5].replace(",", "."))
        except ValueError:
            print(f"'NA' for {date}")
        else:
            temperatures.append(value)
            dates.append(date)

print(temperatures) 
print(dates) 