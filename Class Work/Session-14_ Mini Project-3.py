Mini-Project 3
➔	Implement Rock Paper Scissors Game.
➔	Sample Code
➔	import random
➔	values = ["ROCK" , "PAPER" , "SCISSOR"]
➔
➔	while(True):
➔
➔	    c = random.choice(values)
➔
➔	    for i in range(len(values)):
➔	        print(i , "-->" , values[i])
➔	    u = int(input("Enter you choice : "))
➔
➔	    print("YOU -->" , values[u])
➔	    print("COMPUTER -->" , c)
➔
➔	    if ( c == values[u]):
➔	        print("Tie")
➔
➔	    elif c == values[0] :
➔
➔	        if u == values[1] :
➔	            print("YOU WON")
➔
➔	        else :
➔	            print("COMPUTER WON")
➔
➔	    elif c == values[1] :
➔
➔	        if u == values[0] :
➔	            print("COMPUTER WON")
➔
➔	        else:
➔	            print("YOU WON")
➔
➔	    elif c == values[2] :
➔
➔	        if u == values[1] :
➔	            print("YOU WON")
➔
➔	        else :
➔	            print("COMPUTER WON")
➔
➔	    out = int(input("Press 0 to exit any other key to continue :"))
➔
➔	    if ( out == 0):
➔	        break
➔
Homework question.

●	In the same mini-project add the following features :
○	Handle all the exceptions. - like show invalid input on the wrong input.
○	Ask how many times the user wants to play the game in the beginning.
○	Print the scoreboard at the end.
