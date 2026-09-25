class bank_account():   #класс, для действий с счетом любого типа клиентов
    def __init__(self, money_plus, money_minus):
        self.b_a_plus=money_plus
        self.b_a_minus=money_minus




print ('Сколько клиентов пришло в банк?: ') #начало вывода программы
n = int(input())
for i in range(n):
    i=i+1
    print(f'Выберите тип {i}-го клиента \n 1 - физическое лицо \n 2 - юридическое лицо')




