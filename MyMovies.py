import fresh_tomatoes
import media

avatar = media.Movie("Avatar","A marine on an alian planet.","http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
imitation_game = media.Movie("Imitation Game","Alan Turing cracks Enigma.","http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg","https://www.youtube.com/watch?v=S5CjKEFb-sM")
frozen = media.Movie("Frozen","Children's animation.","http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg","https://www.youtube.com/watch?v=TbQm5doF_Uc")
robocop = media.Movie("Robocop","A man is merged with a machine.","http://upload.wikimedia.org/wikipedia/en/b/b1/Robocop_poster.jpg","https://www.youtube.com/watch?v=jBeSfnIT_Bw")

movies = [robocop, imitation_game, frozen, avatar]

fresh_tomatoes.open_movies_page(movies)
