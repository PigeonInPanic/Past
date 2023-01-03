summ = 0
Elemnt = 0
FirstEl = 1
SecondEl = 2 

summ += FirstEl

while SecondEl <= 4000000:
    print("------------------------------------")
    print ("Первый элемент = " + str(FirstEl))
    print ("Второй элемент = " + str(SecondEl))
    print("------------------------------------")
    summ +=SecondEl
    Elemnt = FirstEl
    FirstEl = SecondEl
    SecondEl = SecondEl + Elemnt
    
print("Сумма всех чисел Фибоначчи не превышающая 4000000: "+ str(summ))