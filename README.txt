Author:  Adilbek Madaminov
Date:    2015-02-26
Summary: Submission for Project 1 - Movie Trailer Website

PROJECT OVERVIEW

A server-side Python code to store a list of my favorite movies, 
including box art imagery and a movie trailer URL. The data is 
served as a web page allowing visitors to review the movies and 
watch the trailers.

PROJECT DETAILS

File 'media.py' contains the definition of Movie class used to 
initialize and store movies of my choice. The class has four 
attributes: title, storyline, poster_url, and trailer_url;
and a method called 'show_trailer' to launch a trailer in a 
web browser at the URL provided in trailer_url.

File 'fresh_tomatoes.py' contains code for creating an html 
file to render the movies initialized in file 'my_movies.py'
with proper formatting and styling. This file has been provided
by Udacity.

File 'my_movies.py' initializes Movie objects with the required
attributes, stores the objects in a list variable, and calls 
a function from 'fresh_tomatoes.py' with that variable to create 
and open in a browser an html page properly formatted and styled.
