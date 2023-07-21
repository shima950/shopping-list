from shop.helper.const import (
    EXIT_COMMANDS,
    USERNAME,
    PASSWORD
)
from shop.utils.funcs import (
    cls,
    show_list,
    remove_item,
    search_in_list,
    show_help,
    add_product,
    edit_product,
    calculate_discount,
    sign_in,
    check_role
)


def main():
    basket = {
        'fruits': {
            "apple": {"price": 1000, "num": 70},
            "orange": {"price": 1500, "num": 50},
            "banana": {"price": 2000, "num": 30}
        },
        'food': {
            "pizza": {"price": 150000, "num": 5},
            "sandwich": {"price": 80000, "num": 20},
            "burger": {"price": 120000, "num": 8}
        },
        'drink': {
            "water": {"price": 5000, "num": 72},
            "milk": {"price": 25000, "num": 13},
            "soda": {"price": 26000, "num": 41}
        },
        'clothing': {
            "pants": {"price": 530000, "num": 105},
            "shirt": {"price": 220000, "num": 99},
            "T-shirt": {"price": 155000, "num": 140}
        },
    }
    shopping_list = dict()
    authentication = False
    while True:
        cls()
        while not authentication:
            cls()
            check_role()
            user_name = input('Enter username: ')
            password_user = input('Enter password: ')
            try:
                sign_in(user_name, password_user, USERNAME, PASSWORD)
                authentication = True
            except Exception as e:
                print(e)
                input('Press ENTER to continue...')
                continue
            except:
                print('Error 504!')
                input('Press ENTER to continue...')
                continue
        command = input("Enter your command:").lower()
        if command in EXIT_COMMANDS:
            show_list(shopping_list)
            break
        elif command == 'remove':
            cls()
            removed_product = input('what do you to remove?')
            remove_item(removed_product, shopping_list)
        elif command == 'search':
            cls()
            product = input('enter word: ')
            search_in_list(shopping_list, product)
            input('Press ENTER to continue...')
        elif command == 'help':
            cls()
            show_help()
            input('Press ENTER to continue...')
        elif command == 'show':
            cls()
            if shopping_list:
                show_list(shopping_list)
                input('Press ENTER to continue...')
            else:
                print('Shopping list is empty.')
                input('Press ENTER to continue...')
                continue
        elif command == 'clear':
            cls()
        elif command == '+':
            cls()
            product = input('Enter your product: ')
            number = input('How many of product: ')
            add_product(product, int(number), basket, shopping_list)
            print(f'the {product} is added to list and {len(shopping_list)} numbers item to list')  # noqa E501
            input('Press ENTER to continue...')
        elif command == 'edit':
            cls()
            show_list(shopping_list)
            edit = edit_product(shopping_list)
            if edit:
                print('Successfuly...')
                input('Press ENTER to continue...')
            else:
                print('The product is not in list.')
                input('Press ENTER to continue...')
        elif command == 'discount':
            customer_type = input(
                "Please specify the type of customer (VIP, loyal, normal): ")
            total_amount = float(input("Please enter the total purchase amount: "))

            print(calculate_discount(total_amount, customer_type))
