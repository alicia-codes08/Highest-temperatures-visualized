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
    if row[2]=="T_max_h1" and row[4]=="°C":
        date = datetime.strptime(row[0][:10], "%Y-%m-%d")
        try:
            value = float(row[5].replace(",", "."))
        except ValueError:
            print(f"'NA' for {date}")
        else:
            temperatures.append(value)
            dates.append(date)


# visualize extraced data
plt.style.use('grayscale')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, temperatures, color="red")
ax.set_title("Max. temperatures in Zurich (2025)", fontsize=20)
ax.set_ylabel("Temperature in °C", fontsize=16)
ax.tick_params(axis="both", labelsize=13)

plt.show() 