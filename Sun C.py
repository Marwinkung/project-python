lst1 = []
lst2 = []
dict1 = []
while True:
    x = input()
    if x == "$":
        break
    else:
        a,b = x.split()
        for i in range (len(lst1)):
            if lst1[i] == a:
                lst2[i] += (int(b))
        lst1.append(a)
        lst2.append(int(b))
print(lst1)
print(lst2)
