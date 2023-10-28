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
    print('Example: 1, 2, 3, 4\n')

    data_str = input('Enter number of walks here: ')
    
    #This splits the data by the (,) to make it into a list.
    #The list will be added to the worksheet.
    walks_data = data_str.split(',')
    validate_data(walks_data)
    

def validate_data(values):
    """
    Validates the numbers inserted by user
    """
    print(values)

    try: 
        if len(values) != 4:
            raise ValueError(
        f'Please enter 4 values, you provided {len(values)}'
        )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')


#print('Welcome to Lucias dog walk!')
get_number_of_walks()

