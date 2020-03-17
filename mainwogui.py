class BD:
    table = []

    def __init__(self, path):
        self.load(path)

    def add(self, data):
        self.table.append(data)

    def get(self):
        return self.table

    def load(self, path):
        f = open(path, 'r')
        data = f.read()
        f.close()
        for i in data.split('\n'):
            aaa = []
            for j in i.split('\t'):
                if len(j) != 0:
                    aaa.append(j)
            if len(aaa) != 0:
                self.add(aaa)

    def save(self, path):
        f = open(path, 'w')
        for i in self.get():
            for j in i:
                f.write(str(j) + '\t')
            f.write("\n")
        f.close()

    def view(self):
        for i in range(len(self.table)):
            print(i, end='\t')
            for j in self.table[i]:
                print(j, end = '\t')
            print()

    def f1(self):
        bomj = min([float(x[2]) for x in self.table])
        for i in self.table:
            if float(i[2]) == bomj:
                for j in i:
                    print(j, end = '\t')
                print()

    def f2(self, klient):
        for i in self.table:
            if i[0].split(' ')[0] == klient:
                for j in i:
                    print(j, end = '\t')
                print()

    def f3(self):
        print('Количество вкладов: ', len(self.table))
        print('Сумма всех вкладов: ', sum([float(x[2]) for x in self.table]))

    def iii(self):
        print('Введите ФИО, номер счета, сумму на счету, адрес клиента, дату последней операции, номер операции')
        print('Для разделения используйте Tab')
        ii = input().split('\t')
        self.add(ii)

    def delete(self):
        self.view()
        im = int(input('Введите номер удаляемого: '))
        if im in range(len(self.table)):
            self.table.pop(im)
        else:
            print('Некорректно введенные данные')


test = BD('bank.txt')
print('1)Вывести самого бедного\n2)Данные о конкретном клиенте\n3)Сумму вкладов всех клиентов и их количество\n ')
print('Для просмотра БД - view\nДля выхода - quit Для добавления и удаления - add и delete\n')
while True:
    inp = input()
    if inp == 'quit':
        break
    elif inp =='view':
        test.view()
    elif inp =='1':
        test.f1()
    elif inp =='2':
        klient = input('Введите фамилию: ')
        test.f2(klient)
    elif inp =='3':
        test.f3()
    elif inp =='add':
        test.iii()
    elif inp =='delete':
        test.delete()
    else:
        print('Такого пункта нет')
test.save('bank.txt')
