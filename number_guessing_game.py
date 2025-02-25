import random 
no= random.randint(1,100)
while True:
 guess = int( input("Please guess the no between 1 and 100 "))
 if(guess>no):
    print("Too high!")
 elif(guess<no):
    print("Too low")
 elif(guess==no):
    print("You guess right!")
    break
 else:
  print("Invalid option!") 
