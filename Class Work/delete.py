value=["_","_","_",
       "_","_","_",
       " "," "," "]


def display_board():
    print(value[0]+"|"+value[1]+"|"+value[2])
    print(value[3]+"|"+value[4]+"|"+value[5])
    print(value[6]+"|"+value[7]+"|"+value[8])
    print()

display_board()

position=int(input("put your position here")) #5
value[position]="X"
display_board()