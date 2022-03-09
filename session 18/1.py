import random as r

n = 0
player_1 = 0
player_2 = 0
choices = [1,2,3]
while n < 5:
    player1=int(input('choose [1-3]: '))
    player2=r.randint(1,3)
    if player1 not in choices:
        print('choice in not valid, try again')
        continue
    print('computer: ',player2)
    if player1==player2:
        continue
    elif player1 < player2 and player1==1 or player1==2:
        if player2 ==3:
            player_2 +=1
        else:
            player_1 +=1
        n += 1
    elif player1 > player2 and player1==3:
        player_1 += 1
        n += 1
    else:
        player_2 +=1
        n += 1

if player_1 > player_2:
    print('You win')
else:
    print('You lose')
    

