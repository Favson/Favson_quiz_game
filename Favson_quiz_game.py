def quiz_game():
    #the score is used to set the score at 0 as default
    score = 0
    print('Hi there! Welcome to Favson Amazing Quiz Competition, where you get to win awesome prizes.')
    proceed = input("To proceed, input 'continue': ").strip()

    if proceed.lower() == "continue":
        user_name = input('Input your name: ').strip()
        print(f'Hi {user_name}, answer the following questions:')
        #a tupule storing the questions and answers
        questions_and_answers = [
            ("Who is the current president of Nigeria?", "Tinubu"),
            ("When did Nigeria get her independence?", "1960"),
            ("What is 4+4?", "8"),
            ("Who is the richest person in the world?", "Elon Musk"),
            ("How many countries are in Africa?", "54"),
            ("How many geo-political zones are in Nigeria?", "6"),
            ("How many states are in America?", "50"),
            ("How many states are in Nigeria?", "36"),
            ("How many continents are in the world?", "7"),
            ("What is the name of the hottest desert in the world?", "Atacama Desert"),
            ("Who created GitHub?", "Twitter"),
            ("Who created VS Code?", "Microsoft"),
            ("How many local government areas are in Nigeria?", "774"),
            ("What's the acroymn / Abb. for hyperText Markup Language", "HTML"),
            ("How many days are in a leap year?", "366"),
            ('Question: What is the chemical symbol for water?', "H2O"),
            ("What is the largest ocean on Earth?", "Pacific"),
            ("What is the smallest prime number?", "2"),
            ("What is the fastest land animal?", "cheetah"),
            ("Which on the planet is the hottest", "Venus"),
        ]
        #A for loop to keep track of the numbejring and also numbers the questions and made use the code is neat using the \n\n to add two line before prompting the user to answer
        for i, (question, correct_answer) in enumerate(questions_and_answers, start=1):
            user_answer = input(f'Question {i}: {question}\n\nANS: ').strip().capitalize()
            if user_answer == correct_answer.capitalize():
                score += 1
        
        if score < 10:
            print(f'Dear candidate, your score is {score}, Keep it up, you can do more next time'),
        elif score > 10:
            print(f'Dear {user_name}, congratulations on your success on this test, Your score is {score}')
    else:
        print("Oops! Sorry, you're out of the game. We'd love to see you back again.")

# Call the function to start the quiz
quiz_game()
