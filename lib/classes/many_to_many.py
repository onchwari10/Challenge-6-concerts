class Band:
    def _init_(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []

    def concerts(self):
        return self._concerts

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        return concert

    def venues(self):
        return [concert.venue for concert in self._concerts]

    def _repr_(self):
        return f"Band(name='{self.name}', hometown='{self.hometown}')"


class Concert:
    def _init_(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def _repr_(self):
        return f"Concert(date='{self.date}', band={self.band}, venue={self.venue})"


class Venue:
    def _init_(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    def concerts(self):
        return self._concerts

    def bands(self):
        return [concert.band for concert in self._concerts]

    def _repr_(self):
        return f"Venue(name='{self.name}', city='{self.city}')"