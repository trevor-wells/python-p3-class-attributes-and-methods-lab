class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.add_to_genres(self)
        Song.add_to_artists(self)

    @classmethod
    def add_to_genres(cls, song):
        if song.genre not in cls.genres:
            cls.genres.append(song.genre)
        cls.add_to_genre_count(song)

    @classmethod
    def add_to_artists(cls, song):
        if song.artist not in cls.artists:
            cls.artists.append(song.artist)
        cls.add_to_artist_count(song)

    @classmethod
    def add_to_genre_count(cls, song):
        if 
        cls.genre_count[song.genre] += 1
        

    @classmethod
    def add_to_artist_count(cls, song):
        cls.artist_count[song.artist] += 1
        
