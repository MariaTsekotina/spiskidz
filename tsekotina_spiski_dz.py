s=input("Введите слово: ")
slovo_list=list(s)
print(slovo_list)
while True:
    print("1-Определить длину строки ")
    print("2-Добавляет введеный пользователем элемент в конец списка ")
    print("3-Разворачивает список ")
    answer=int(input("Какую функцию вы желаете использовать?: "))
if answer==1:
    try:
        d=len(slovo_list)
        print(f"Длина строки: {d}")
    #break
    #except:
        #ValueError
    #else:
        #print("Ой, что-то не так. Попробуйте еще раз!")
        
    
