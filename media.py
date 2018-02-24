# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser


class Movie(object):
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_rating, poster_image,
                 trailer_youtube):
        """
        Initialize the movie instance.
        Arguments:
        movie_title: title of the movie
        movie_rating: IMDb movie rating 
        poster_image: image of the movie poster
        trailer_youtube: youtube trailer of the movie  
        Returns: 
        None
        """
        self.title = movie_title
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Plays the youtube trailer.
        Arguments: None   
        Returns: 
        None 
        """
        webbrowser.open(self.trailer_youtube_url)
