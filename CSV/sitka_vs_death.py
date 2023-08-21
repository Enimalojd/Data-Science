import csv
from matplotlib import pyplot as plt
from datetime import datetime

filenames = ['data/sitka_weather_2021_simple.csv', 'data/death_valley_2021_simple.csv']
for filename in filenames:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[4])
                low = int(row[5])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red', alpha=1)
        plt.title(f'Daily high temperatures on {filename} 2021 year', fontsize=12)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel('Temperatures', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()