# band.py
from musician import Musician  # Import Musician if needed for type annotations


class Band:

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        performances = []
        for musician in self.musicians:
            if musician.instruments:
                for instrument in musician.instruments:
                    performances.append(f"{musician.name} is playing: {instrument}")
            else:
                performances.append(f"{musician.name} needs an instrument!")
        return '\n'.join(performances)
