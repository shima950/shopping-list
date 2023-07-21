import os
from difflib import SequenceMatcher


def cls():
    os.system('cls')


def show_list(shopping_list: list):
    for index, item in enumerate(shopping_list, start=1):
        product = item
        price = shopping_list[product]['price']
        number = shopping_list[product]['num']
        print(f'{index}- Name:{product} Price:{price} Number:{number}')


# def add_product(product, shoppin_list: list) -> bool:
#     if product in shoppin_list:
#         return False
#     else:
#         shoppin_list.append(product)
#         return True


def remove_item(removed_list, shopping_list: list):
    if removed_list in shopping_list:
        shopping_list.remove(removed_list)
    else:
        print('the product is not in list')


def search_in_list(shopping_list: list, item: str):
    if item in shopping_list:
        print('This item found')
    else:
        print('This item not found')


def edit_product(shopping_list: list) -> bool:
    product = input("enter your product for edit: ")
    if product in shopping_list:
        new_product = input("enter your product for update: ")
        index_product = shopping_list.index(product)
        shopping_list.remove(product)
        shopping_list.insert(index_product, new_product)
        return True
    else:
        return False


def show_help():
    print(
        '''
        1. Use `+` to add the product to the product basket.
        2. Use `show` for to see the entire list.
        3. Use `remove` for delete the things we dont want
        4. Use `search` to search for an item
        5. Use `edit` for edit item in list and update this
        '''
    )


def similarity(actual, expected):
    return SequenceMatcher(None, actual, expected).ratio()


def search_basket(basket: list, keyword: str) -> None:
    print(f"Search for {keyword}...")
    results = [
        (product, similarity(product, keyword))
        for product in basket
        if keyword.lower() in product.lower()
    ]
    if results:
        print(f'Found ({len(results)}) results:')
        for product, score in results:
            print(f'Product: {product}, Similarity Score: {score:.2f}')
    else:
        print("No result Found.")


def get_group(product: str, basket: dict) -> str:
    for item in basket:
        for i in basket[item]:
            if product == i:
                return item


def show_products(basket: dict) -> None:
    for group in basket:
        print(group)
        for index, product in enumerate(basket[group], start=1):
            price = basket[group][product]['price']
            number = basket[group][product]['num']
            print(f'\t{index}: {product} Price: {price:,} Number: {number}')
        print('-' * 20)


def add_product(product: str, number: int, basket: dict, shopping_list: dict) -> None:
    group = get_group(product, basket)  # clothing
    product = product  # pants
    number = number  # 5
    price = basket[group][product]['price']  # 530000
    # pants : {price: 530000, num: 5}
    shopping_list[product] = {'price': price, 'num': number}
    num = basket[group][product]['num']  # 105 - 5 = 100
    basket[group][product]['num'] = num - number  # 100


def check_role() -> str:
    while True:
        cls()
        role = input("Enter your role (customer/seller): ")
        if role == "seller" or role == "customer":
            print(f"You are {role}!")
            break
        else:
            print("Invalid role! Please try again.")
            input('Press ENTER to continue...')
            continue


def calculate_discount(total_amount, customer_type):
    discount_percentage = 0

    if customer_type == "normal":
        if total_amount >= 00000:
            discount_percentage = 5
    elif customer_type == "loyal":
        if total_amount >= 0000:
            discount_percentage = 10
    elif customer_type == "VIP":
        if total_amount >= 0000:
            discount_percentage = 15

    discount_amount = (total_amount * discount_percentage) / 100
    final_amount = total_amount - discount_amount

    return final_amount


def sign_in(user_name: str, password_user: str, USER: str, PASS: str) -> str:
    if user_name == USER and password_user == PASS:
        print("Registration successful!")
    else:
        raise Exception("Registration failed.")
