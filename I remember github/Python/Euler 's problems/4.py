FN = 1
SN = 1
Result = 1
i = 100
y = 100

for i in range (100,1000):
    for y in range (100,1000):
        raw = str(i*y)
        rf = int(raw[::-1])
        if rf == i * y:
            FN = i
            SN = y
            Result = rf

print("Первый элемент умножения =" + str(FN))
print("Второй элемент умножения = " + str(SN))
print("Результат = " + str(Result))

print(str(FN) + " * " + str(SN) + " = " + str(Result))