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
mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dict:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_text.append(eq_dict['properties']['title'])

#нанесение данных на карту
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
            'size': [5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title=f"{all_eq_data['metadata']['title']}")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='images/global_earthquakes30.html')

print(len(all_eq_dict))
print(mags[:10])
print(lons[:5])
print(lats[:5])