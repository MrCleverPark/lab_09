import random
import logging
logging.basicConfig(level=logging.INFO, filename="Log.log",filemode="w")
guesses_made = 0
while True: 
    try:
        N=int(input('Введите предел чисел:'))
        logging.info('User entered upper limit:'+str(N))
        break
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз')
        logging.info('User entered'+str(N))
while True:
    try:
        K=int(input('Введите количество попыток:'))
        logging.info('User entered '+str(K)+'try ')
        break
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз')
        logging.info('User entered'+str(K))
number = random.randint(1, N)
while guesses_made < K:
    while True: 
        try:
            guess = int(input('Введи число: '))
            break
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз')
            logging.info('User entered'+str(guess))
    # увеличиваем счетчик числа попыток
    guesses_made += 1
    if guess < number:
        print ('Твое число меньше того, что я загадал.')
        logging.info('User number(' + str(guess) +') turned out to be less than predicted (' + str(guess) + ')')
    if guess > number:
        print ('Твое число больше загаданного мной.')
        logging.info('User numbe(' + str(guess) +') turned out to be more than expected (' + str(guess) + ')')
    if guess == number:
        break
if guess == number:
    print ('Ты угадал число, использовав',guesses_made, 'попыток!')
    logging.info('The user guessed the number ' + str(number) +' with ' + str(guesses_made ) + ' attempts')
else:
    print ('Попытки закончились, я загадал число',number)
    logging.info("The user did not guess on the "+str(K)+' try')
