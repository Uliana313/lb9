A = set(range(1, 251))

num = int(input("Введіть число: "))

A = {x for x in A if num % x != 0}

print("Множина після видалення дільників:", A)
