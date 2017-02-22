import time


questions = ['Is the project a Nu-Heat Heat Pump? ', 'Is the project over 200 sqm? ', 'Is the project bigger than 120 sqm of Lo-Pro? ', 'Is the project over 60 sqm of Lo-Pro Max? ']
designTeam = 'a runner.'
for question in questions:
    answer = input(question)
    if answer.lower() == 'yes':
        designTeam = 'a repeater.'
        break
print('This is', designTeam)

time.sleep(10)




