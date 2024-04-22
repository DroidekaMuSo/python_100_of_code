from data import MENU, resources

is_on = True
current_resources = resources


def check_stocks(ingredients):
    if "milk" in ingredients:
        if ingredients['milk'] > current_resources['milk'] and ingredients['coffee'] > current_resources['coffee'] and ingredients['water'] > current_resources['water']:
            return False
        else:
            return True
    else:
        if ingredients['coffee'] > current_resources['coffee'] and ingredients['water'] > current_resources['water']:
            return False
        else:
            return True


def prepare_beverage(ingredients):
    for ingredient in current_resources:
        current_resources[ingredient] -= ingredients[ingredient]


def check_count(quarters, dimes, nickels, pennies, beverage_price):
    coins_inserted = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)
    total = round(beverage_price - coins_inserted, 2)

    return total


while is_on:
    beverage = input("What would you like?").lower()

    if beverage == 'off':
        is_on = False
    elif beverage == 'report':
        print(current_resources)
    elif beverage in MENU:
        print(f"{beverage.title()} costs ${MENU[beverage]['cost']}")

        quarter = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nickel = int(input("How many nickels?"))
        pennie = int(input("How many pennies?"))

        change = check_count(quarter, dime, nickel, pennie, MENU[beverage]['cost'])

        if change > 0:
            print("Not enough money. \n Money refunded")
        else:
            if "milk" not in MENU[beverage]['ingredients']:
                MENU[beverage]['ingredients']['milk'] = 0

            if check_stocks(MENU[beverage]['ingredients']):
                prepare_beverage(MENU[beverage]['ingredients'])
                print(f"Here's your {beverage} and your change ${-change}")
            else:
                print("Not enough resources")

    else:
        print("Invalid option")
