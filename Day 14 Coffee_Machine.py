menu = {
    "espresso" :{
        "ingredients":{
            "water":50,
            "coffee":18
        },
        "cost":1.5,
    },
    "latte" :{
            "ingredients":{
                "water":200,
                "milk":150,
                "coffee":24
            },
            "cost":2.5,
    },
    "cappuccino" :{
            "ingredients":{
                "water":200,
                "milk":100,
                "coffee":24,
            },
            "cost":3.0,
    },
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
    "money" : 0,
}



def report():
    """Print the report"""
    print(f"water : {resources["water"]}\nMilk : {resources["milk"]}\nCoffee : {resources['coffee']}\nMoney : {round(resources["money"],2)}")

def sufficient_resources(drink):
    """Retrun the True if resources are sufficent else retrun the iten which is less"""
    for item in menu[drink]["ingredients"].keys():
        if menu[drink]["ingredients"][item] > resources[item] :
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coin_calculater(drink):
    """If money is not sufficient return -1 else returns extra money and reduces the resources"""
    print("Please insert coins.")
    quarters = int(input("How Many quarters?: "))
    dimes = int(input("How Many dimes?: "))
    nickles = int(input("How Many nickles?: "))
    pennies = int(input("How Many pennies?: "))
    total_money = quarters*0.25  + dimes*0.10 + nickles*0.05 + pennies*0.01
    if total_money >= menu[drink]["cost"]:
        resouce_used(drink,total_money)
        return total_money - menu[drink]["cost"]
    return -1

def resouce_used(drink, money):
    """reduces the amount of resources used and updates money"""
    for item in menu[drink]["ingredients"].keys():
        resources[item] -= menu[drink]["ingredients"][item]
    resources["money"]+=money


def make_coffee(drink):
    """Make the coffee and return the extra money"""
    result = sufficient_resources(drink)
    if  result == True:
        sufficient_coin = coin_calculater(drink)
        if sufficient_coin == -1:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if sufficient_coin > 0:
                print(f"Here is ${round(sufficient_coin,2)} dollars in change.")
            print(f"Here is your {drink} Enjoy!")
        

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            report()
        elif choice == 'off':
            return
        else:
            make_coffee(choice)

coffee_machine()