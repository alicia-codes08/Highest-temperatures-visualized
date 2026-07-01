import csv
import matplotlib.pyplot as plt 
from pathlib import Path 

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
    if row[4] == "°C":
        try:
            value = float(row[5].replace(",", "."))
        except ValueError:
            print("NA")
        else:
            temperatures.append(value)

print(temperatures) 