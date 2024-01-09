import random

bigboard=[]
count=0

#welcome message
print("Hello, this is a two player tic-tac-toe game!\nWhen the board generates and it's your turn, enter a number, and that space on \nthe board will be filled.\nHave fun!")

#board size
y = input("\nWould you like a randomly generated board (yes or no)? ")

if y.lower()=='yes':
    x=random.randint(3,5)
    a=x
    print("\nYou will have a",x,"by",x,"board:")
else:
    a = int(input("How long would you like each side of the board to be (an integer from 3 to 5)? "))
    if 3<=a<=5:
        print("\nHere is your",a,"by",a,"board:")
    else:
        while a>5 or a<3:
            a = int(input("Please pick an integer from 3 to 5: "))
        if 3<=a<=5:
            print("\nHere is your",a,"by",a,"board:")

print("")
for i in range(1,(a**2)+1):
    bigboard.append(i)

for j in range(1,(a**2)+1):
    print("%3.0f"%bigboard[j-1], end=' ')
    if (j)%a==0:
        print("")
        print("")

n=len(bigboard)

#checking for wins
def checkWin(board):
    if len(board)==9:
        for i in range(3):
            if board[i]==board[i+3]==board[i+6]=='X' or board[i]==board[i+3]==board[i+6]=='O':
                return True
        for i in range(0,7,3):
            if board[i]==board[i+1]==board[i+2]=='X' or board[i]==board[i+1]==board[i+2]=='O':
                return True
        if board[0]==board[4]==board[8]=='X' or board[0]==board[4]==board[8]=='O':
            return True
        if board[2]==board[4]==board[6]=='X' or board[2]==board[4]==board[6]=='O':
            return True
    elif len(board)==16:
        for i in range(4):
            if board[i]==board[i+4]==board[i+8]==board[i+12]=='X' or board[i]==board[i+4]==board[i+8]==board[i+12]=='O':
                return True
        for i in range(0,13,4):
            if board[i]==board[i+1]==board[i+2]==board[i+3]=='X' or board[i]==board[i+1]==board[i+2]==board[i+3]=='O':
                return True
        if board[0]==board[5]==board[10]==board[15]=='X' or board[0]==board[5]==board[10]==board[15]=='O':
            return True
        if board[3]==board[6]==board[9]==board[12]=='X' or board[3]==board[6]==board[9]==board[12]=='O':
            return True
    elif len(board)==25:
        for i in range(5):
            if board[i]==board[i+5]==board[i+10]==board[i+15]==board[i+20]=='X' or board[i]==board[i+5]==board[i+10]==board[i+15]==board[i+20]=='O':
                return True
        for i in range(0,21,5):
            if board[i]==board[i+1]==board[i+2]==board[i+3]==board[i+4]=='X' or board[i]==board[i+1]==board[i+2]==board[i+3]==board[i+4]=='O':
                return True
        if board[0]==board[6]==board[12]==board[18]==board[24]=='X' or board[0]==board[5]==board[10]==board[15]==board[24]=='O':
            return True
        if board[4]==board[8]==board[12]==board[16]==board[20]=='X' or board[4]==board[8]==board[12]==board[16]==board[20]=='O':
            return True
    return False

def miniGame():
    global board1
    global counts
    board1=[]

    for i in 'abcdefghi':
        board1.append(i)

    #count=0 #for ties 
    counts=0 #minigame ties

                ### MINIGAME
    for j in range(1,10):
            print("%3s"%board1[j-1], end=' ')
            if (j)%3==0:
                print("")
                print("")
    
    while checkWin(board1)==False:
        d = (input("\nPlease enter a number, Player 1: "))
        while d.isdigit()==False:
            d=input("\nPlease enter a number, Player 1: ")
        d=int(d)
        if d<=9 and d>=1:
            if board1[d-1]!='X' and board1[d-1]!='O':
                board1[d-1]='X'
                counts+=1
            else:#####
                while board1[d-1]=='X' or board1[d-1]=='O':
                    d = (input("\nPlease enter another number since the slot is already filled: "))
                    while d.isdigit()==False:
                        d=input("\nPlease enter a number, Player 1: ")
                    if d.isdigit()==True:####!
                        while int(d)>9 or int(d)<1:
                            d = (input("\nPlease enter a number that is on the board: "))
                            while d.isdigit()==False:
                                d=input("\nPlease enter a number, Player 1: ")
                    d=int(d)
                if board1[d-1]!='X' and board1[d-1]!='O':
                    board1[d-1]='X'
                    counts+=1
        else:
            while d>9 or d<1:
                d = (input("\nPlease enter a number that is on the board: "))
                while d.isdigit()==False:
                    d=(input("\nPlease enter a number, Player 1: "))
                if d.isdigit()==True:
                    while int(d)<=9 and int(d)>=1:
                        while board1[int(d)-1]=='X' or board1[int(d)-1]=='O':
                            d = (input("\nPlease enter another number since the slot is already filled: "))
                            while d.isdigit()==False:
                                d = input("\nPlease enter a number, Player 1: ")
                    
                d = int(d)

                if board1[d-1]!='X' and board1[d-1]!='O':
                    board1[d-1]='X'
                    counts+=1
                    
        for j in range(1,10):
            print("%3s"%board1[j-1], end=' ')
            if (j)%3==0:
                print("")
                print("")
                
        #checkWin(board1)
        
        if checkWin(board1) == True:  
            print("Player 1, you win this minigame!")
            bigboard[n-1]='X'
            board1=[]#reset minigame board

            for i in 'abcdefghi':
                board1.append(i)
                

                
            break 
        if counts==9:
            print("This minigame ended in a tie!")
            bigboard[n-1]='-'
            break ###

        
        d = (input("\nPlease enter a number, Player 2: "))
        while d.isdigit()==False:
            d=input("\nPlease enter a number, Player 2: ")
        d=int(d)
        if d<=9 and d>=1:
            if board1[d-1]!='X' and board1[d-1]!='O':
                board1[d-1]='O'
                counts+=1
            else:#####
                while board1[d-1]=='X' or board1[d-1]=='O':
                    d = (input("\nPlease enter another number since the slot is already filled: "))
                    while d.isdigit()==False:
                        d=input("\nPlease enter a number, Player 2: ")
                    if d.isdigit()==True:####!
                        while int(d)>9 or int(d)<1:
                            d = (input("\nPlease enter a number that is on the board: "))
                            while d.isdigit()==False:
                                d=input("\nPlease enter a number, Player 2: ")
                    d=int(d)
                if board1[d-1]!='X' and board1[d-1]!='O':
                    board1[d-1]='O'
                    counts+=1
        else:
            while d>9 or d<1:
                d = (input("\nPlease enter a number that is on the board: "))
                while d.isdigit()==False:
                    d=(input("\nPlease enter a number, Player 2: "))
                if d.isdigit()==True:
                    while int(d)<=9 and int(d)>=1:
                        while board1[int(d)-1]=='X' or board1[int(d)-1]=='O':
                            d = (input("\nPlease enter another number since the slot is already filled: "))
                            while d.isdigit()==False:
                                d = input("\nPlease enter a number, Player 2: ")
                    
                d = int(d)

                if board1[d-1]!='X' and board1[d-1]!='O':
                    board1[d-1]='O'
                    counts+=1
                    
        for j in range(1,10):
            print("%3s"%board1[j-1], end=' ')
            if (j)%3==0:
                print("")
                print("")
                
        #checkWin(board1)
        
        if checkWin(board1) == True:  
            print("Player 2, you win this minigame!")
            bigboard[n-1]='O'
            board1=[]#reset minigame board

            for i in 'abcdefghi':
                board1.append(i)

                
            break 
        if counts==9:
            print("This minigame ended in a tie!")
            bigboard[n-1]='-'
            break ###

    #######end  

#actual game, taking turns taking input
while checkWin(bigboard)==False:
    n = input("\nPlease enter a number, Player 1: ")
    while n.isdigit()==False:
       n = input("\nPlease enter a number, Player 1: ")
    n = int(n)
    if n <= len(bigboard) and n>=1:
        if bigboard[n-1]!='X' and bigboard[n-1]!='O' and bigboard[n-1]!='-':
            miniGame()
            count+=1
        else:
            while bigboard[n-1]=='X' or bigboard[n-1]=='O' or bigboard[n-1]=='-':
                n = (input("\nPlease enter another number since the slot is already filled: "))
                while n.isdigit()==False:
                    n = input("\nPlease enter a number, Player 1: ")
                n = int(n)
            if bigboard[n-1]!='X' and bigboard[n-1]!='O' and bigboard!='-':
                miniGame()
                count+=1         
    else:
        while n>len(bigboard) or n<1:
            n = input("\nPlease enter a number that is on the board: ")
            while n.isdigit()==False:
               n = input("\nPlease enter a number, Player 1: ")
            n = int(n)
        if bigboard[n-1]!='X' and bigboard[n-1]!='O' and bigboard[n-1]!='-':
                miniGame()
                count+=1

    for j in range(1,(a**2)+1):
        print("%3s"%bigboard[j-1], end=' ')
        if (j)%a==0:
            print("")
            print("")

    if checkWin(bigboard) == True:
        print("Player 1, you win!")
        break
    if count==len(bigboard):
        print("It's a tie!")
        break
    #SECOND PLAYER TURN
    n = (input("\nPlease enter a number, Player 2: "))
    while n.isdigit()==False:
       n = input("\nPlease enter a number, Player 2: ")
    n = int(n)
    if n <= len(bigboard) and n>=1:
        if bigboard[n-1]!='X' and bigboard[n-1]!='O' and bigboard!='-':
            miniGame()
            count+=1
        else:
            while bigboard[n-1]=='X' or bigboard[n-1]=='O' or bigboard[n-1]=='-':
                n = (input("\nPlease enter another number since the slot is already filled: "))
                while n.isdigit()==False:
                   n = input("\nPlease enter a number, Player 2: ")
                n = int(n)
            if bigboard[n-1]!='X' and bigboard[n-1]!='O' and bigboard[n-1]!='-':
                miniGame()
                count+=1
    else:
        while n>len(bigboard) or n<1:
            n = (input("\nPlease enter a number that is on the board: "))
            while n.isdigit()==False:
               n = input("\nPlease enter a number, Player 2: ")
            n = int(n)
        if bigboard[n-1]!='X' and bigboard[n-1]!='O' and bigboard[n-1]!='-':
                miniGame()
                count+=1


    for j in range(1,(a**2)+1):
        print("%3s"%bigboard[j-1], end=' ')
        if (j)%a==0:
            print("")
            print("")

    #checkWin(bigboard)
    if checkWin(bigboard)==True:
        print("Player 2, you win!")
        break

    if count==len(bigboard):
        print("It's a tie!")
        break
