MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made else False"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many 5's?: "))
    total += int(input("How many 10's?: "))
    total += int(input("How many 20's?: "))
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted else False"""
    if money_received >= drink_cost:
        if money_received > drink_cost:
            change = round(money_received - drink_cost)
            print(f"Here is {change} Rs. change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough monet. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name}")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/cappuccino/latte)")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: {profit} Rs")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

