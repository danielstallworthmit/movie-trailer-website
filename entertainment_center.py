import fresh_tomatoes
import media

# Instantiate movies using the media.Movie class from media.py
iron_man = media.Movie("Iron Man",
                       "http://ecx.images-amazon.com/images/I/515wjJQt2nL.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

avengers = media.Movie("Avengers",
                       "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=JAUoeqvedMo")

the_matrix = media.Movie("The Matrix",
                         "http://ecx.images-amazon.com/images/I/51EG732BV3L.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

batman_begins = media.Movie("Batman Begins",
                         "http://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                         "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

happy_feet = media.Movie("Happy Feet",
                         "http://upload.wikimedia.org/wikipedia/en/5/5c/Happy_Feet_Poster.jpg",
                         "https://www.youtube.com/watch?v=hFUC5adf8FE")

march_of_the_penguins = media.Movie("March of the Penguins",
                         "http://ia.media-imdb.com/images/M/MV5BMTM1NDc5MDYxMl5BMl5BanBnXkFtZTcwMjMzNDAzMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=L7tWNwhSocE")

three_10_to_yuma = media.Movie("3:10 to Yuma",
                         "http://upload.wikimedia.org/wikipedia/en/2/27/310_to_Yuma_(2007_film).jpg",
                         "https://www.youtube.com/watch?v=ZeroJ1BK6GQ")

gladiator = media.Movie("Gladiator",
                         "http://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                         "https://www.youtube.com/watch?v=IvTT29cavKo")

anchorman = media.Movie("Anchorman",
                         "http://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                         "https://www.youtube.com/watch?v=Ip6GolC7Mk0")

# Create list of movies
movies = [iron_man,
          avengers,
          the_matrix,
          batman_begins,
          happy_feet,
          march_of_the_penguins,
          three_10_to_yuma,
          gladiator,
          anchorman]

# Calls fresh_tomatoes.py and passes the movies list
fresh_tomatoes.open_movies_page(movies) 
