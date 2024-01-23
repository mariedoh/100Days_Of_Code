#Deleted the original cause i didn't like it
#Restarting with fingers crossed
#Need to figure out how to check resources
#Did that but now i'm getting some other issues
#Deleted again
#Wish me luck man
#The mker is workinggggggggggg
'''
import os
info = [
    {
        "name": "cappuccino",
        "coffee_needed": 24,
        "milk_needed": 100, 
        "water_needed" : 250,
        "price": 3.5
    },
    {
        "name": "expresso",
        "coffee_needed": 18,
        "milk_needed": 0, 
        "water_needed" : 50,
        "price": 1.5
    },
    {
        "name": "latte",
        "coffee_needed": 24,
        "milk_needed": 150, 
        "water_needed" : 200,
        "price": 2.5
    }
]
resources = {
    "milk": 200,
    "coffee": 100,
    "water" : 300
}
revenue = 0
cost = 0

def take_money():
    money = {
    "twenty_p" :0,
    "fifty_p" : 0,
    "one_cedi": 0,
    "two_cedi":0
    }
    payment=0
    try:
        money["twenty_p"] += (int(input("How many twenty pesewas coins? ")) *0.2)
        money["fifty_p"] += (int(input("How many fifty pesewas coins? "))*0.5)
        money["one_cedi"] += (int(input("How many one cedi coins? ")) *1)
        money["two_cedi"] += (int(input("How many two cedi coins? "))   *2) 
    except (ValueError):
        print(" Whole Numbers Only!!")
        return False
    return payment

def check_money(payment, cost, drink):
    global revenue
    if payment > cost:
        print(f"Here's your {drink} and the change of {(payment-cost)}")
        revenue += cost
        return True
    elif payment == cost:
        print(f"Here's your {drink}. See you later!!")
        revenue +=cost
        return True
    elif payment < cost:
        balance_needed = input(f"Insufficient funds. Extra {cost - payment} needed. Will you pay it, 'y' or 'n'? ")
        if balance_needed == "y":
            payment += take_money()
            check_money(payment, cost, drink)
        elif balance_needed == "n":
            print(f"Here's your {payment} back. Drop by again!!")
            quit()
        else:
            print("Wrong input!!")
            quit()

def main_program():
    print("Welcome to Barbie's Coffee")
    print("Today's menu: latte, expresso and cappuccino!")
    drink = input("What drink would you like to have? ").lower()
    if drink == "report":
        print(f"Coffee left: {resources['coffee']}")
        print(f"Milk left: {resources['milk']}")
        print(f"Water left: {resources['water']}")
        print(f"Profit: {revenue}")
    elif drink == "off":
        quit()
    elif drink in ("expresso", "latte", "cappuccino"):
        for x in info:
            if x["name"] == drink:
                cost = x["price"]
                if resources["coffee"] -  x["coffee_needed"] >= 0:
                    if resources["milk"] - x["milk_needed"] >=0:
                        if resources["water"] - x["water_needed"] >=0:  
                            print(f"That costs {cost}")
                            print("Please insert coins")
                            payment = take_money()
                            if payment is False:
                                print("Wrong Input!! Order Cancelled")
                                quit()
                            if check_money(payment, cost, drink):
                                resources["coffee"] -= x["coffee_needed"]
                                resources["milk"] -= x["milk_needed"]
                                resources["water"] -= x["water_needed"]

                        else:
                            print("Sorry, not enough water to make this drink")
                    else:
                        print("Sorry, not enough milk to make this drink")
                else:
                    print("Sorry not enough coffee to make this drink")
    else :
        print("That's not on the menu today. Sorry")


main_program()
another_one = input("Would you like another drink? 'y'or 'n' ").lower()
while another_one == "y":
    os.system("cls")
    main_program()
    another_one = input("Would you like another drink? 'y'or 'n' ").lower()

if another_one == "n":
    print("Goodbye")
    quit()
else:
    print("Wrong input!")
    another_one = input("Would you like another drink? 'y'or 'n' ").lower()
'''

#New Program Loading
