from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die1 = Die()
die2 = Die()
die3 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

freqs = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_result+1):
    feq = results.count(value)
    freqs.append(feq)

#визуализация результатов
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=freqs)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='image/d6_d6_d6.html')
