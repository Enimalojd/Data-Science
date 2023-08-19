from random import randint

class Die():
    #класс, представляющий кубик
    def __init__(self, num_sides=6):
        #инициализируем 6ти гранный кубик
        self.num_sides = num_sides
    
    def roll(self):
        #возвращает рандомное число от 1 до 6
        return randint(1, self.num_sides)