class Album:
    def __init__(self, title, genre, artist, id=None):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.id = id

    def __repr__(self):
        return f"{self.artist.name} - {self.title} [{self.genre}]"