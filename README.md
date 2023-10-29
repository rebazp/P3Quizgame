## Quizgame

Quizgame is a terminal based python game where the player have to answer ten specific questions chosen by me. Each questions have four options but only one is correct. At the end of the game the player will see the score in percentage, the correct answers and aksed to replay the game.

![Live version of my project](assets/images/responsive.jpg)

![Responsive Mockup](assets/images/responsive.jpg)

## How to play

Quizgame is a game that asks questions about movies, books, astronomy, animals and much more. There are ten specific questions where the player will have to pick one answer that is correct. The other three options are wrong and the game will print wrong answer if the player choose wrong answer.

The player can choose to replay the game after answering ten questions and try to get better score.

This game is for entertainment purpose and to see if the player have good memory and know random facts.

## Features

This game have two features. One where the player will choose one out of 4 options for every option that appears. The second feature is where the result will appear, the correct answers and ask the player if he/she want's to play again.

### Existing Features

- __The Game Area__

This is where the player will have to choose one out of 4 options.

![Game](assets/images/game.jpg)

- __The Result Area__

This is where the correct answer and player guesses are displayed. The score is displayed in percentage and the player is asked to play again. The playeer will have to type Yes or No.

![Game](assets/images/game.jpg)

### Features left to implement

- One feature that would make the game more difficult and fun would be to add more questions. But everytime the game starts, the game only choose ten random questions. Next time the game starts it choose ten new questions so that everytime there is new questions to choose from.

- Feature that gives the player the option to show or hide the correct answers.

## Data Model


## Testing

I have manually tested this project by doing:

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Try different options while playing the game to see if the score is correct.
- Finished the game several times to see if the score is correct and option to replay appears.

## Bugs

### Solved bugs

- For a while I could not start the game properly. By making a small change in the new_game code I managed to make it work.

### Remaining bugs

- There is no bugs in the game.

### Validator testing

- PEP8
    - No significant errors were returned from the [CI Python Linter](https://pep8ci.herokuapp.com/)

## Deployment

This project was deployes using the Code Institute's mock terminal for Heroku.
- Steps for deployment
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Python and Node35 in that order
    - Link the Heroku app to the repository
    - Click on Deploy

## Credits

The code that I've used in this project is my own. Code that I've learned from Code Institute Python modules, loop tutorial that I found online and from Youtube channel.

- [Python Loop](https://www.youtube.com/watch?v=yriw5Zh406s&t=199s&ab_channel=BroCode)
- [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s&t=199s&ab_channel=BroCode)

### Content

- The main game area and function comes from [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s&t=199s&ab_channel=BroCode)

## Media

- There is no media in this project.