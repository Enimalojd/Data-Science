from random import choice

class RandomWalk():
#класс для генерирования случайного блуждания
    def __init__(self, num_points=5000):
        #инициализируем атрибуты блуждания(переменная для хранения точек и два списка координат)
        self.num_point = num_points

        #все блуждания начинаются с точки(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #Вычисляет все точки блуждания. Шаги достигаются до достижения нужной длины
        while len(self.x_values) < self.num_point:

            #определение направления и длины перемещения
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            #вычисление следующих значений x и y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
