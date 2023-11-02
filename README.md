# Dog Walk AB

Dog Walk AB is a personalized program for dog walking companies. This program will help user to keep track of number of walks in a day for each dog. This program will also calculate the total price for each dog. By simply typing in the name of the dog the total price will be displayed.


- Link to deployed project:
https://dog-walk-ab-b6fc65e542c7.herokuapp.com/

- Link to Google spreadsheet:
https://docs.google.com/spreadsheets/d/1-z2f1tkFrZtLMJW0q38bZneJiyy5Eo5amcbG16H9BkQ/edit#gid=1820810552

![Am I responsive](docs/amiresponsive.png)

## How to use
To use the program, simply follow the instructions provided. Enter number of walks in presented order. Then if the user would like to see the total cost for a dog, enter name of the dog and the total price will be fetched! If the user would like to leave the program it is really simple. Just write exit and the program will finish and the terminal will clear it self.
*** 
## Features

### Existing Features
- Welcome text

The user is welcomed with a Pyfiglet styled text. This text displays the Dog Walk AB logo. This gives the otherwise bland terminal a fun decor.
The Welcome text provides the user with information on how to enter number of walks. If the user enters invalid information there will be a error message. Then the user will be asked to insert new values until the values are correct.

![Welcome text](docs/dog-walk-figlet.png)
![Welcome text](docs/enter-number.png)

- Updating worksheet

When user has enterd number of walks the information will be stored inside a worksheet called walks. By default the user will be informed of the daily revenue. The daily revenue will be stored in worksheet called prices. From this worksheet the user will be abel to extrect information of the total price for each dog.

![Update worksheet](docs/calculate-revenue.png)

- Exit program

When the user is ready to leave the program, he/she enters exit in the input. The program will then clear the terminal automatically after 3 second.

![Exit program](docs/calculate-exit.png)
- Color terminal

To make the program user friendly there is a color function that will randomly change the color of the text in the terminal. This is to make the program funnier to use.

### Future Features
- This app should in the future have the abillity to add a new dog to the program.
- There will be a delete function for the user to delete price for each dog when the price has been paid.
*** 
## Data Model
## Testing
### Following tests were carried out:
- User inputs will be handled, if input value is incorrect this    
  will be handled with information of error.
- Walks worksheet updates with the right number of walks
- Each dog name collects correct value from price 
- Daily revanue calculates correctly and stores in price worksheet
- Exit function will close the program

### Bugs
 - Clear()

    When the clear() is carried out, the whole terminal is not cleared out. This is thought to have to do with the termina size. To fix this bug I could place several clear() so the terminal never gets completly filled.
    Satus: Under investigation.

- Clear price columns

    There is a bug in the program that results in error message. This will occure when user clears price worksheet. The column clears as it should, but when the user wants to get the total revenue the program errors. This bug is belived to have to do with the cleared columns. When the function who calculates prices runs it seems to read the empty cell values as strings. Which are not allowed inside the calculate function.
    Status: Under investigation.

### Solved Bugs
- Problem with deployment to Heroku.

    When trying to deploy project  
    error message occured. This was because the import of gspread was never installed in the terminal.
    Status: Fixed.

### Validator Testing
- PEP8 https://pep8ci.herokuapp.com/
  - Validation showed minor errors of whitespces. Theese errors were corrected. No errors left in program.
*** 
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
To deploy project.

- Create a Heroku account.
- Log in to Heroku account.
- In the dashbord choose "Create new app". It's located in the 
  middel of the dashboard.
- Give the new app a name and choose what region you are from. 
- When information is enterd, find the tabs to Overview, Resources, Deploy, Metrics, Activity, Access and Settings. This should be in the upper right of the site. Click "Settings" tab.
- Find the Config Vars section and click the "Reveal Config Vars".
Enter information if there is hidden information in Github  repository. In this project a creds.json file was enterd. If you don't have any hidden information in Github, step over the two following sections.
- Inside Create config vars, enter KEYS and VALUE. Inside KEYS enter CREDS and copy and paste information from creds.json file, into VALUE. Click the "Add" button. 
- Add a new KEY with PORT and VALUE 8000. Click "Add" button.
- Scroll down to Buildpacks section. Click "Add buildpack". 
- Choose buildpack Python and "Save changes". Add another buldpack with nodjs. Save changes. It is importent that the buildpacks are added in the correct order. Drag and drop buildpacks if they are in the wrong order.
- When buildpacks are in order. Locate the "Deploy" tab. It's found on the leftside of "Settings" tab.
- In the Deployment method section, choose GitHub to connect repository. Confirm request to connect GitHub.
-Search for repo-name. This is the name of repository. Click "Search". 
-Click "Connect" to link Heroku app to GitHub repository.
-Scroll down to Automatic deploy section and Manual deploy section.
-Choose how project should be deployed. If Enable Automatic Deploys, Heroku rebuilds app every time new changes are pushed.
- If Manual deploy is choosen the current state of the project will be deployed. For this alternative click "Deploy Branch".
- When project is deployed there will be four green circles with checkmarks inside. There should be a message "Yor app was successfully deployed.". Click the "View" button to se deployed project. If steps are followed there should be a mock terminal with project inside of it. Program starts automaticly. 

***
## Credits

### Code institute
- Tutoring sessions with Code Institute.
- My fantastic mentor Brian O'Hare.
- Love Sandwiches project

### ChatGPT
ChatGPT was used to explain python language. ChatGPT helped with explaining while loop, functions and try-except statements. 

### W3schools 
Was used to find information about Python language.

### gspred
Was used to find information on how to use gspread and access information in worksheet.

### Github user gStarhigh
To create this README I was inspired by the exellent README from gStarhighs project project 3- Python. A budget app.

### Youtube tutorial
Learn Python Functions - Quick Python Project For Beginners by Python Simplified.
