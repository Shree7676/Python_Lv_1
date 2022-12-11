#100,80,60,70,60,75,85 >> 1,1,1,2,1,4,6
#10, 4, 5, 90, 120, 80 >> 1 1 2 4 5 1
l=[100,80,60,70,60,75,85]
#l=[10, 4, 5, 90, 120, 80]
span=[1]
for x in range(1,len(l)):
    c=0
    for y in range(x,-1,-1):
        print(l[x], l[y])
        if l[x]>=l[y]:
            c+=1
        else:
            print(y,"hi")
            break
    print()
    print()
    span.append(c)

print(span)
