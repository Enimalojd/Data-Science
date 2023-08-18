import matplotlib.pyplot as plt
from random_walk import RandomWalk

# построение случайного блуждания
rw = RandomWalk(50000)
rw.fill_walk()

# нанесение точек на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_point)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
#выделение первой и последней точки
ax.scatter(0, 0, color='green', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], color='red', s=100)
#удаление осей
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('image/rw_image.png')




