item_code = {
    "1A": "Coke", "1B": "Diet Coke",
    "1C": "Pepsi", "1D": "Coke Zero",
    "2A": "7Up", "2B": "Fanta",
    "2C": "Sprite", "2D": "Mirinda",
    "3A": "Gatorade", "3B": "Orange Juice",
    "3C": "Iced Tea", "3D": "Water"
}
item_stock = {
    "1A": 10, "1B": 10,
    "1C": 10, "3A": 10,
    "3D": 10, "1D": 10,
    "2C": 10, "2A": 10,
    "2B": 10, "2D": 10,
    "3B" : 10, "3C" : 10,
}
item_price = {
    "1A": 260, "1B": 350,
    "1C": 230, "1D": 325,
    "2A": 300, "2B": 255,
    "2C": 275, "2D": 270,
    "3A": 610, "3B": 475,
    "3C": 445, "3D": 100
}

receipt = []

def display_items():
    print(f"{'Code':<5} {'Name':<15} {'Price($)':<10} {'Stock':<5}")
    print("=" * 40)
    for code in item_code:
        price = item_price[code] / 100
        stock = item_stock[code]
        print(f"{code:<5} {item_code[code]:<15} {price:<10.2f} {stock:<5}")
        print("-" * 40)
    print("=" * 40)


def get_funds():
    while True:
        amount = float(input("Enter funds: $"))
        if amount > 0:
            return int(amount * 100)
        elif amount <= 0:    
            print("Amount must be positive.")
        else:
            print("Invalid amount. Try again.")


def buy_item(bal):
    code = input("Enter item code: ").upper()

    if code not in item_code:
        print("Invalid item code.")
        return bal

    if item_stock[code] == 0:
        print(f"{item_code[code]} is out of stock.")
        return bal

    price = item_price[code]

    if bal < price:
        print("Insufficient funds.")
        return bal

    item_stock[code] -= 1
    bal -= price
    print(f"Dispensing {item_code[code]}")
    print(f"Remaining balance: ${bal / 100:.2f}")

    receipt.append((item_code[code], price))

    return bal


def print_receipt(bal):
    print("=" * 30)
    print("        RECEIPT")
    print("=" * 30)

    if not receipt:
        print("No items purchased.")
    else:
        total = 0
        for name, price in receipt:
            print(f"{name:<15} ${price / 100:.2f}")
            total += price

        print("-" * 30)
        print(f"{'Total':<15} ${total / 100:.2f}")

    print(f"{'Change':<15} ${bal / 100:.2f}")
    print("=" * 30)


def calc_change(bal):
    quarters = bal // 25
    change = quarters * 25
    print(f"Your change is ${change / 100:.2f}")


def main():
    bal = 0

    while True:
        display_items()

        while True:
            bal += get_funds()
            print(f"Current balance: ${bal / 100:.2f}")

            cont = input("Add more funds? (Y/N): ").upper()
            if cont != "Y":
                break

        while True:
            bal = buy_item(bal)
            cont = input("Buy another item? (Y/N): ").upper()
            if cont != "Y":
                break

        cont = input("Make another transaction? (Y/N): ").upper()
        if cont != "Y":
            break

    calc_change(bal)
    print_receipt(bal)


if __name__ == "__main__":
    main()
