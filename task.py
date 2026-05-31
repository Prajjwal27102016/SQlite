name = "prajjwal singh mandloi"
list1=[0]
for i in range(len(name)):
    if name[i]==" ":
        list1.append(i+1)

print (list1)

for i in range(len(name)):
    if i in list1:
        print(name[i].upper(), end="")
    else:
        print(name[i], end="")