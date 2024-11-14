#Randomly select a secret number between 1-10.
#Ask the user to make a guess between 1-10.
#If the user is correct, print "Congratulations, You guessed the secret number!"
#If the user is too low, print "Too low!"
#If the user is too high, print "Too high!"

secret_number=4

guess= int(input("Guess a number between 1 and 10?"))

if guess== secret_number:
    print('Congratulations, You guessed the secret number!')
elif guess< secret_number:
    print('Too low!')
else:
    print('Too High!')

#random.randint() to make it like a fun solo game