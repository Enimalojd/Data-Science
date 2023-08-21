import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    #чтение максимальных температур и запись их в список
    precipitations, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            precipitation = float(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            precipitations.append(precipitation)

#нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c='red', alpha=0.5)
plt.fill_between(dates, precipitations, facecolor='blue', alpha=0.5)
plt.title('Rainfall on Sitka 2021 year', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()