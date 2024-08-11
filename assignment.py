score = 0
print('Hi there!, welcome to Favson Amazing quiz competition, where you get to win an awesome prizes, ')
proceed = input("To proceed input continue:-  ").strip()
if (proceed == "continue"):
    User_Name = input('Input your name:-  ').strip()
    print(User_Name, 'answer the following questions')
    Question1 =input("Who is the current president of Nigeria?\n\n ANS:  ").strip().capitalize()
    if (Question1 == "Tinubu"):
        score +=1
    else:
        score+=0
    Question2 =input('When did Nigeria got her independence?\n\n   ANS:    ').strip().capitalize()
    if (Question2 =='1960'):
        score+=1
    else:
        score +=0
    Question3 = input('4+4\n\n ANS:   ').strip()
    if (Question3 == '8'):
        score+=1
    else:
        score +=0 
    Question3 = input('Who is the richest person in the world\n\n ANS:   ').strip().capitalize()
    if (Question3 == 'Elon Musk'):
        score+=1
    else:
        score +=0 
    Question3 = input('How many countries are in Africa\n\n   ANS:   ').strip().upper()
    if (Question3 == '54'):
        score+=1
    else:
        score +=0 
    Question3 = input('Hoe many goe-political zones are  in Nigeria\n\n      ANS:   ').strip().upper()
    if (Question3 == '6'):
        score+=1
    else:
        score +=0 
    Question3 = input('How many states are in America\n\n    ANS:   ').strip().upper()
    if (Question3 == '50'):
        score+=1
    else:
        score +=0 
    Question3 = input('How many States are in Nigeria\n\n   ANS:   ').strip().upper()
    if (Question3 == '36'):
        score+=1
    else:
        score +=0
    Question3 = input('How many continents are in the world\n\n    ANS:   ').strip().upper()    
    if (Question3 == '7'):
        score+=1
    else:
        score +=0 
    Question3 = input('what is the name of the hottest desert in the world\n\n   ANS:   ').strip().upper()
    if (Question3 == 'Atacama Desert'):
        score+=1
    else:
        score +=0 
    Question3 = input('Who created github\n\n      ANS:   ').strip().upper()
    if (Question3 == 'Twitter'):
        score+=1
    else:
        score +=0 
    Question3 = input('Who created VS code\n\n    ANS:   ').strip().upper()
    if (Question3 == 'Microsoft'):
        score+=1
    else:
        score +=0 
    Question3 = input('How many local Goverments Areas are in Nigeria\n\n   ANS:   ').strip().upper()
    if (Question3 == '774'):
        score+=1
    else:
        score +=0    

    print('Dear candidate, your score is', score)
else:
    print("Oops sorry you're out of the game, will love to see you back again.")