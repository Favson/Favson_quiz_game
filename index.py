# print(500+500)
# # print()

# name = "Favour"
# print('My name is', name)

# firstname = "Favour"
# lastname = "Adebisi"
# Department = "Cybersecurity Expert"
# Institution = "SQI college of ICT"
# Religion = "Christian"
# Nationality = "Nigeria"
# State_of_origin = "Oyo State"
# Act_balance = "9000.5"
# Career = "I'm a career personnel, A tech enthusiast, a cybersecurity expert, studied at SQI college of ICT, ogbomosho, oyo state, Nigeria"
# Passion = "I'm a guy who is always passionate about making Africa a tech continent and Nigeria a dwellings of techies, And not just that i'm also passionate about making the gospel known to the world through my writing skills"


# print("I'm", lastname , firstname, "by name. I'm a", Department +" I studied at", Institution + " I'm a",Religion +" i'm from",Nationality, State_of_origin +" to be precise", "Currently I'm having $"+Act_balance, Career)

# print(f"I'm {lastname}{firstname} by name. I'm a {Department} I studied at {Institution}. I'm a {Religion}. I'm from {Nationality} {State_of_origin} to be precise. Currently I'm having ${Act_balance}")

# firstname, secondname = "Martins", "Martins"

# print(firstname, secondname)
# x=y=z=3
# water = 'omi'
# bottle = water, 'salt', 'sand', 'stone'
# print(bottle)



# value = complex(3j + 1)
# print(value)

# # Sequence type
# 1. list
# value = [2, 3, 4, True, "string", 45.6]
# basket = [
    # 'Garri',
    # 'Fruits',
    # 'floating berries'
# ]
# print(value)
# print(basket)

# bag = (
#     'laptop',
#     'books',
#     'charger',
#     'extension box'
# )
# print(len(bag))
# value = tuple((
#     'laptop',
#     'books',
#     'charger',
#     'extension box',
# ))
# print(value)

# # # 3. Range
# number = range(1, 101,2)
# print(list(number))

# # Set types
# Value = {1, 2, 3, 4, 4}
# guess_word = {
#     'Good',
#     'Amapiano',
#     'SQI',
#     'Arithmetics'
# }
# print(guess_word)
# print(Value)

# # Mapping datatypes
# # Python dictionary
# vehicles ={'model':'toyota Camry', 'Yop':2020, 'color':'grey'}
# print(vehicles)
# print(vehicles['model'])


# # Boolean datatypes
# # It's just true or false
# value = True
# print(type(value))

# number = [1, 2, 3, 4, 5]
# print(number[0])

# name = 'ayomide' #['A', 'y', 'o', 'm', 'i', 'd', 'e']
# print(name[4])

# print(ord('A'))

# # Binary datatype
# number = bin(10)
# print(number)

# number = bytes('ayomide', encoding='utf8')
# print(number)


# print(chr(90))

# value = 45.5
# val = str(value)
# print(type(val))

# print(int(value))

# setA = {'Eba', 'fufu'}
# print(tuple(setA))

# python_student = ['Paul', 'Victor', 'Favour', 'Samuel', 'Helen', 'Leumas']
# print('Leumas' not in python_student)

# fval = 45
# sval= 36
# print('45 = ',bin(fval)) #0b101101
# print('36 = ', bin(sval)) # 0b100100


# x = 6
# y = 10
# if y ==10 and x <=6:
#     print('correct')
# else:
#     print('wrong')

# degood_food = [
#     'rice',
#     'beans',
#     'bread'
# ]

# degood_comp = [
#     'meat',
#     'fish',
#     'egg'
# ]

# degood_drinks = [
#     'coke',
#     'fanta',
#     'exotic'
# ]

# user = input('Your Name: ').strip()
# user_food = input('food: ').strip().lower()
# user_comp = input('compliment: ').lower()
# user_drink = input('drink: ').lower()
# if (user_food in degood_food) and (user_comp in degood_comp) and (user_drink in degood_drinks):
#     print(f"""
#             Degood Resturant
#            Order from {user}
#            1. {user_food}
#            2. {user_comp}
#            3. {user_drink}

#            please serve {user}
#          """)
# elif (user_food in degood_food) or (user_comp in degood_comp) or (user_drink in degood_drinks):
#     print("""
#            Sorry, We don't have all your order
#            available foods are; rice, beans and bread
#             compliment are:- meat, fish, egg
#             while drinks:- coke, fanta,exotic
#            """)

# else:
#     print('order not available, please come back later.')

# comment = 'commented is a town hall different from bala blu, blue blu bulaba. broom broom broom brooooooooom. Bala blu blue blu bulaba. The farmers will make more money. Your lunch will not be imported, cassava garri ewa and ehhh ehhhhnn. The farmer will make money, the dinner would be cassava, eba, ewa and everything.'
# print(comment.startswith("commented"))
# print(comment.endswith("commented"))
# print(len(comment))

my_list = ['Mango', 'Apple', 'Plum', 'Watermelon', 'agbalumo', 'agbalumo', True, 67, 67.8, ['israel', 'Helen', 'Modecai'],]
# print(type(my_list))
# print(len(my_list))
# print()

# reassgining
# my_list[0] = 'Pawpaw'
# my_list[:5] = ['Ayomide', 'Tofunmi', 'dunmininu', 'Favour', 'Bayo']
# print(my_list)

# print(my_list[-1][2])
# print('palindrome checker' .center(50, '_'))
# user = input('Your Palindrome:- ').lower()
# if user.lower == user[::-1].lower():
#     print(f'{user} is a palindrome ')

# else:
#     print(f'{user} is not a palindrome')

# Functions Of list
# my_list.append("Mathew")
# print(my_list)

# print(my_list.index('Apple'))

# my_list.clear()
# print(my_list)

# my_list1 = ['akorede', 'ibadan', 'lanlate']
# my_list.append(my_list1)
# print(my_list)

# my_list.extend(my_list1)
# print(my_list)

# my_list.insert(3, 'David')
# print(my_list)

# my_list.pop(2)
# print(my_list)
# my_list.remove('Apple')
# print(my_list)

# del my_list
# print(my_list)

# num = [1, 5, 3, 6, 4, 2]
# print(sum(num)/len(num))
# print(max(num))

x = 1.
name_of_student = ['Favour', "Ayomide", "Mathew", 'Leumas', "Israel"]
for name in name_of_student:
    print(f"""
       Student {x}: {name}
    """)
    x+=1

    
# questions = [
#     "1. What is the name of nigeria president (a.) Tinubu (b.) Abubakar",
#     "2. What is the capital of Japan"
# ]

# answers = ['b', 'a']

# score = 0

# for ques, ans in zip(questions,answers):
#     print(ques)
#     user= input('Answer: ')
#     if user.strip().lower() == ans:
#         print('correct')
#         score+=5
#     else:
#         print('Why you no know book! go meet your papa')

# print(f'Your total score is {score}')