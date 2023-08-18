import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # построение случайного блуждания
    rw = RandomWalk()
    rw.fill_walk()

    # нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_point)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    #выделение первой и последней точки
    ax.scatter(0, 0, color='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], color='red', s=100)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
