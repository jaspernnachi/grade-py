greet= 'Welcome to Learnfactory!'
students_name = input('Enter your name: ')
print(f'{students_name}! {greet}')
exam_score = float(input('Enter your exam score: '))

if exam_score <= 0 or exam_score > 100:
    print(f'{students_name}Your {exam_score} is an Invalid score')
else:
    if exam_score >=90 or exam_score == 100:
        print(f'{students_name} Your score is {exam_score}. \nYou did excellent! \nYou got an A!')
    elif exam_score >= 80 or exam_score == 89:
        print(f'{students_name} Your score is {exam_score}. \nYou did great! \nYou got a B!')
    elif exam_score >= 70 or exam_score ==79:
        print(f'{students_name} Your score is {exam_score}. \nBravo! \nYou got a C!')
    elif exam_score >= 60 or exam_score ==69:
         print(f'{students_name} Your score is {exam_score}. \nYou made it! \nYou got a D!')
    elif exam_score >=50 or exam_score ==59:
        print(f'{students_name} Your score is {exam_score}. \nYou passed! \nYou got an E!')
    elif exam_score <49:
        print(f'{students_name} Your score is {exam_score}. \nYou failed! \nYou got an F!')