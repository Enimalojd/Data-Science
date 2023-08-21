import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#изучение структур данных
filename = 'data/eq_data_1_day_m1.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dict = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#нанесение данных на карту
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='images/global_earthquakes.html')

print(len(all_eq_dict))
print(mags[:10])
print(lons[:5])
print(lats[:5])