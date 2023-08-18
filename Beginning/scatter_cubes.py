import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x*x*x for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)
ax.set_title('Cubes numbers', fontsize=15)
ax.set_xlabel('Value', fontsize=7)
ax.set_ylabel('Cube of value', fontsize=7)
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()
