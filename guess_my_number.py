print("Please think of a secret number between 0 and 100")

high = 100
low = 0

while True:
    guess = (high + low)//2
    print ('Is your secret number ' + str(guess) + '?')
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if hint == 'h':
        high = guess
    if hint == 'l':
        low = guess
    if hint == 'c':
       print('Game over. Your secret number was: ' + str(guess))
       break
    if (hint != 'h') and (hint != 'l') and (hint != 'c'):
       print("Sorry, I did not understand your input.")
