# This file contains Movie class definition.
# Last updated 2015-02-26.

# Module 'webbrowser' is needed in method 'show_trailer'
# to open() the movie trailer in a browser window.
import webbrowser

# Defining my Movie class.
class Movie(object):
    '''Class to hold my favorite movies.

    Attributes:

    title: A string containing the movie title.
    storyline: A string containing a short description of the movie.
    poster_url: A string with URL for the movie poster image file.
    trailer_url: A string with URL for the official YouTube trailer.
    '''
    def __init__(self, title, storyline, poster_url, trailer_url):
    	'''
    	Initializes Movie class with title, storyline, poster_url, trailer_url.
    	'''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
    def show_trailer(self):
    	'''
    	Launches the movie trailer.
    	'''
        webbrowser.open(self.trailer_youtube.url)
