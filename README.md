# Dog Walk AB
***
Dog Walk AB is a personalized program for dog walking companies. This program will help user to keep trac of number of walks in a day for each dog. This program will also calculate the total price for each dog, by simply typing in the name of the dog.


- Link to deployed project:
https://dog-walk-ab-b6fc65e542c7.herokuapp.com/

- Link to Google spreadsheet:
https://docs.google.com/spreadsheets/d/1-z2f1tkFrZtLMJW0q38bZneJiyy5Eo5amcbG16H9BkQ/edit#gid=1820810552

![Am I responsive](docs/amiresponsive.png)

## How to use
To use the program, simply follow the instructions provided. Enter number of walks in presented order. Then if the user would like to see the total cost for a dog, enter name of the dog and the total price will be fetched! If the user would like to leave the  it is really simple. Just write exit and the program will finish and the reminal will clear it self.
*** 
## Features
*** 
### Existing Features
- Welcome text
The user is welcomed with a Pyfiglet styled text. This text displays the Dog Walk AB logo. This gives the otherwise bland terminal a fun decor.
The Welcome text provides the user with information on how to enter number of walks. If the user enters invalid information there will be a error message. Then the user will be asked to insert new values until the values are correct.

![Welcome text](docs/dog-walk-figlet.png)
![Welcome text](docs/enter-number.png)

- Updating worksheet
When user has enterd number of walks the information will be stored inside a worksheet called walks. By default the user will be informed of the daily revanue. The daily revanue will be stored in worksheet called prices. From this worksheet the user will be abel to extrect information of the total price for each dog.

![Update worksheet](docs/calculate-revenue.png)

- Exit program
When the user is ready to leave the program, he/she enters exit in the input. The program will then clear the terminal automatically after 5 second.

![Exit program](docs/calculate-exit.png)

- Color terminal
To make the program user friendly there is a color function that will randomly change the color of the text in the terminal. This is to make the program funnier to use.

### Future Features
- This app should in the future have the abillity to add a new dog to the program.
- There will be a delete function for the user to delete price for each dog when the price has been paid.
*** 
## Data Model
***
## Testing
### Following tests were carried out:
- User inputs will be handeld, if input value is incorrect this will be handeld with information of error.
- Walks worksheet updates with the right number of walks
- Each dog name collects correct value from price 
- Daily revanue calculates correctly and stores in price worksheet
- Exit function will close the program

### Bugs
 Problem with clear()
 When the clear() is carried out, the whole terminal is not cleared out. 
 Satus: Under investigation.

### Solved Bugs
Problem with deployment to Heroku. When trying to deploy project error message occured. This was because the import of gspread was never installed in the terminal.
Status: Fixed.

### Validator Testing
- PEP8 https://pep8ci.herokuapp.com/
  - Validation showed minor errors of whitespces. This errors were corrected. No effors left in program.
## Libraries and Software
### Libraries used:
- gspread- was used to handle Google Sheets API by Python
- pyfiglet- was used to write Dog Walk logo
- os- was used to be able to clear the terminal
- time- was used to set a timefunction to clear the terminal.
- random- was used to be abel to randomize color change in terminal
- sty- was imported to style text in terminal

### Software
- Github
- Heroku
- Codeanywhere


## Deployment
## Credits

### Youtube tutorials:
Learn Python Functions - Quick Python Project For Beginners by Python Simplified.

### Tutoring sessions
Tutoring sessions with Code Institute.

### Mentor
My fantastic mentor Brian O'Hare.

### ChatGPT
ChatGPT was used to explain python language. ChatGPT helped with explaining while loop, functions and try-except statements. 

### W3schools 
Was used to find information about Python language.

### gspred
Was used to find information on how to use gspread and access information in worksheet.


