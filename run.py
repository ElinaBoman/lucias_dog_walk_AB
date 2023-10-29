import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


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

        data_str = input('Enter number of walks here: ')
        
        #This splits the data by the (,) to make it into a list.*****
        #The list will be added to the worksheet.****
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
        f'Please enter 4 values, you provided {len(values)}'
        )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True


def update_walks_worksheet(data):
    """
    Turns data string into integers and updates walks worksheet.
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
    print('Updating price worksheet...')
    price_worksheet = SHEET.worksheet('price')
    price_worksheet.append_row(price_data)
    print('Price worksheet updated successfully!')

    return price_data


def calculate_price_for_one_dog():
    """
    Calculates total price for one dog and then clears price column
    """
    price = SHEET.worksheet('price')
    
    columns = []
    for ind in range(1, 5):
        column = price.col_values(ind)
        columns.append(column)
   return columns
    #print('Which dog would you like to calculate?')
    #dog_name = input('Enter name of dog here: ')


    #This should be to be able to choose wich dog to calculate:
    #valid_dog_names = ['Lou', 'Bently', 'Spookie', 'Baltzar']
   
   # while True:
        #if dog_name not in valid_dog_names:
            #print('Name is invalid')
            #input('Enter dog name here:\n')
            #return True
        
        #else:
            #print('Name is valid!')
            #return False
            #break


def main():
    """
    Run all program function
        """
    data = get_number_of_walks()
    walks_data = [int(num) for num in data]
    update_walks_worksheet(walks_data)
    calculate_revenue_data(walks_data)
    new_prices_data = update_price_data(price_data)
    calculate_price_for_one_dog()
    

    

print('Welcome to Lucias dog walk AB!')
#main()
price_columns = calculate_price_for_one_dog()