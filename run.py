import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import os
import time
import random
from sty import fg, rs


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Lucias_dog_walk_AB')


def get_number_of_walks():
    """
    Get number of walks input from the user.
    This code has been inspired by Code Institutes Love Sandwiches project.
    """
    while True:
        print('Please enter number of walks for each dog')
        print('Data should be separated by commas')
        print('Each number represents total walks for one dog in a day')
        print('Enter walks in following order: Lou, Bently, Spookie, Baltzar')
        print('Example: 1, 2, 3, 4\n')

        data_str = input('Enter number of walks here: \n')
        walks_data = data_str.split(',')

        if validate_data(walks_data):
            print('Data is valid!')
            break
    return walks_data


def validate_data(values):
    """
    Validates the numbers inserted by user
    This code is from Code Institutes Love Sandwiches project.
    It has been adjusted to suit this program.
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(f'Enter 4 integer values, you provided{len(values)}')
    except ValueError as e:
        print(f'Invalid data, please try again.\n')
        print('Please try again.\n')
        return False

    return True


def update_walks_worksheet(data):
    """
    Updates walks worksheet.
    """
    print('Updating walks worksheet...')
    walks_worksheet = SHEET.worksheet('walks')
    walks_worksheet.append_row(data)
    print('Walks worksheet updated successfully.\n')


def update_price_data(price_data):
    """
    Updates price worksheet with calculated prices.
    The returned value is the price for each dog and day.
    """
    print('Updating price worksheet with todays combined walks...\n')
    price_worksheet = SHEET.worksheet('price')
    price_worksheet.append_row(price_data)
    print('Price worksheet updated successfully!\n')


def calculate_revenue_data(walks_row):
    """
    Calculates earnings for each dog and day
    Every walk is multiplyed with the price per walk (5$)
    """
    print('Calculating daily revenue for all dogs...')
    price = SHEET.worksheet('price').get_all_values()
    price_row = price[-1]
    global price_data

    price_data = []
    for walks, price in zip(walks_row, price_row):
        price_for_walk = walks * 5
        price_data.append(price_for_walk)
    print(price_data)


def calculate_price_for_one_dog():
    """
    Calculates total price for one dog.
    First this function wants to know if this function should run or exit.
    If user wants to continue, the program searches for name of dogs in
    register.
    If the name is in register, the total price for choosen dog will be
    displayed.
    Then the nested argument wants to know if the price column should be
    cleared.
    If "Yes" is enterd the program will clear price and walk columns in worksheet.
    Then the program will return to the While loop.
    """
    price = SHEET.worksheet('price')
    walks = SHEET.worksheet('walks')
    price_worksheet = SHEET.worksheet('price').row_values(1)
    while True:
        print('Would you like to calculate the total price for a dog?')
        print('Enter name of dog or "Exit."')
        print('Dogs in register are Lou, Bently, Spookie and Baltzar.')
        str_name = input('Name of dog: or "Exit" \n')
        str_name = str_name.capitalize()

        if str_name == 'Exit':
            print('Thank you for today!')
            break

        elif str_name not in price_worksheet:
            print(f'No dog named {str_name} in register.')
            print('Please try again...')

        else:
            if str_name == 'Lou':
                values_list = price.col_values(1)
                values_to_use = [int(num) for num in values_list[1:]
                                 if num.strip() and num.strip().isdigit()]
                total_value_lou = sum(values_to_use)
                print(f'Total revenue for Lou is ${total_value_lou}')
                print('If the total price for Lou has been paid,')
                print('you can clear total price for Lou.')
                print(f'{fg.red}If price is cleard data is lost{rs.all}')
                clear_column = input('Type "Yes" to clear or press "Enter".\n')
                if clear_column.capitalize() == 'Yes':
                    price.batch_clear(['A2:A100'])
                    walks.batch_clear(['A2:A100'])
                    print('Lou has been cleared!')
                    print('Good job!')

            elif str_name == 'Bently':
                values_list = price.col_values(2)
                values_to_use = [int(num) for num in values_list[1:]
                                 if num.strip() and num.strip().isdigit()]
                total_value_bently = sum(values_to_use)
                print(f'Total revenue for Bently is ${total_value_bently}')
                print('If the total price for Bently has been paid,')
                print('you can clear total price for Bently.')
                print(f'{fg.red}If price is cleard data is lost{rs.fg}')
                clear_column = input('Type "Yes" to clear or press "Enter".\n')
                if clear_column.capitalize() == 'Yes':
                    price.batch_clear(['B2:B100'])
                    walks.batch_clear(['B2:B100'])
                    print('Bently has been cleared!')
                    print('Good job!')

            elif str_name == 'Spookie':
                values_list = price.col_values(3)
                values_to_use = [int(num) for num in values_list[1:]
                                 if num.strip() and num.strip().isdigit()]
                total_value_spookie = sum(values_to_use)
                print(f'Total revenue for Spookie is ${total_value_spookie}')
                print('If the total price for Spookie has been paid,')
                print('you can clear total price for Spookie.')
                print(f'{fg.red}If price is cleard data is lost{rs.fg}')
                clear_column = input('Type "Yes" to clear or press "Enter".\n')
                if clear_column.capitalize() == 'Yes':
                    price.batch_clear(['C2:C100'])
                    walks.batch_clear(['C2:C100'])
                    print('Spookie has been cleared!')
                    print('Good job!')

            elif str_name == 'Baltzar':
                values_list = price.col_values(4)
                values_to_use = [int(num) for num in values_list[1:]
                                 if num.strip() and num.strip().isdigit()]
                total_value_baltzar = sum(values_to_use)
                print(f'Total revenue for Baltzar is ${total_value_baltzar}')
                print('If the total price for Baltzar has been paid,')
                print('you can clear total price for Baltzar.')
                print(f'{fg.red}If price is cleard data is lost{rs.all}')
                clear_column = input('Type "Yes" to clear or press "Enter"\n')
                if clear_column.capitalize() == 'Yes':
                    price.batch_clear(['D2:D100'])
                    walks.batch_clear(['D2:D100'])
                    print('Baltzar has been cleared!')
                    print('Good job!')
            else:
                print('Name not found.')


def clear_terminal():
    """
    Clear terminal when functions have updated walks and price worksheet.
    Code was designed togheter with ChatGPT.
    """
    time.sleep(3)
    os.system('clear')


def generateRGB():
    """
    Generates color
    """
    red = random.randint(100, 256)
    green = random.randint(100, 256)
    blue = random.randint(100, 256)
    return red, green, blue


def generateColor(red, green, blue):
    """
    Generates colored text in terminal
    """
    return fg(red, green, blue)


def main():
    """
    Run all program function
    """
    red, green, blue = generateRGB()
    generateColor(red, green, blue)

    data = get_number_of_walks()
    walks_data = [int(num) for num in data]
    update_walks_worksheet(walks_data)
    calculate_revenue_data(walks_data)
    update_price_data(price_data)
    calculate_price_for_one_dog()
    clear_terminal()


"""
Figlet text
"""
print(pyfiglet.figlet_format("Dog Walk AB", font='big', width=110))

"""
Text that will show before main ()
"""
print('Welcome to Dog Walk AB!\n')
print('Let us store number of walks and calculate your revenue!')
print('The price for one walk is $5.')
print('Dogs in the register are Lou, Bently, Spookie and Baltzar.\n')
print('Follow the instructions to enter number of walks.')
print('After that we will calculate daily revanue.\n')
print('If you would like to see total cost for a specific dog,')
print('we will fetch thoose numbers for you!\n')
print("Let's enter todays walks and calculate the total price!")

red, green, blue = generateRGB()
color = generateColor(red, green, blue)
print(color)

main()