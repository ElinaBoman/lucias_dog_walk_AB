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

#data ***


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
    """
    print('Calculating revenue...')
    price = SHEET.worksheet('price').get_all_values()
    price_row = price[-1]
    print(price_row)



def main():
    """
    Run all program function
        """
    data = get_number_of_walks()
    walks_data = [int(num) for num in data]
    update_walks_worksheet(walks_data)
    calculate_revenue_data(walks_data)

print('Welcome to Lucias dog walk AB!')
main()