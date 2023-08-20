import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    #чтение максимальных температур и запись их в список
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.title('Daily high temperatures on Sitka july 2021 year', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()