import art
from game_data import data
import random
from replit import clear

print(art.logo)

global score
score=0

global stopgame
stopgame=False

def get_data():
  
    global compare_aa
    
    

    compare_aa = random.choice(data)
    
    global string_a
    string_a =f"Compare A: {compare_aa['name']}, {compare_aa['description']} from {compare_aa['country']}."

    return (string_a)


def get_data_2():
    global compare_b
    compare_b = random.choice(data)
    global string_b
    string_b=f"Compare B: {compare_b['name']}, {compare_b['description']} from {compare_b['country']}.  "

    return (string_b)


def check_followers(guess):
    follower_a = compare_aa['follower_count']
    follower_b = compare_b['follower_count']
    # print(max(follower_a,follower_b))
    

    if (follower_a > follower_b and guess == "a"):
      
        
     
      results = string_a
      next_stage(results)

    elif (follower_b > follower_a and guess == "b"):
        
        results = string_b
        next_stage(results)
    else:
        
        print("Wrong Guess! Game Over")
        print(f"Your final score:{score}")
        stopgame=False
       

def next_stage(results):
  
 
  if results == string_a:
    
    clear()
    print(art.logo)
    score+=1    
    print(f"You are right. Your Score is: {score}")
    print(f"{results}")
    print(art.vs)
    print(get_data_2())
    guess_answer()
    
  if results == string_b:
    clear()
    string_aa = results
    string_bb = get_data_2()
    print(art.logo)
    score+=1
    print(f"You are right. Your Score: {score}")
    print(f"Compare A:{string_aa[10:]}")
    print(art.vs)
    print(string_bb)
    guess_answer()

def guess_answer():
  guess = input("Who has more followers A or B? Type 'A' or 'B' ").lower()
 
  
  answer=check_followers(guess)
  next_stage(answer)
  

def game():
  
  
  compare_A = get_data()
  print(compare_A)
  print(art.vs)
  print(get_data_2())
  
  guess_answer()
  



game()