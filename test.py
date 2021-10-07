lst = []
lst_1 = []
lst_2 = []

for i in range(6):
    lst.append(input())

for h in range(len(lst)):
    if h % 2 == 0:
        lst_1.append(lst[h])

for j in range(len(lst)):
    if j % 2 != 0:
        lst_2.append(lst[j])

print(", ".join(lst_1))
print(", ".join(lst_2))