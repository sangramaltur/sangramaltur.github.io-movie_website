# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py.

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

dark_knight = media.Movie("The Dark Knight",
                          "IMDb 9/10",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=TQfATDZY5Y4")

two_towers = media.Movie("The Two Towers",
                         "IMDb 8.7/10",
                         "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                         "https://www.youtube.com/watch?v=cvCktPUwkW0")

inception = media.Movie("Inception",
                        "IMDb 8.8/10",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

dunkirk = media.Movie("Dunkirk",
                      "IMDb 8.1/10",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

wall_e = media.Movie("WALL-E",
                     "IMDb 8.14/10",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                     "https://www.youtube.com/watch?v=alIq_wG9FNk")

terminator_2 = media.Movie("Terminator 2",
                           "IMDb 8.5/10",
                           "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
                           "https://www.youtube.com/watch?v=lwSysg9o7wE")


movies = [dark_knight, two_towers, inception, dunkirk, wall_e, terminator_2]
fresh_tomatoes.open_movies_page(movies)
