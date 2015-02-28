# Module 'fresh_tomatoes' has been supplied by Udacity,
# and module 'media' was created by me (Adilbek).
from fresh_tomatoes import open_movies_page
from media import Movie

# Initializing 4 movies, each with attibutes title,
# storyline, poster_url, trailer_url.

avatar = Movie(
    "Avatar",
    "A marine on an alien planet.",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

imitation_game = Movie(
    "Imitation Game",
    "Alan Turing cracks Enigma.",
    "http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster."
    "jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM"
    )

frozen = Movie(
    "Frozen",
    "Children's animation.",
    "http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_"
    "poster.jpg",
    "https://www.youtube.com/watch?v=TbQm5doF_Uc"
    )

robocop = Movie(
    "Robocop",
    "A man is merged with a machine.",
    "http://upload.wikimedia.org/wikipedia/en/b/b1/Robocop_poster.jpg",
    "https://www.youtube.com/watch?v=jBeSfnIT_Bw"
    )

# Placing the above created Movie objects inside a list.
movies = [robocop, imitation_game, frozen, avatar]

# Passing the 'movies' list to a function from fresh_tomatoes.
open_movies_page(movies)
