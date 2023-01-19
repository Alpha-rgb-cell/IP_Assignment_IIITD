menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

def print_menu():
    print("Menu:")
    for i, item in enumerate(menu):
        print(f"{i+1}. {item[0]}, Rs {item[1]}")

def take_order():
    order = {}
    while True:
        item = input("Enter item number and quantity (e.g. '3 1'): ")
        if item == "":
            break
        try:
            item_num, quantity = map(int, item.split())
            if item_num < 1 or item_num > len(menu):
                print("Invalid item number.")
            else:
                item_name = menu[item_num-1][0]
                item_price = menu[item_num-1][1]
                if item_name in order:
                    order[item_name][0] += quantity
                    order[item_name][1] += quantity * item_price
                else:
                    order[item_name] = [quantity, quantity * item_price]
        except ValueError:
            print("Invalid input. Please enter a number.")
    return order

def print_bill(order):
    total_items = 0
    total_cost = 0
    print("BILL:")
    for item in order:
        quantity = order[item][0]
        cost = order[item][1]
        total_items += quantity
        total_cost += cost
        print(f"{item}, {quantity}, Rs {cost}")
    print(f"TOTAL, {total_items} items, Rs {total_cost}")

print_menu()
order = take_order()
print_bill(order)