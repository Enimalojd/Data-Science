import csv
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    longs, lats, dates, brightness = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            lat = float(row[0])
            long = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            lats.append(lat)
            longs.append(long)
            brightness.append(bright)

#нанесение пожаров на карту
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,

}]
my_layout = Layout(title=f"{filename}")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='images/global_fires.html')