import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'pog.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
        dates, highs, lows = [], [], []
    for row in reader:
        corrent_data = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[3])
        dates.append(corrent_data)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
_, ax = plt.subplots()
ax.plot(dates, highs, c='blue')
ax.plot(dates, lows, c='green')
ax.set_title("Najwyższa i najniższa temperatura", fontsize=16)
ax.set_xlabel("", fontsize=16)
_.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.2)
plt.show()
