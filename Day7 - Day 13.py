#Day 7
#How-Much-Paint Calculator, Prime number checker and Caesar's cipher
'''
#paint calculator
height = int(input("Height of Wall In Meters: "))
width = int(input(" Width of Wall In Meters: "))

#One paint can = 5m^3

def paint_calculator(h = height, w = width):
    surface_area = h * w
    num_cans = round(surface_area/5)
    return f" You need {num_cans}"


print(paint_calculator(height, width))

#prime_or_nah
def prime_or_nah(number):
    for x in range(2, 10):
        if number%x ==0 and number !=x:
            print("This is not a prime number!")
            break
        if number%x !=0 and x ==9:
            print("It is a prime number!")


num = int(input("What number are you checking? "))
prime_or_nah(num) 

#Caeser's Cipher
letters = ["a","b", "c","d","e","f", "g","h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y","z",
               "a","b", "c","d","e","f", "g","h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y","z"]

def caeser(t,s, d):
    if s>10:
        s = s%25
    coded_word = ""
    for x in t:
        if x.isalpha():
            og_loc = letters.index(x)
            if d == "encode":
                coded_word+= letters[og_loc + s]
            else:
                coded_word += letters[og_loc - s]
        else:
            coded_word+=x
    print(f" Here's the encoded result: {coded_word}")


def take_info():
    direction = input("Type \"encode\" to encode and \"decode\" to decode ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction in ("encode", "decode"):
        caeser(text, shift, direction)
    
    else:
        print("Recheck your input!")
        quit()

    start_over = input("Type \'yes\' to try again and \'no\' to leave. ")
    while start_over == "yes":
        take_info()
    else:
        quit()

        #This could also be done by creating a singular function to do what encrypt and decrypt are doing.
        #I've replaced them with Caeser

take_info()

#Again, ignore the reds
'''
#Day 8 travel_log and Secret Auction
'''
travel_log = [
    {"country" : "France",
    "visits" : 12,
    "cities" : ["Paris", "Lille", "Dijon"]
   },
   {
    "country" : "Ghana",
    "visits" : 5,
    "cities" : ["Accra", "Aflao", "Ho"]
   }
]

def add_new_country(count, visi, places_list):
    new_dic = {}
    new_dic["country"] = count
    new_dic["visits"] = visi
    new_dic["cities"] = places_list
    travel_log.append(new_dic)


add_new_country("Argentina", 5 , ["Messi's House", "IdkanycitiesinArgentina"])
print(travel_log)

#This is a Secret Auction
#Coolest one so far, lol.
#I'm in love
import os
my_dic = {}

def add_to_main():
    print("Welcome to the Secret Auction!")
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    my_dic[name] = bid


def run_else_stop():
    others = input("Are there any other bidders? \"yes\", or \"no\". ")

    while others == "yes":
        os.system("cls")
        add_to_main()
        others = input("Are there any other bidders? \"yes\", or \"no\". ")     

    else:
        chosen_name = [""]
        for x in my_dic:
            money = 0
            if my_dic[x] > money:
                money = my_dic[x]
                chosen_name[0] = x
    os.system("cls")
    print(f"The winner is {chosen_name[0]}")
        

add_to_main()
run_else_stop()
'''
#Day 9, Name formatter, Days in Months
'''
#This is to show the title function that changes all the first letter to caps and the rest small.
#Run this block of code to see
def my_func(fname, lname):
    if fname == "" or lname == "":
        return("You didn't enter both names.")
    else:
        return (fname.title() +" " + lname.title())


print(my_func("mfker", "HEloo"))

#Using leap Year function from Day3
#Checking how many days are in a given month from a given year
def leap_or_nah(year):
    if (year% 4 ==0 and year% 100 == 0 and year% 400 != 0):
        return False
    elif year % 4== 0  and year%100== 0 and year % 400 ==0:
        return True
    elif (year%4 ==0):
        return True
    else:
        return False
    
def days_in_month(y , m):
    month_days = [31, 28, 31,30,31, 30, 31, 31, 30, 31, 30, 31]
    months = ["january", "february", "march","april", "may", "june", "july", "august", "september","october","november", "december"]
    counter = 0
    if m not in months:
        return ("Invalid Month")
    for mon in months:
        if mon == m:
            if mon == "february" and leap_or_nah(y):
                return (month_days[counter] + 1)
            return month_days[counter]
        counter+=1 
    
    

year = int(input("Enter a year: "))
month = input("Enter a month: ").lower()
days = days_in_month(y = year,m= month)
print(days)
'''
'''
#Day 10
#Calculator
#Not a love Calculator nor a Bill Calculator or any of that, an actual Calculator

import operator

def calculator(beginner, nextt, operation):
    operators_ = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/" : operator.itruediv}
    result  = (operators_[operation])(beginner, nextt)
    action = f"{beginner} {operation} {nextt} = {result}"
    print(action)
    return result


#Taking input for the calculator
def take_info_and_calculate():
    print(''' 
#  _____________________
# |  _________________  |
# | | Barbie          | |
# | |_________________| |
# |  ___ ___ ___   ___  |
# | | 7 | 8 | 9 | | + | |
# | |___|___|___| |___| |
# | | 4 | 5 | 6 | | - | |
# | |___|___|___| |___| |
# | | 1 | 2 | 3 | | * | |
# | |___|___|___| |___| |
# | | . | 0 | = | | / | |
# | |___|___|___| |___| |
# |_____________________|
''')
    

    print("*art by Jeremy Olsen*")
    print("Welcome to Barbie's Calculator")
    #Exception Handling and taking the two operands
    try:
        beginner = float(input("What's the first number? "))
        next_num = float(input("What's the next number? "))
    except (ValueError):
        print("Numbers Only!!!")
        quit()

    print("+\n-\n*\n/")
    #Exception Handling
    operation = input("Pick an operation from the line above: ")
    if operation not in ("+", "-", "*", "/"):
        print("That is not incuded!!. Try again later!!")
        quit()

    return calculator(beginner, next_num, operation)


#calculating with the collected numbers
result = take_info_and_calculate()
keep_calc = True
while keep_calc:    
    cont = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'q' to leave: ")
    if cont not in ("y", "n", "q"):
        print("InvaLid Answer!!")
        quit()
    elif cont == "q":
        print("Goodbye")
        quit()
    elif cont == "y":
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        next_num = float(input("What's the next number? "))
        result = calculator(result, next_num, operation)
    elif cont == "n":
        take_info_and_calculate()

'''
#Black Jack
#Day 11
'''
#I think i misunderstood the game rules.
#Will leave the flawed version here until i feel like writing code again
#Tired af, 
#Tech_babe
#Editing_in_Progress
#Doneeeeeee,Everything works now

import random
import os
player_count = 0
dealer_count  =0   
player_deck =  []
dealer_deck  =[]
num_deals = 0
cards = [2,3,4,5,6,7,8,9,10,"j","k","q", "a"]
card_values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "k": 10, "q" :10, "j":10, "a":11}
def deal_player():
    #declaring all player varibales global
    global player_count
    global player_deck
    #Dealing the player
    player_card = random.choice(cards)
    if player_card == "a" and (player_count +11) >21:
        player_count +=1
    else:
        player_count += card_values[player_card]

    player_deck.append(player_card)

def deal_dealer():
    #declaring globals
    global dealer_count
    global dealer_deck
    #Dealing the dealer (Computer)
    dealer_card = random.choice(cards)
    if dealer_card == "a" and (dealer_count +11) >21:
        dealer_count +=1
        
    else:
        dealer_count += card_values[dealer_card]
    dealer_deck.append(dealer_card)

def loss_present():
    if player_count> 21:
        print("You Lost") 
        present_decks()
        return True
    
    elif player_count ==21 and len(player_deck) ==2 and dealer_count !=21:
        print("Computer Lost, You Have a BlackJack")
        present_decks()
        return True
    elif  dealer_count ==21 and len(dealer_deck) ==2:
        print("You lose, i have a BlackJack")
        present_decks()
        return True
    else:
        return False


def present_decks():
    global num_deals
    print(f"Your deck: {player_deck}, current score: {player_count}")
    if num_deals == 0 and not loss_present():
        print(f"The dealer has: {dealer_deck[0]}")
        num_deals +=1
    else:
        print(f"The dealer has {dealer_deck}.")


def check_win():
    if player_count > dealer_count:
        print("Player Wins!!")
        present_decks()
        quit()
    elif player_count == dealer_count:
        end_or_cont = input(f"Both your counts are {player_count}, Deal again ('y') or quit ('n')")
        if end_or_cont == "y":
            deal_player()
        elif end_or_cont == "n":
            print("No Winner!")
            present_decks()
            quit()
        else:
            print("Can't you read? You lost! ")
            quit()
    elif 21 >= dealer_count > player_count:
        print("Computer Wins")
        present_decks()
        quit()
    elif dealer_count > player_count and dealer_count > 21:
        print("You Win!!")
        present_decks()
        quit()
    else:
        return None
    

def main_game():
    starter = input("Do you want to play a game of BlackJack? Type 'y' or 'n'. ")
    if starter == "n":
        print("See you next time! Goodbye.")
        quit(0)
    elif starter == "y":
        #print('''
#Clear the triple quotes after this line
'''
           /\\
         .'  `.         _     _            _    _            _    
        '      `.      | |__ | | __ _  ___| | ___  __ _  ___| | __
     .'          `.    | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    {              }   | |_) | | (_| | (__|   <| | (_| | (__|   < 
     ~-...-||-...-~    |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
           ||                                 _/ |                
          '--`                               |__/                 )'''
#The triple quote below continues to the end of BlackJack.
'''
        deal_player()
        deal_player()
        deal_dealer()
        deal_dealer()

        if loss_present():
            quit()

        #Move on if no busts
        while not loss_present():
            present_decks()
            deal_again = input("Deal Again ('y') or pass ('n')? ")
            if deal_again == "y":
                loss_present()
                deal_player()
            elif deal_again not in ("y", "n"):
                print("'y' or 'n'!!")
                quit()

            while deal_again == "n":
                if dealer_count > 17:
                    check_win()
                else:
                    deal_dealer()
                    loss_present()
            

    else:
        print("Invalid Answer!! You've been sacked.")
        quit(1)


main_game()
restart = input("Would you like to go again? 'y' or 'n'. ")
if restart == "y":
    os.system("cls")
    main_game()
elif restart == "n":
    print("Good bye!!")
    quit()
else:
    print("Bitch Get Out With your Spelling Incapabilities!!")
    quit()

'''
#Day 12
#Number Guessing Game
'''
import random
number = random.randint(0,100)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 0 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
num_attempts = 0

if level == "easy":
    num_attempts +=10
elif level == "hard":
    num_attempts +=5
else:
    print("Wrong Input!")
    quit()

for x in range(0, num_attempts):
    print(f"You have {num_attempts} attempts remaining to guess the number!")
    #Exception handling for the guesses
    try:
        guess = int(input("Make a guess: "))
    except (ValueError):
        print("Must be a number!!")
    #Evaluating the guesses. Anything that is not the number should reduce attempts and in the end, show the number
    if guess == number:
        print("Yessirrrrrr!!")
        quit()
    else:
        if guess > number:
            print("Too high")
        
        elif guess < number:
            print("Too low")
        print("Try again")
        num_attempts -=1
    if num_attempts == 0:
        print(f"Sorry, You've run out chances. The number was, {number}")

'''
#Day 14
#Higher Or Lower Guessing Game
#The data alone took over 300 lines, i've moving this game to a new file and consequent days will be continued in a different file. Thank you