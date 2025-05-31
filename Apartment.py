class Apartment:
    def __init__(self, location, size, bedrooms, rent):
        self.location = location.upper()
        self.size = size
        self.bedrooms = bedrooms
        self.rent = rent

    def __gt__(self, rhs):
        if self.location != rhs.location:
            return self.location > rhs.location

        elif self.size != rhs.size:
            return self.size > rhs.size
        
        elif self.bedrooms != rhs.bedrooms:
            return self.bedrooms > rhs.bedrooms
        
        else:
            return self.rent > rhs.rent
        
    def __lt__(self, rhs):
        if self.location != rhs.location:
            return self.location < rhs.location

        elif self.size != rhs.size:
            return self.size < rhs.size
        
        elif self.bedrooms != rhs.bedrooms:
            return self.bedrooms < rhs.bedrooms
        
        else:
            return self.rent < rhs.rent
        
    def __eq__(self, rhs):
        return self.location == rhs.location and self.size == rhs.size and self.bedrooms == rhs.bedrooms and self.rent == rhs.rent
    
    def __str__(self):
        return f"Location: {self.location}, Size: {self.size} sqft, Bedrooms: {self.bedrooms}, Rent: ${self.rent}"
