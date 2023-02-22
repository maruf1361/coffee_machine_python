MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def resources_availability(coffee):
    for item in coffee:
        if coffee[item] >= resources[item]:
            print(f"Sorry! We ran out of {item}")
            return False
        else:
            return True


def calculate_coins():
    list_of_coins = ['quarters', 'dimes', 'nickles', 'pennies']
    coins_equivalencies = [0.25, 0.1, 0.05, 0.01]
    usd = 0
    for number in range(len(list_of_coins)):
        ask = input(f"How many {list_of_coins[number]}")
        dollar_conversion = float(ask) * coins_equivalencies[number]
        usd += dollar_conversion
    if usd > drink_cost:
        remaining = round(usd - drink_cost)
        print(f"Here is ${remaining} in change")
        return f"Here's your {prompt}! Enjoy!!"
    elif usd < drink_cost:
        return "Not enough money! Please Refill"

    else:
        return f"Here's your {prompt}! Enjoy!!"


def update_ingredients_amount(coffee):
    for item in coffee:
        remaining_amount = resources[item] - coffee[item]
        resources[item] = remaining_amount
    return resources

def report():
    for item in resources:
        print(f"{item} = {resources[item]}")
    return f"money = {money}"





machine_on = 0

while machine_on == 0:

    prompt = input("What would you like? (latte/ espresso/ cappuccino) ")

    if prompt == "report":
        print(report())
    elif prompt == "off":
        machine_on = 1
    else:
        drink = MENU[prompt]["ingredients"]
        drink_cost = MENU[prompt]["cost"]
        if resources_availability(drink):
            print(calculate_coins())
            update_ingredients_amount(drink)
            money =+ drink_cost

# I have a function that checks if the coffee making ingredients are enough or not.
# I have another function that asks for coins and calculates the coins.

#TODO: Now I have to make a function which I will run after the ingredients check function and calculation function.
# This new function will take the drink name and then access the ingredients in the machine resources and subtract the
# amount of coffee ingredients from the machine resources.


#TODO: Now I have make an another function for the report. This function will show how many ingredients remaining


























