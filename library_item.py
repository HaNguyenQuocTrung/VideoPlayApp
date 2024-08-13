class LibraryItem:
    def __init__(self, name, director, rating, type, tempo, mp3_file):
        self.name = name
        self.director = director
        self.rating = rating
        self.type = type
        self.tempo = tempo
        self.mp3_file = mp3_file
        self.play_count = 0

    def info(self):
        return f"{self.name} by {self.director} ({self.type}, {self.tempo}) - {self.rating}"

    def play(self):
        self.play_count += 1

    def reset_play_count(self):
        self.play_count = 0

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
