#Pattern Problem Set-1

for i in range(3):
    for j in range(5):
        print("*" , end=" ")
    print()

Hollow Rectangle
Answer
for i in range(3):
    for j in range(5):
        if(i==0 or i == 2 or j == 0 or j == 4):
            print("*" , end=" ")
        else:
            print(" ", end=" ")
    print()

Pattern Problem Set-2

Half Pyramid
Answer
for i in range(6):
    for j in range(i+1):
        print("*" , end=" ")
    print()

Inverted Half Pyramid
Answer
for i in range(6):
    for j in range(6-i):
        print("*" , end=" ")
    print()

A hollow inverted half pyramid
Answer
for i in range(6):
    for j in range(6-i):
        if ( i == 0 or i == 5 or j == 0 or j == 6-i-1):
            print("*" , end=" ")
        else :
            print(" " , end = " ")
    print()

Pattern Problem Set-3
Answer

.
.
Half pyramid with numbers
Answer
for i in range(6):
    for j in range(i+1):
        print(j+1 , end=" ")
    print()
.
.
Inverted Half pyramid with numbers
Answer
for i in range(6):
    for j in range(6-i):
        print(j+1 , end=" ")
    print()
.
Hollow half pyramid
Answer
for i in range(6):
    for j in range(i+1):
        if (i == 0 or i == 5 or j == 0 or j == i) :
            print(j+1 , end=" ")
        else :
            print(" " , end=" ")
➔
    print()
.
.
Pattern Problem set-5


Solid diamond
Answer
for i in range(5):
    for j in range(5-i-1):
        print(" " , end="")
    for k in range(i+1):
        print("*" , end=" ")
    print()
➔
for i in range(5):
    for j in range(i):
        print(" " , end="")
    for k in range(5-i):
        print("*" , end=" ")
    print()


#
for i in range(5):
    for j in range(5-i-1):
        print(" " , end="")
    for k in range(i+1):
        if ( k == 0 or k == i):
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()
➔
for i in range(5):
    for j in range(i):
        print(" " , end="")
    for k in range(5-i):
        if k == 0 or k == 5-i-1 :
            print("*" , end=" ")
        else:
            print(" " , end=" ")
    print()


Solid half diamond
for i in range(6):
    for j in range(i+1):
        print("*" , end=" ")
    print()


for i in range(5):
    for j in range(5-i):
        print("*" , end=" ")
    print()


