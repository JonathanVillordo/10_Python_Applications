class Purchase:
    def __init__(self, city, zipcode, state, beds, baths, sqft, home_type,
            sale_date, price, latitude, longitude):
        
        
        self.city   = city
        self.zipcode = zipcode
        self.state   = state
        self.beds =  beds
        self.baths = baths
        self.sqft = sqft
        self.home_type = home_type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
    
    @staticmethod
    def create_from_dict( lookup):
        return Purchase(
                lookup['city'],
                lookup['zip'],
                lookup['state'],
                int(lookup['beds']),
                int(lookup['baths']),
                int(lookup['sqft']),
                lookup['type'],
                lookup['sale_date'],
                float(lookup['price']),
                float(lookup['latitude']),
                float(lookup['longitude']))

