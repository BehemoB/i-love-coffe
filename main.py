#Создаем функцию:
def rot(num):
    Po_bukvam = iter(num) #Проитерируем
    Spisok = list(iter(lambda:int(next(Po_bukvam)), None)) #Делаем список
    for pochti_bukva in range (len(Spisok)): #Проверяем по символам, первую же шестерку заменяем на девятку
        if Spisok[pochti_bukva] == 6: 
            Spisok[pochti_bukva] = 9
            break
    Proverka = ''.join(str(chislo) for chislo in Spisok) #Объединяем в строку список и возвращаем
    return Proverka
num = input('num = ', )
print(rot(num)) #Выводим ответ
