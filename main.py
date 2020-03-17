from tkinter import *

class Main:
    root = Tk()
    message = StringVar()

    def __init__(self):
        self.root.title('Bank')
        self.root.geometry('900x700')
        self.text = Label(bg='white', height=42, width=125, justify=LEFT, anchor=NW, text='')
        self.text.pack()
        self.btn = Button(self.root, text="Click me", width=10, height=1, bg="white", fg="black")
        self.btn.place(relx=.90, rely=.94)
        self.btn.bind("<Button-1>", hello)
        self.entry = Entry(width=130, textvariable=self.message)
        self.entry.place(relx=.45, rely=.96, anchor="c")
        self.entry.bind("<Return>", hello)

    def start(self):
        self.root.mainloop()

    def print(self, arg, end='\n'):
        if len(self.text['text'].split('\n')) > 38:
            self.clear()
        self.text['text'] += arg
        self.text['text'] += end

    def clear(self):
        self.text['text'] = ''

    def clear_entry(self):
        self.message.set('')

    def get(self):
        return self.message.get()

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
        window.clear()
        for i in range(len(self.table)):
            window.print(str(i), end='\t')
            for j in self.table[i]:
                window.print(j, end='\t')
            window.print('')

    def f1(self):
        bomj = min([float(x[2]) for x in self.table])
        for i in self.table:
            if float(i[2]) == bomj:
                for j in i:
                    window.print(j, end='\t')
                window.print('')

    def f2(self, klient):
        for i in self.table:
            if i[0].split(' ')[0] == klient:
                for j in i:
                    window.print(j, end='\t')
                window.print('')

    def f3(self):
        window.print('Количество вкладов: '+str(len(self.table)))
        window.print('Сумма всех вкладов: '+str(sum([float(x[2]) for x in self.table])))

    def delete(self, klient):
        if int(klient) in range(len(self.table)):
            self.table.pop(int(klient))
        else:
            window.print('Некорректно введенные данные')


def hello(event):
    global temp1, temp2
    if temp1 == '0':
        inp = window.get()
        window.clear_entry()
    else:
        inp = temp1
        temp2 = window.get()
        window.clear_entry()
    if inp == 'view':
        test.view()
    elif inp == '1':
        test.f1()
    elif inp == '2':
        if inp != temp1:
            window.print('Введите фамилию: ')
            temp1 = inp
        else:
            test.f2(temp2)
            temp1 = '0'
    elif inp == '3':
        test.f3()
    elif inp == 'add':
        if inp != temp1:
            window.print('Введите ФИО, номер счета, сумму на счету, адрес клиента, дату последней операции, номер ')
            window.print('операции\nДля разделения используйте \'_\'')
            temp1 = inp
        else:
            test.add(temp2.split('_'))
            temp1 = '0'
    elif inp == 'delete':
        if inp != temp1:
            test.view()
            window.print('Введите номер удаляемого: ')
            temp1 = inp
        else:
            test.delete(temp2)
            temp1 = '0'
    else:
        window.print('Такого пункта нет')


temp1 = '0'
temp2 = str()
window = Main()
test = BD('bank.txt')
window.print('1)Вывести самого бедного\n2)Данные о конкретном клиенте\n3)Сумму вкладов всех клиентов и их кол', end='')
window.print('ичество\n Для просмотра БД - view\nДля добавления и удаления - add и delete\n', end='')
window.start()
test.save('bank.txt')