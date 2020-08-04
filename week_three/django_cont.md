#### Objectives
-   Gain more familiarity with project set-up
-   Reinforce GET vs. POST
-   Breakdown request.POST and accessing form data
-   Displaying user inputted data on HTML, persistent data storage

## GET vs POST
-   How are POST requests sent?
-   Why do we send data through forms?
-   Why is it poor practice to render on a POST request?

## Accessing Form Data
-   HTML form breakdown
    -   What is the purpose of the name attribute? <input>
    -   Why do forms need actions?
    -   Why must we be explicit of method?
-   Retrieving data from the server
    -   What is request.POST?

## Displaying server data on HTML
-   Persistent data storage
    -   What is the biggest difference between context and request.session?
    -   How do we use request.session?
-   Templating languages
    -   What is the syntax when looking at static data with Jinja?
    -   When writing functionality?

## Game of War!

# Create a game where users compete to build the largest armies!

-   When a user send the request for '/', render an HTML page with a form for a user to input their name, favorite color, and a submit button that reads "Start Game" 

-   When a user clicks "start game", send a request for '/game'. Requests for '/game' are handled by an HTML page with a button for "adding soldiers"

-   When user clicks "add soldier", number of soldiers increases by 1

# BONUS FEATURES

-   game.html includes button that allows for "battle". A random number between 0 and double the users soldiers is generated.
    -   If random number is greater than user soldiers, user loses difference in troops
    -   If random number is less than user soldiers, user gains difference in troops

-   Modify game.html to display an icon for each troop in users army

-   Add a button on game.html to "add to leaderboard", where current size of army and user's name is stored and displayed on leaderboard

