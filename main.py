import pickle
import random
import keyboard
import sys

def main():
    username = input("Choose your username: \n")
    
    while ' ' in username or username.islower() == False:
        username = input("Enter a username with no spaces and in lowercase only:\n ")
    
    data = None
    try:
        with open('DataLawoulet.pkl', 'rb') as file:
            data = pickle.load(file)
            if data['username'] == username:
                print(f"Welcome back, {username}! Your current score is {data['score']}")
            else:
                print(f"New user {username}, let's start with a score of 0.")
                data = {'username': username, 'score': 0}
    except FileNotFoundError:
        print(f"New user {username}, let's start with a score of 0.")
        data = {'username': username, 'score': 0}
    
    while True:  
        pc_number = random.randint(0, 100)

        play = 5
        
        while play > 0:
            chosen_number = input(f"Pick a number between 0 and 100 ({play} chances remaining - Press 'K' to stop):\n ")
            
            if keyboard.is_pressed('K') or keyboard.is_pressed ('k'):
                print("You stopped the game.")
                sys.exit()
                
            
            while not (chosen_number.isdigit() and 0 <= int(chosen_number) <= 100):
                chosen_number = input("Pick a number between 0 and 100: \n")
            
            chosen_number = int(chosen_number)
            
            print(f"You picked {chosen_number} and the computer choosed {pc_number}")
            
            if chosen_number == pc_number:
                print("You win. You have {play}")
                data['score'] += 100  
                break  
            
            else:
                play -= 1
                if chosen_number > pc_number:
                    print(f"Your number is higher than the computer's number. You have {play} more play.\n Please pick another one.")
                elif chosen_number < pc_number:
                    print(f"Your number is lower than the computer's number.You have {play} more play. \n Please pick another one.")
            
            if play == 0:
                print("You've run out of chances. You lost.")
                break 
        
        print(f"Your current score is {data['score']}")
        
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break  
    
    with open('DataLawoulet.pkl', 'wb') as file:
        pickle.dump(data, file)
    
if __name__ == "__main__":
    main()

     


 



 

