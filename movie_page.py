import media
import fresh_tomatoes

# Generate the movies' detail information.
wonder_woman = media.Movie("Wonder Woman",
                           "Princess of the Amazons leaves home to"
                           " fight a war.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "The Guardians fight to keep "
                                      " their newfound family together.",
                                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                      "https://www.youtube.com/watch?v=2cv2ueYnKjg")

cafe_society = media.Movie("Café Society",
                           "In the 1930s, a Bronx native moves to"
                           " Hollywood and falls in love with a"
                           " young woman who is seeing a married man.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNjk1NjY4NjE5N15BMl5BanBnXkFtZTgwMTU0NDg0OTE@._V1_SY1000_CR0,0,667,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=Rl4X6pFfmTI")

lion = media.Movie("Lion",
                   "A five-year-old Indian boy gets lost on the"
                   " streets of Calcutta. 25 years later, he sets"
                   " out to find his lost family.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA3NjkzNjg2MF5BMl5BanBnXkFtZTgwMDkyMzgzMDI@._V1_SY1000_CR0,0,681,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo")

passengers = media.Movie("Passengers",
                         "A spacecraft traveling to a distant colony "
                         "planet and transporting thousands of people "
                         "has a malfunction in its sleep chambers.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4MjU3MDIzOF5BMl5BanBnXkFtZTgwMjM2MzY2MDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

logan = media.Movie("Logan",
                    "In the near future, a weary Logan cares for an"
                    " ailing Professor X, somewhere on the Mexican"
                    " border. However, Logan's attempts to hide from" 
                    " the world, and his legacy, are upended when a"
                    " young mutant arrives, pursued by dark forces.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwODQwNTg4OV5BMl5BanBnXkFtZTgwMTk4MTAzMjI@._V1_.jpg",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

# Create the movies' list.
movies = [wonder_woman, guardians_of_the_galaxy, cafe_society,
          lion, passengers, logan]

# Create the movies' html and open it.
fresh_tomatoes.open_movies_page(movies)
