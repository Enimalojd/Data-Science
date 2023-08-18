import matplotlib.pyplot as plt
import matplotlib.style as style

input_valuus = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_valuus ,squares, linewidth=3)

#назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)
plt.show()