#### Objectives
-   Review timeline; expectations for coming weeks and exam
-   Gain more familiarity with DB design through IMDDB project
-   Reinforce idea of REST through building IMDDB project

## IM(D)DB
-   The Internet Movie (Dojo) Data Base!

-   Our Task:
    -   Build a movie website where users may add their favorite Directors and Movies.

        -   Root Page ('/') prompts user with option to visit Director Page or Movie Page
        -   Directors page ('/directors') displays form to add directors, and table of existing directors
        -   Movies page ('/movies') displays form to add movies, and table of existing movies.

-   Making it RESTful
    -   Modifying our project to allow requests for one movie or one director.

        -   One Director page ('/director/int:id') displays all Director info, including all movies the Director has worked on.
            -   One director page has option for deleting director ('director/delete/int:id')
            -   One director page has the option for editing a director ('director/edit/int:id')
        -   One Movie page ('/movie/int:id') displays all Movie info, including Director
            -   One movie page has option for deleting movie ('movie/delete/int:id')
            -   One movie page has option for editing movie ('movie/edit/int:id')

-   Many-To-Many
    -   Modify your models.py to handle an Actors table.

        -   Actors page ('/actors') displays form to add Actors, and table of existing actors
        -   Modify one movie page to handle adding actors to a movie
        -   Modify one movie page to display all actors in a movie

