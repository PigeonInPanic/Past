count = 0
Num = 20

while count < 20:
    for i in range (1,10):
        count = 0
        Num +=1
        if Num % i == 0:
            count +=1

print ("Самое маленькое число, которое делится от 1 до 20 без остатка = " + str(Num))