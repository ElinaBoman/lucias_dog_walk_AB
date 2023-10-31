import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import pyfiglet
import os
import time
import random 
from sty import fg


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
    Get number of walks input from the user
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
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
            f'Please enter 4 values, you provided{len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
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


def calculate_revenue_data(walks_row):
    """
    Calculates earnings for each dog and day
    Every walk is multiplyed with the price per walk (5$)
    """
    print('Calculating revenue...')
    price = SHEET.worksheet('price').get_all_values()
    price_row = price[-1]
 
    global price_data
    price_data = []
    for walks, price in zip(walks_row, price_row):
        price_for_walk = walks * 5
        price_data.append(price_for_walk)
    print(price_data)


def update_price_data(price_data):
    """
    Updates price worksheet with calculated prices.
    The returned value is the price for each dog and day.
    """
    print('Updating price worksheet...\n')
    price_worksheet = SHEET.worksheet('price')
    price_worksheet.append_row(price_data)
    print('Price worksheet updated successfully!\n')

    return price_data


def validate_dog_name():
    """
    Validates input from user to check if name is in register.
    If name not in valid_dog_names user will get a print message to try again.
    This will loop until the name is inside register.
    """
    price_worksheet = SHEET.worksheet('price').row_values(1)
    
    while True:
       
        print('Please enter name of dog.\n')
        dog_name = (input('Enter name of dog:\n'))
        dog_name = dog_name.capitalize()
        
        if dog_name not in price_worksheet:
            print('Name is invalid')
            print(f'No dog named {dog_name}.')
        else:
            print('Name is valid!\n')
            return False      
    return (dog_name)


def calculate_price_for_one_dog(dog_name):
    """
    Calculates total price for one dog
    """
    price = SHEET.worksheet('price')
    str_name = input('Dog name: ')
    str_name = str_name.capitalize()
    
    if str_name == 'Lou':
        values_list = price.col_values(1)
        values_to_use = [int(num) for num in values_list[1:]]
        total_value_lou = sum(values_to_use)
        print(f'The total price for Lou is ${total_value_lou}')

    elif str_name == 'Bently':
        values_list = price.col_values(2)
        values_to_use = [int(num) for num in values_list[1:]]
        total_value_bently = sum(values_to_use)
        print(f'The total price for Bently is ${total_value_bently}')

    elif str_name == 'Spookie':
        values_list = price.col_values(3)
        values_to_use = [int(num) for num in values_list[1:]]
        total_value_spookie = sum(values_to_use)
        print(f'The total price for Spookie is ${total_value_spookie}')
        
    elif str_name == 'Baltzar':
        values_list = price.col_values(4)
        values_to_use = [int(num) for num in values_list[1:]]
        total_value_baltzar = sum(values_to_use)
        print(f'The total price for Baltzar is ${total_value_baltzar}')
        
    else:
        print('Name not found.')
    """
    columns = []
    for ind in range(1, 5):
        column = price.col_values(ind)
        columns.append(column[1:])
    
    return columns
    """


def calculate_total_price(data):
    """
    Calculate columns data
    """
    print('Calculate price data...')
    new_price_data = []

    for column in data:
        int_column = [int(num) for num in column]
        total_price = sum(int_column)
        new_price_data.append(total_price)
    print(new_price_data)


def clear_terminal():
    """
    Clear terminal when functions have updated walks and price worksheet.
    Code was designed togheter with ChatGPT.
    """
    time.sleep(5)
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
    Generates colord text in terminal
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
    dog_name = validate_dog_name()
    calculate_price_for_one_dog(dog_name)


    
#clear_terminal()
    
    #calculate_total_price(price_columns)

"""
Figlet text
"""
print(pyfiglet.figlet_format("Dog Walk AB",font='big',width=110))
print('Welcome to Lucias dog walk AB!\n')
red, green, blue = generateRGB()
color = generateColor(red, green, blue)
print(color)
main()

"""
walks_worksheet = SHEET.worksheet('walks')
val = walks_worksheet.acell('B1').value
print(val)
"""