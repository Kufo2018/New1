import sqlite3
import pymysql
from tabulate import tabulate
from prettytable import PrettyTable
import sys

universal = []

a = {}


def welcome_menu():
    # Display these on startup
    print(
        """ 
    It's a bright and sunny day!!!
    Welcome to Kufco Stores\n
    """
    )


def kufco_database_name_display():
    # Connecting to the database
    db = pymysql.connect("localhost", "root", "root", "python_class")
    # Prepare cursor object using cursor()method
    cursor = db.cursor()
    # prep SQL query to Read a record from the database
    query = "SELECT id, name FROM kufco"
    # Execute SQL command
    cursor.execute(query)
    for columns in cursor:
        print(tabulate([columns]))
    # disconnect from server
    db.close()


def kufco_database_full_display():
    # Connecting to the database
    db = pymysql.connect("localhost", "root", "root", "python_class")
    # Prepare cursor object using cursor()method
    cursor = db.cursor()
    # prep SQL query to Read a record from the database
    query = "SELECT * FROM kufco"
    # Execute SQL command
    cursor.execute(query)
    for (id, name, category, price, stock) in cursor:
        print("{}. {} {} {} {}".format(id, name, category, price, stock))
    # disconnect from server
    db.close()


def prices_only():
    # Connecting to the database
    db = pymysql.connect("localhost", "root", "root", "python_class")
    # Prepare cursor object using cursor()method
    cursor = db.cursor()
    # prep SQL query to Read a record from the database
    query = "SELECT price FROM kufco"
    # Execute SQL command
    cursor.execute(query)
    for columns in cursor:
        universal = columns
        print(universal)
    # disconnect from server
    db.close()


def items_prices():
    # Connecting to the database
    db = pymysql.connect("localhost", "root", "root", "python_class")
    # Prepare cursor object using cursor()method
    cursor = db.cursor()
    # prep SQL query to Read a record from the database
    query = "SELECT id, name, price FROM kufco"
    # Execute SQL command
    cursor.execute(query)
    for columns in cursor:
        print(tabulate([columns]))
    # disconnect from server
    db.close()


def purchase_instructions():
    # Declaring global variables
    global user_list, ask, item_stock, stock_available, user_qty
    max_list_of_items = 4

    # Getting user input
    user_list = input("\nEnter the item you wish to purchase and press the enter button: \n")

    # Validating user_list
    while user_list.lower() not in item_validation():
        print("That item is not available in our inventory, please try again")
        user_list = input("\nEnter the item you wish to purchase and press the enter button: \n")

    # Call this method to handle user_qty and validation
    # stock_validation()

    # Getting user quantity
    user_qty = input("Enter the quantity of the items you wish to purchase: \n")

    # Comparing user_qty with value in database
    # Database queries
    db = pymysql.connect("localhost", "root", "root", "python_class")
    cursor = db.cursor()
    query = "SELECT stock FROM kufco WHERE name LIKE '%s'" % user_list
    cursor.execute(query)
    for x in cursor:

        # Saving stock available in a string
        stock_available = x[0]
        # Comparing user_qty with stock
        while int(user_qty) > int(stock_available):
            print("We have only " + str(stock_available) + " in stock\n")
            user_qty = input("Enter the quantity of the items you wish to purchase: \n")

    # Saving item and stock into a dictionary
    item_stock = {user_list: user_qty}
    a.update(item_stock)
    print(a)

    # Asking if user wants to make further purchases
    ask = input("\nDo you want to buy another item?\n\nYes or No: ")
    i = 0
    while ask.lower() == "yes" or "no":
        if ask.lower() == 'yes':
            if i < max_list_of_items:

                # Selecting additional items for purchase
                user_list = input("\nEnter your item then press the enter button to select the quantity: \n")
                while user_list.lower() not in item_validation():
                    print("\nThat item is not available in our inventory, please try again\n")
                    user_list = input("\nEnter the item you wish to purchase and press the enter button: \n")
                else:
                    # Selecting quantity of additional items for purchase
                    user_qty = input("\nEnter the quantity of the items you wish to purchase: \n")

                    # Call this method to handle user_qty and validation
                    # stock_validation()

                    # Comparing user_qty with value in database
                    # Database queries
                    db = pymysql.connect("localhost", "root", "root", "python_class")
                    cursor = db.cursor()
                    query = "SELECT stock FROM kufco WHERE name LIKE '%s'" % user_list
                    cursor.execute(query)
                    for x in cursor:
                        # Saving stock available in a string
                        stock_available = x[0]

                    while int(user_qty) > int(stock_available):
                        print("Invalid choice!" + " We have only " + str(stock_available) + " in stock\n")
                        user_qty = input("Qty: ")

                    # compiling user_list and qty into a dictionary
                    else:
                        item_stock = {user_list: user_qty}
                        a.update(item_stock)
                        i += 1
                        print("\nYou have " + str(4 - i) + " orders left\n")
                        ask = input("\nDo you want to buy another item?\nYes or No: \n")
            else:
                print("\nYou can only order five items\nHere is your order list")

                # prints total order in the form of a dictionary
                print(a)
                return a
        elif ask.lower() == 'no':
            print("\nOkay, here is your order list\n")

            # prints total order in the form of a dictionary
            print(a)
            return a
        else:
            print("\nThat is an invalid option!\n")
            ask = input("\nDo you want to buy another item?\nYes or No: \n")


def purchases_computation():
    # Note to self: find a way to get the inventory from database in a list format

    global price_coke, price_apple, price_baked_beans, price_cards, price_doughnut

    valid_prices = {"coke": "150", "apple": "200", "baked_beans": "200", "cards": "800", "doughnut": "80"}
    valid_prices_keys = ([*valid_prices])
    # print(valid_prices_keys)  # prints the items in store

    valid_prices_values = list()
    for i in valid_prices.values():
        valid_prices_values.append(i)
    # print(valid_prices_values)  # prints the prices of items in store

    user_list = list()
    for i in a.keys():
        user_list.append(i)
    # print(user_list)  # prints the listitem_validation of items user has bought

    user_qty = list()
    for j in a.values():
        user_qty.append(j)
    # print(user_qty)  # prints the quantity of each item the user has bought

    false_key = "falsekey"
    if false_key == "falsekey":
        if "coke" in a.keys():
            coke_ordered = int((a.get("coke")))
            coke_price = int(valid_prices.get("coke"))
            price_coke = coke_ordered * coke_price
        else:
            price_coke = 0
        if "cards" in a.keys():
            cards_ordered = int((a.get("cards")))
            cards_price = int(valid_prices.get("cards"))
            price_cards = cards_ordered * cards_price
        else:
            price_cards = 0
        if "apple" in a.keys():
            apple_ordered = int((a.get("apple")))
            apple_price = int(valid_prices.get("apple"))
            price_apple = apple_ordered * apple_price
        else:
            price_apple = 0
        if "doughnut" in a.keys():
            doughnut_ordered = int((a.get("doughnut")))
            doughnut_price = int(valid_prices.get("doughnut"))
            price_doughnut = doughnut_ordered * doughnut_price
        else:
            price_doughnut = 0
        if "baked_beans" in a.keys():
            baked_beans_ordered = int((a.get("baked_beans")))
            baked_beans_price = int(valid_prices.get("baked_beans"))
            price_baked_beans = baked_beans_ordered * baked_beans_price
        else:
            price_baked_beans = 0


def total_prices():
    total_price = price_coke + price_apple + price_baked_beans + price_doughnut + price_cards
    print("\nThe total price for items purchased is: NGN", total_price)
    print("\nThank you for coming, see you some other time.")


def item_validation():
    # Connecting to the database
    db = pymysql.connect("localhost", "root", "root", "python_class")
    # Prepare cursor object using cursor()method
    cursor = db.cursor()
    # prep SQL query to Read a record from the database
    query = "SELECT * FROM kufco"
    # Execute SQL command
    cursor.execute(query)
    # this makes a list of all the names of the items present in the inventory
    items = []
    stock = []
    for name in cursor:
        items.append(name[1])
    return items


def main():
    # Display these options to the user
    user_input = None
    while user_input != "0":
        welcome_menu()
        print(
            """
            How may we be of assistance to you?
            0 = Quit
            1- View Inventory
            2- Purchase Items
            """
        )
        # User options
        user_input = input("Kindly enter your option here: ")
        if user_input == "0":
            print("\nThanks for coming, we hope to see you next time!")
        elif user_input == "1":
            print("\nHere are the items present in the inventory")
            kufco_database_full_display()
            user_choice = input("\nDo you want to purchase anything?\n\nPlease type a yes or no: ")
            while user_choice.lower() == '\nyes' or 'no':
                if user_choice.lower() == 'yes':
                    purchase_instructions()
                elif user_choice.lower() == 'no':
                    purchases_computation()
                    print("\nThanks for coming, we hope to see you next time")
                    break
                else:
                    print("That is an invalid choice!")
                    main()
                    # this should be a function that goes immediately to the purchases section
        elif user_input == "2":
            purchase_instructions()
            print("\nIs the list above correct?\n")
            answer = input("yes or no: ")
            if answer == "yes":
                purchases_computation()
                total_prices()
                main()
            elif answer == "no":
                print("Please try again, more carefully")
                main()
            else:
                print("That is invalid\nPlease try again, more carefully")
                main()
        else:
            print("You have selected an invalid option!")
            main()


main()

# extra code snippets
# OR
# print([*a])

# idea, if user list is less than five, populate it with fake data
#
# """
#             How may we be of assistance to you?
#             0 = Quit
#             1- View Inventory
#             2- Purchase Items
#             3- Add Items to Inventory
#             4- Delete Items from Inventory
#             5- Modify Items in Inventory
#             """
