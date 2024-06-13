# many_to_many.py

from typing import List, Union

class Band:
    def __init__(self, name: str, hometown: str):
        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value: str):
        raise AttributeError("Hometown cannot be changed")

    def concerts(self) -> List['Concert']:
        return self._concerts

    def venues(self) -> List['Venue']:
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue: 'Venue', date: str) -> 'Concert':
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self) -> List[str]:
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self._concerts
        ]


class Concert:
    all = []

    def __init__(self, date: str, band: 'Band', venue: 'Venue'):
        self.date = date
        self.band = band
        self.venue = venue
        self.__class__.all.append(self)

    @classmethod
    def get_all_concerts(cls) -> List['Concert']:
        return cls.all

    def hometown_show(self) -> bool:
        return self.band.hometown == self.venue.city

    def introduction(self) -> str:
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name: str, city: str):
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set(concert.band for concert in self._concerts))

    def add_concert(self, concert: 'Concert'):
        self._concerts.append(concert)

    # def concert_on(self, date: str):
    #     for concert in self._concerts:
    #         if concert.date == date:
    #            
