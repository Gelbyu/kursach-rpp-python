f = open('bank.txt', 'r')
data = f.read()
f.close()
table = []
for i in data.split('\n'):
    tabl = []
    for j in i.split('\t'):
        if len(j) != 0:
            tabl.append(j)
    if len(tabl) != 0:
        table.append(tabl)
print('1)Вывести самого бедного\n2)Данные о конкретном клиенте\n3)Сумму вкладов всех клиентов и их количество\n ')
while True:
    inp = input()
    if inp == 'quit':
        break
    elif inp == 'view':
        for i in table:
            for j in i:
                print(j, end = '\t')
            print()
    elif inp == '1':
        bomj = min([float(x[2]) for x in table])
        for i in table:
            if float(i[2]) == bomj:
                for j in i:
                    print(j, end = '\t')
                print()
    elif inp == '2':
        klient = input('Введите фамилию: ')
        for i in table:
            if i[0].split(' ')[0] == klient:
                for j in i:
                    print(j, end = '\t')
                print()
    elif inp == '3':
        print('Количество вкладов: ', len(table))
        print('Сумма всех вкладов: ', sum([float(x[2]) for x in table]))
    else:
        print("Rustya norm pacan")
f = open('bank.txt', 'w')
for i in table:
    for j in i:
        f.write(str(j) + '\t')
    f.write("\n")
f.close()