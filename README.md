# Hangman
[View The Deployed Site Here](https://hangman-gamer-fa003c400c0e.herokuapp.com/)

## About
The concept of this application was to create an engaging game of hangman for the end-user using Python. 
The game will display the instructions depending on the level selected in the game. Easy mode for 3-letter words, medium mode for 5-letter words, and hard mode for 7-letter words.  
I opted to create the Python code using the programming paradigm, object-oriented programming, or O.O.P.


---

## User stories:
1. As a site user, I would like the site in English so it is understandable to me

1. As a site user, I would like to play a game for healthy brain stimulation 

1. As a site user, I am open-minded and willing to try new games to help my mental health

1. As a site user, I am interested in games as I enjoy the competitiveness 

1. As a site user, I would like the information to be clear so I have a better understanding of what the game does

1. As a site user, I would like to know the game rules, so it makes the experience more fun

1. As a site user, I would like the option of replaying the game once it is finished

### Site Owner:

1. As a site owner, I would like the site to display all the necessary information for site users to understand

1. As a site owner, I would like the game to be intuitive for game users

1. As a site owner, I would like game rules/instructions to be displayed for site users to know how the game is played

--
## How To Play

- The first screen display the various game levels, Easy, Medium & Hard.
    - Easy mode is for guessing 3 letter words in 7 attempts.
    - Medium Mode is for guessing 5 letter words in 7 attempts.
    - Hard mode is for guessing 7 letter words in 7 attempts. 
- The user then selects which level the wish to play by type eitherr, e, m, or h.
    - e = Easy
    - m = Medium
    - h = Hard
- Once the user has selcted their game level they wish to play the instructions are displayed for that level.
- Also displayed is a welcome message, the gallows, the correct number of underscores ( _ )  for that level to dictate the empty word, a prompt asking the user to guess a letter, and an input for the user to enter a letter of their choice.
- Once the user guesses a correct letter & enters it, a congratulations message is displayed. 
- If the user enters a number, more than one letter, or a special character, an error message is displayed.
- If the user guesses the correct word, a congratulations message is displayed.
- If the user does not guess the correct word a warning message is displayed. 
- At the end of the game the user can decided if they wish to replay the game or not. 

## Wire Frames

Opening screen will show a tabel that will outline the levels, easy, medium, hard. For each level the user must guess a 3, 5, 7 letter word in 7 attempts.

![Wireframe One](./documentation/wire_one.png)

The game play screen will show a gallows and have the game instructions depending on the level selected by the user.

![Wireframe Two](./documentation/wire_two.png)

Once the user has completed the game, they will be asked if they wish to play again

![Wireframe Three](./documentation/wire_three.png)

## Features

1. Opening Screen

![Main Screen](./documentation/main_screen.png)

2. Playing ~The Games

![Game Play](./documentation/game_play.png)

3. Errors, Warnings, & Text Dispaly

- Entering a Number:

![Entering a Number](./documentation/wrong_one.png)

- Entering a Special Charater:

![Entering a Special Charater](./documentation/wrong_two.png)

- Guessing the Wrong Letter:

![Wrong Letter](./documentation/wrong_letter.png)

- Guessing the Correct Letter:

![Right Letter](./documentation/correct_letter.png)

 4. Winning or Lossing the Game

- Losing the Game:

![Lost Game](./documentation/lost_game.png)

- Winning the Game:

![Game Won](./documentation/game_win.png)

5. Play Again

![Play Again](./documentation/play_again.png)

---

## Technologies used

- ### Languages:

    + [Python](https://developer.mozilla.org/en-US/docs/Glossary/Python): This was used for producing the game itself. 

- ### Programming Paradigm

    + [Object Orientated Programming](https://codeinstitute.net/ie/blog/object-oriented-programming/): This was the paradigm I chose to complete this project. It involves classes and methods that are accessed to complete tasks of a desired outcome. 

- ### Other tools:

    + [GitHub](https://github.com/): This was used to host the source code of the website
    + [GitHub Pages](https://github.com/Ajfriel86/PilatesParadise/settings/pages): This was used to publish the files that were pushed to the repository
    + [VSCode](https://code.visualstudio.com/): This was the IDE used to develop the website
    + [Heroku](https://dashboard.heroku.com/apps): This was used to deply the application
    + [Miro](https://miro.com/) : This was used to create the flowchart

- ### Packages

    + [OS](https://docs.python.org/3/library/os.html ) : This module is built in and provides a portable way of using operating system dependent functionality. This was used to create the clear_screen() function.
    + [Random](https://docs.python.org/3/library/random.html) : This module is built in and implements pseudo-random number generators for various distributions. Specifically for this project, it was used to selected a random word from words.py, depending on the level selected by the user.
    + [Time](https://docs.python.org/3/library/time.html) : This module is built in and provides various time-related functions. The sleep function of Time was used to delay the clear_screen() function so the errors messages where dispalyed long enough for the user to read. 
    + [Colorama](https://pypi.org/project/colorama/) : This module is a third party module and was used to colour the text in the terminal window. 
---


### Flow Chart

![Flowchart](./documentation/flowchart.png)


## Testing

### Bugs

Throughout compiling the projects code I ran tests to check all of the cose was meeting pep8 standards. Using a built-in pepe8 linter in VS I ran into a mountain of errors at the start. Most of which where using single backslashes and trailing whitespace. Other's "string statement has no effect." Which was related to my docstrings being used improperly. These were easy fixes.

![Python Linter](./documentation/pylint.png)

While testing the game I ran into a bug. Thius was at the end of the game when the user is asked if they will playing or not. 
When entering anything other than the required fileds (y/n), an error was thrown. This was in relation to the .strip() function. 
I changed the error handling from an if/else statement to an exception and removed the .strip() funstion.

![Bug](./documentation/bug_one.png)

After correcting the above error, I ran into another issue. The final screen asking the user if they wish to play again was not using the clear_screen() function. The orignal error was addressed but the scrolling text took away from the resat of the game using clear_scrren() This was then added and it solved the issue.

![Clear Screen](./documentation/clearscreen_error.png)

While using OOP standard, I seperated the various parts of the code in to other documents. The words that were picked at random, the hangman figure to be diaplyed and the text box displayed at the start of the game that depicts the levels; these were all put into their own .py file.
But, while trying to import functions from other .py documents I ran into some issues. It seems having a documents named with an underscorelike so, display_hangman.py, were causing difficuties while trying to import them

![Import Error](./documentation/import_error.png)

This was corrected by removing the underscore and ernaming the file:

![Import Fix](./documentation/import_fix.png)

When creating the hangman icon's to be displayed I ran into an error using the backslashes for the arms and legs. A work around for this was to add a double backslash. This then removed the error and also only displayed one backslash. This error could have been due to the fact that a single backslash is used as an escape sequence. So a double backslash must be used to display a backslash.

![BackSlash](./documentation/pylint2.png)

Testing the game on medium level I stumbled into this error. 

- TypeError: can only concatenate str (not "NoneType") to str

![Medium Error](./documentation/medium_error.png)

This was resolved by adding the following piece of code:

![None Error](./documentation/none_error.png)




### Validation
#### Python:

To validate my code I used the Code Institute's PEP8 Python Linter: [CI Python Linter](https://pep8ci.herokuapp.com/)

run.py
- Trailing Whitespace found on run.py file
![Run](./documentation/run_whitespace.png)

- Run.py file with no errors:
![Run No Errors](./documentation/run_no-errors.png)

- All other files returned no errors:

![All Clear](./documentation/all_clear.png)

## Deployment

This website was constructed in VS Code and deployed on [Heroku](https://www.heroku.com/)

### Deployment to Heroku
#### Activating your Heroku Student Pack

- Navigate to https://www.heroku.com/github-students
- Click “Get the student offer”
- Login with Heroku if necessary
- Click “Verify with GitHub”
- Click “Authorize heroku”
- In order to receive the Heroku credits, payment details are required.
- In the new tab, click “Add credit card”.
- Enter your payment details as requested and then head back to the Heroku sign up process
- Enter your details, ensuring to put “Code Institute” as your School name, heed the warning and then click “Send”
- Read Heroku’s terms and click “Agree” to continue
- A thank you message will be shown, indicating that it can take up to 24 hours for the request to be processed

#### Adding an App to Heroku

- On the main page of your Heroku account, select the "New" tab
- Then select "Create New App"
- Add an "App-Name"
- On the newly available page, selcet your deplyment method as GitHub and connect to this
- Enter in the REpo of your project you wish to host on Herko
- Once it is connected, you can then choose "Automatic Deploys" This will automatucally update your application on every push
- The app is now hosted on Heroku [here](https://hangman-gamer-fa003c400c0e.herokuapp.com/)

### Deployment to Git Hub Pages

- Log into GitHub
- Go to the list of repositories on the left-hand side of the screen
- Click on the repository - [Hangman](https://github.com/Ajfriel86/HangManGame)
- Choose the settings tab from the menu items across the top of the page; it is the 9th tab on the menu items list.
- Under 'Code and automation,' the last choice on the list is 'Pages'
- In the 'Source' section, choose 'Deploy from a branch'
- In the 'Branch' section, choose the branch you wish to deploy
- Select, or click, the 'Save' button
- A link to the deployed website is then displayed at the top of the page

### How To Clone a GitHub Repository

- On GitHub.com, navigate to the main page of the repository
- Above the list of files, click <>  Code
- Copy the URL for the repository
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory
- Type git clone, and then paste the URL you copied earlier
- Press Enter to create your local clone

These steps can where found in the help documentation for GitHub here:
- [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

---

## Credits

- [CPPSecrets](https://cppsecrets.com/users/5617971101051071011161151049711410997484852494964103109971051084699111109/Hangman-Game-using-Python.php) : This site was the inspiration for creating this hangman game
- [How to build HANGMAN with Python in 10 MINUTES](https://www.youtube.com/watch?v=m4nEnsavl6w) : This was used to help with understanding the game in greatrer detail while using Python to create the game
- [How To Print Colored Text in Python (Colorama Tutorial)](https://www.youtube.com/watch?v=u51Zjlnui4Y) : This was used to help understand the use of colorama for changing the colour of the text on the terminal screen
- [Corey Schafer ](https://www.youtube.com/@coreyms) : Corey's YT channel was used to explore in greater detail the Python language and the use of OOP for this language
- [Simple-Terminal-Window](https://pypi.org/project/simple-term-menu/) : This creates simple menus for interactive command line programs
- [Random](https://docs.python.org/3/library/random.html) : This was used to help select a random word from the word dictionary file
- [Gitnux](https://blog.gitnux.com/code/python-clear-console/) : This was used to help clear the terminal window
- [Iuliia Konovalova](https://github.com/IuliiaKonovalova) : I would like to give credit to my mentor for her guidance and inspiration while completing this project. Iuliia helped to point me in the direction that I needed to complete this project

