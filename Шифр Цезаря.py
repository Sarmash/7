def encoder():
    cod = input('Нужно шифрование или дешфрование? Нажмите "ш" = шифрование или "д" = дешифрование: ')
    while cod != 'ш' and cod != 'д':
        print('Введите правильный символ')
        cod = input()
    language = input('Выберите язык алфавита? Нажмите "р" = русский или "а" = английский: ')
    while language != 'р' and language != 'а':
        print('Введите правильный символ')
        language = input()
    step = int(input('Замена символа в алфавите находящемся правее него на определенном количестве шагов. Выберите шаг сдвига (со сдвигом вправо): '))
    txt = input('Введите текст:  ')
    p = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    P = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    e = 'abcdefghijklmnopqrstuvwxyz'
    E = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if cod == 'ш' and language == 'р':
        for i in range(len(txt)):
            if txt[i] in p:
                c = p.index(txt[i])
                if c + step > 32:
                    d = c + step - 32
                else:
                    d = c + step
                txt = txt[:i] + p[d] + txt[i + 1:]
            if txt[i] in P:
                c = P.index(txt[i])
                if c + step > 32:
                    d = c + step - 32
                else:
                    d = c + step                    
                txt = txt[:i] + P[d] + txt[i + 1:]
        print(txt)
    elif cod == 'д' and language == 'р':
        for i in range(len(txt)):
            if txt[i] in p:
                c = p.index(txt[i])
                if c - step < 0:
                    d = c - step + 32
                else:
                    d = c - step
                txt = txt[:i] + p[d] + txt[i + 1:]
            if txt[i] in P:
                c = P.index(txt[i])
                if c - step < 0:
                    d = c - step + 32
                else:
                    d = c - step
                txt = txt[:i] + P[d] + txt[i + 1:]
        print(txt)
    elif cod == 'ш' and language == 'а':
        for i in range(len(txt)):
            if txt[i] in e:
                c = e.index(txt[i])
                if c + step > 26:
                    d = c + step - 26
                else:
                    d = c + step                
                txt = txt[:i] + e[d] + txt[i + 1:]
            if txt[i] in E:
                c = E.index(txt[i])
                if c + step > 26:
                    d = c + step - 26
                else:
                    d = c + step                
                txt = txt[:i] + E[d] + txt[i + 1:]
        print(txt)
    elif cod == 'д' and language == 'а':
        for i in range(len(txt)):
            if txt[i] in e:
                c = e.index(txt[i])
                if c - step < 0:
                    d = c - step + 26
                else:
                    d = c - step
                txt = txt[:i] + e[d] + txt[i + 1:]
            if txt[i] in E:
                c = E.index(txt[i])
                if c - step < 0:
                    d = c - step + 26
                else:
                    d = c - step
                txt = txt[:i] + E[d] + txt[i + 1:]
        print('Значение:')
        print(txt)
    x = input('Продолжить работу с шифрами? Если да, то нажмите "д". Если или нет, то нажмите "н": ')
    while x != 'д' and x != 'н':
        print('Введите правильный символ')
        x = input()
    if x == 'д':
        encoder()
    elif x == 'н':
        print('Успехов в Ваших замыслах')
encoder()
input()
