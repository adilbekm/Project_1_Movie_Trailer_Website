Author:  Adilbek Madaminov
Date:    2015-02-27
Summary: Submission for Project 1 - Movie Trailer Website

PROJECT OVERVIEW

A server-side Python code to store a list of my favorite movies, 
including box art imagery and a movie trailer URL. The data is 
served as a web page allowing visitors to review the movies and 
watch the trailers.

HOW TO RUN THE APPLICATION

To execute the application, install Python 2.7.9 or greater (you 
can download Python here: https://www.python.org/downloads/).
From Python, run 'my_movies.py' and it will generate 
'my_movie.html' file and open it in the default browser.

The generated HTML page will have show "Fresh Tomatoes Movies 
Trailer" at the top and list 4 movies, each with a poster image, 
title, and a short description. To make changes, continue reading
about project files and what each of them does.

PROJECT FILES

File 'media.py' contains the definition of Movie class used to 
initialize and store movies of my choice. The class has four 
attributes: title, storyline, poster_url, and trailer_url.

File 'fresh_tomatoes.py' contains code for creating an html 
file to render the movies initialized in file 'my_movies.py'
with proper formatting and styling. This file has been provided
by Udacity.

File 'my_movies.py' initializes Movie objects with the required
attributes, stores the objects in a list variable, and calls 
a function from 'fresh_tomatoes.py' with that variable to create 
and open in a browser an html page properly formatted and styled.
