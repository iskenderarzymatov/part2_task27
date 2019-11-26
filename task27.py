all_numbers = input("Введите положительные и отрицательные числа: ").split()
int_all_numbers = []
positive = []
negative = []
for x in all_numbers:
    int_all_numbers.append(int(x))

for i in int_all_numbers:
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)
    else:
        None
print("Положительные числа: ", positive)
print("Отрицательные числа: ", negative)