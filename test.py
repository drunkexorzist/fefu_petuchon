lst=[]
lst1=[]
lst2=[]
for i in range(6):
    a=input()
    lst.append(a)
for j in range(6):
    if j%2==0:
        lst1.append(lst[j])
    else:
        lst2.append(lst[j])
str1=', '.join(lst1)
str2=', '.join(lst2)
print(str1)
print(str2)
