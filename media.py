import webbrowser

class Movie():
    """ Defines the structure of a movie on the page """
    def __init__(self,movie_title,art_url,youtube_link):
        self.title = movie_title
        self.poster_image_url = art_url
        self.trailer_youtube_url = youtube_link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
