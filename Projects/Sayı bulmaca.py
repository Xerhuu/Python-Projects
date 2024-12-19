print("Try to find the chosen number")
print("--------------**-------------")

import random   
is_run = True
guesses = 0

print("************************")
print()
print("1-Easy mod= 0 - 10")
print("2-Medium mod= 0 - 100")
print("3-Hard mod= 0 - 1000")
print()
print("************************")

choice = (input("Pick a difficualty to play : "))

if choice == '1':
   minimum =0
   maximum =10
elif choice =='2':
   minimum=0
   maximum =100
elif choice =='3':
   minimum =0
   maximum =1000
else:
   print("İnvalid number, try again.")
   

sayı = random.randint(minimum, maximum)

while is_run:
    guess = int(input("Make a guess : "))
        
    if guess < minimum or guess > maximum:
        if maximum == 10:
           print("Wrong guess, guess beetwen 1 and 10. ")
        elif maximum == 100:
           print("Wrong guess, guess beetwen 1 and 100. ")
        elif maximum ==1000:
           print("Wrong guess, guess beetwen 1 and 1000. ")
    elif guess < sayı:
      print("Your number is lower then the chosen number, try again.")
      guesses +=1
    elif guess > sayı:
      print("Your number is higher then the chosen number.")
      guesses +=1
    else: 
      guesses +=1
      print("You find the number, well done.")
      print(f"You found the answer with in {guesses} try.")
      is_run= False  
        


