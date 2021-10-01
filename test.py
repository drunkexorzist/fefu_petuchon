lst = list(map(int, input().split()))

lst_max = max(lst)
lst_min = min(lst)

lst_out = []

for i in lst:
    a = lst.index(i)
    if a == lst.index(lst_max):
        lst_out.append(lst_min)
    else:
        lst_out.append(i)
        
print(*lst_out)