import gspread
from google.oauth2.service_account import Credentials


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
    print('Please enter number of walks for each dog')
    print('Data should be separated by commas')
    print('Each number represents total walks for one dog in a day')
    print('Example: 1, 2, 3, 4')

    data_str = input('Enter number of walks here: ')
    print(f'Number of walks provides is {data_str}')


get_number_of_walks()