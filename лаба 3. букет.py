colors=['красный', 'зеленый', 'фиолетовый', 'розовый', 'желтый']
sizes=['большой', 'средний', 'маленький']
flower_types=['розы', 'ромашки', 'ирисы']
full_price=[]

y=0

class flower:
    def __init__(self):
        self.number_of_flowers=None
        self.color=None
        self.size=None
        self.type=None
        self.price=None

    def n_o_f(self):
        global number
        global y
        while True:
            self.number_of_flowers = input('Сколько цветов Вы хотите добавить в букет? ')
            if (self.number_of_flowers).strip().isdigit():
                self.number_of_flowers=int(self.number_of_flowers).strip()

                if y > number:
                    print('Ошибка! Вы хотите добавить больше цветов, чем должно было быть в букете. Попробуйте еще раз.')
                else:
                    break
            else:
                print('Недопустимый формат введения. Попробуйте еще раз.')

    def set_color(self):
        while True:
            self.color = str(input('Какого цвета будут цветы? '))
            self.color = (str(self.color)).lower().strip()
            if self.color in colors:
                break
            else:
                print('Такого цвета у нас нет! Попробуйте еще раз.')
    def set_size(self):
        while True:
            self.size = input('Какой размер бутона вам нужен? (большой, средний, маленький) ')
            self.size = (str(self.size)).lower().strip()
            if self.size in sizes:
                break
            else:
                print('Недопустимый формат введения. Попробуйте еще раз.')




class Rose(flower):
    def cost(self):
        self.price=200*self.number_of_flowers
        full_price.append(self.price)

class Daisies(flower):
    def cost(self):
        self.price=150*self.number_of_flowers
        full_price.append(self.price)

class Iris(flower):
    def cost(self):
        self.price=80*self.number_of_flowers
        full_price.append(self.price)

def full_price_count():
    x=0
    for i in range(len(full_price)):
        x=x+int(full_price[i])
    return int(x)

def bouquet(x):
    for i in range(x):
        while True:
            typee=input('Розы, ромашки или ирисы? ')
            if str(typee).lower().strip() in flower_types:
                break
            else:
                print('Недопустимый формат введения. Попробуйте еще раз.')

        if str(typee).lower().strip()=='розы':
            f=Rose()
            f.n_o_f()
            f.set_color()
            f.set_size()
            f.cost()

        if str(typee).lower().strip()=='ромашки':
            f=Daisies()
            f.n_o_f()
            f.set_color()
            f.set_size()
            f.cost()
        if str(typee).lower().strip()=='ирисы':
            f=Daisies()

            f.n_o_f()

            f.set_color()

            f.set_size()
            f.cost()
    final_cost = 0
    for j in range(len(full_price)):
        final_cost + int(full_price[j])
    print(f'Итоговая цена букета {final_cost} рублей')


number=int(input('Какое количество цветов будет в букете? '))
types=int(input('Сколько разных видов цветов вы хотите в букете? '))
start=bouquet(types)










