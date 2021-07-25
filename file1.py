import f1 as f1

array = [a, 21, 65, 4, fe, rer, 34, asd]
with open("f1.txt", "w") as file:
    array.sort(key=lambda x: len(x))
    print(array)
    file.write(array)
print("Привет")