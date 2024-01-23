
#First day of 100Days of code 
#From Angela Yu's Python Course

#Challenge 1: Band Name Generator
'''
print("Welcome to the Band Generator")

first = input("What's the name of the city you grew up in?\n")
last = input("What's your pet's name? \n")
print("Your band name could be, " + first + " " + last + ".")

#Getting to know the Python Print Function
#Next Challenge,

print("Day 1 - Python Print Function \nThe function is declared like this:")
print("print(\"What to print\")")


#Next Challenge : Finding the length of a Name using Functions and len()
name = input("what is your name? ")
print(len(name))

def my_func_counter(String):
    counter = 0
    for x in String:
        counter+=1
    return counter

print(my_func_counter(name))

#Next Challenge: Switching values of variables
a = input("a: ")
b = input ("b: ")
c = a 
a = b
b =c
print("a: " + a)
print("b: " + b)

'''

#Day 2
#Treasure Island, Tip Calculator, Years_Left_to_live Calculator
'''
#Tip Calculator
print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? "))
num = float(input("How many people to split the bill? "))
tip_cent = float(input("What percent tip would you like to give, 10, 12, or 15? "))

total_bill = bill + ((bill*tip_cent)/100)
indi_bill = total_bill/num
indi_bill = round(indi_bill, 2)

print(f"Each person should pay: {indi_bill}")


#Sum_of_double_digit_numbers
two_digit_number = input("Enter a double digit number to be worked on. ")
counter = 0
for x in two_digit_number:
    counter+= int(x)
print(counter)


age = int(input("What is your current age? "))
years_left = 90- age
months_left = years_left * 12
weeks_left = years_left * 52
days_left =  years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left." )

#This one is huge
print(
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
'''



#Day3 Challenges
#Love Calculator, Pizza Bill Calculator, Even_Or_Odd number checker, Leap Year Function
'''
#Checks if a given number is even or odd
def odd_or_even(number):
    if number%2 == 0:
        print("It is an even number.")
    else:
        print("This is an odd number")


odd_or_even(int(input("Enter a number please. ")))


#This next challenge is to check whether a given year is a leap year or not.
def leap_or_nah(year):
    if (year% 4 ==0 and year% 100 == 0 and year% 400 != 0):
        print("This is not a leap year, love")
    elif year % 4== 0  and year%100== 0 and year % 400 ==0:
        print("This is a leap year.")
    elif (year%4 ==0):
        print("It's a leap year.")
    else:
        print("This is not a leap year. Try again next year.")


leap_or_nah(int(input("What year are you checking? ")))

#This challenge calculates the total bill of a customer at Python Pizza.
#Exceptions are handled.
print("Welcome to Python Pizza")
bill = 0
size = input("What size pizza would you like? S, M, or L? ").lower()
if (size == "s"):
    bill +=15
elif size == "m":
    bill +=20 
elif size == "l":
    bill +=25
else:
    print("Please use the specified letters and try again.")
    quit()

pepp = input("Would you like pepperoni toppings? Y or N? ").lower()
if (pepp == "y" and size == "s"):
    bill+= 2
elif pepp == "y" and size in ("m", "l"):
    bill+=3
elif pepp == "n":
    print("No pepporoni, noted.")
else:
    print("Please use the letters given.")
    quit()

cheese = input("Do you want extra cheese? Y or N? ").lower()
if (cheese == "y"):
    bill += 1
elif (cheese == "n"):
    print("No extra cheese, noted.")
else:
    print("Please use the stated letters.")
    quit()
#to use sys.exit you must import the sys module
print(f"Your bill is ${bill}.")

#Day 3 love Calculator
#Intro and information sourcing
print("Welcome to the love Calculator !")
name1 = (input("What is your first name?\n ")).lower().strip()
name2 =(input("What is your partner's first name?\n ")).lower().strip()
counter = 0 
#setting the names as lists
name_uno =[]
for x in name1:
    name_uno.append(x)

name_two = []
for y in name2:
    name_two.append(y)
#cancelling similarities
for p in name_uno:
    if p in name_two:
        name_uno.pop(counter)
        counter2 = name_two.index(p)
        name_two.pop(counter2)
    counter +=1
#removing unneccesary details
if "-" in name_uno:
    name_uno.remove("-")
if "-" in name_two:
    name_two.remove("-")

#Calculating the love   
letters_left = len(name_uno) + len(name_two)
flame = letters_left %6
if flame ==0:
    print("You are secret lovers.")
elif flame ==1:
    print("You are just friends. Find love elsewhere hun.")
elif flame ==2:
    print("You are lovers. Slay bestie")
elif flame ==3:
    print("You only admire each other.")
elif flame ==4:
    print("Y'all are getting married. Save me some food ai")
elif flame ==5:
    print("It will end in hate. Sorry babe.")
'''

#Day4
#Bill Roulette, Heads or Tails, Setting treasure.
'''
#Anyways, random heads or tails generator loading
import random
def heads_or_tails_gen(test_seed):
    rando = random.randint(0,test_seed)
    if rando%2 ==0:
        #even number
        print("Heads")
    elif rando%2 != 0:
        #odd number
        print("Tails")

def heads_or_tails_alt():
    #uses only 2 numbers
    rando = random.randint(0,1)
    if rando == 1:
        print("Heads")
    else:
        print("Tails")


seed = int(input("Create a seed number: "))
heads_or_tails_gen(seed)
heads_or_tails_alt()


#Bill Roulette
#Whose wallet is gonna bleed?
import random
def bill_rou(number, people):
    rando = random.randint(0, number-1)
    print(f"{people[rando]} is going to pay the bill.")

def bill_rou_pro(people):
    rando = random.choice(people)
    print(f"{rando} will pay the bill.")


people = (input("Give me everyone's names seperated by a comma and space. ")).split(",")
num = len(people)
bill_rou(num, people)
bill_rou_pro(people)


#Next challenge, Placing Treasure
#Nested lists.
row1 =["*", "*", "*"]
row2 = ["*", "*", "*"]
row3 = ["*", "*", "*"]

mapp = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

location = input("Where will you place the treasure? Enter the row and column number seperated by a space.")
loca = location.split(" ")
mapp[int(loca[1])-1 ][(int(loca[0]) - 1)] = "✖️"
print(f"{row1}\n{row2}\n{row3}")u
'''

#Day 5
#Password generator, FizzBuzz, and functions to calculate average and max height from a string, as well as even numbers w/n a range.
'''
#Password Generator
import random

letters = ["a","b", "c","d","e","f", "g","h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y","z",
           "A", "B","C", "D", "E","F","G","H","I","J","K","L","M","N", "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols =["!","@","#","$","%","^","&","*"]
numbers = [0,1,2,3,4,5,6,7,8,9]


req_lett = int(input("How many letters would you like in your password? "))
req_sym = int(input("How many symbols would you like? "))
req_num = int(input("How many numbers would you like in your password? "))

password = []

for x in range(0, req_lett):
    password.append(random.choice(letters))

for x in range(0, req_sym):
    password.append(random.choice(symbols))
for x in range (0, req_num):
    password.append(random.choice(numbers))

random.shuffle(password)
ppass =""
for x in password:
    ppass += str(x)

print(ppass)  

#the code runs fine so ignore them reds


#Average Heights
heights = (input("Enter a list of students heights seperated by a space. ")).split(" ")
summ = 0
num  = len(heights)

for x in heights:
    summ += int(x)

average_height = summ/num
print(round(average_height, 2))
#You can use the sum function, but i need to practice loops


#Highest_Score
#Again, i could've just used the max function but i need to practice loops

heights = (input("Enter a list of students heights seperated by a space. ")).split(" ")
highest_score = 0

for x in heights:
    if int(x) > highest_score:
        highest_score = int(x)

print(f"The highest score is {highest_score}.")

#Adding evens
def adding_evens(x,y):
    sum_of_evens = 0
    for p in range(x, y):
        if p %2 ==0:
            sum_of_evens += p
    
    print(sum_of_evens)


def adding_evens_pro(x,y):
    sum_of_evens = 0
    for p in range(x,y,2):
        sum_of_evens+=p

    print(sum_of_evens)


adding_evens(0,101)
adding_evens_pro(0,101)


#FizzBuzz coding challenge

def fizzbuzz(x, y):
    for p in range(x,y):
        if p%3 ==0 and p%5 ==0:
            print("FizzBuzz")
        elif (p%3==0):
            print("Fizz")
        elif (p%5 ==0):
            print("Buzz")
        else:
            print(p) 


fizzbuzz(0,101)

'''
#The rest of the day and days are continued in the file, Day7-100. Thanks
