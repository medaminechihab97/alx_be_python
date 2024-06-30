import random
secretnumber = 0

secretnumber = random.randint(1,10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? :"))

match   (guess):
    case _ if guess == secretnumber :
        print("Congratulation, You guessed the number!!!")
    
    case _ :
        print ("please enter a valid number: ")

   # case != secret_number :
    #    print("oops, try again")    