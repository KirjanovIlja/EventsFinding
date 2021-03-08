class Concert :
    def __init__(self, band, start_date, end_date, city, country, place, genre, image):
        self.band = band
        self.start_date = start_date 
        self.end_date = end_date 
        self.city = city
        self.place = place
        self.genre = genre 
        self.image= image
        self.country = country

    def info(self):
        return self.band, self.start_date, self.end_date, self.city, self.place, self.genre, self.image, self.country
    
    def toObj(self):
        return {
            "band": self.band,
            "genre":self.genre,
            "start date": self.start_date,
            "end date": self.end_date,
            "city":self.city,
            "place":self.place,
            "country": self.country,
            "image":self.image
        }