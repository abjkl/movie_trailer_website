import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailor(self):
        webbrowser.open(self.trailer_youtube_url)
