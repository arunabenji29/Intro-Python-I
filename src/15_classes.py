# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon
    
    def get_LatLon(self):
        return [self.lat,self.lon]

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):

    def __init__(self,name,lat,lon):
        super().__init__(lat,lon)
        self.name = name

    def get_LatLon(self):
        latlon = super().get_LatLon()
        print(latlon)
        latlon.append(self.name)
        return latlon


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self,name,difficulty,size,lat,lon):
        super().__init__(name,lat,lon)
        self.difficulty = difficulty
        self.size = size
        
    def get_LatLon(self):
        geo = super().get_LatLon()
        print(geo)
        geo.append(self.difficulty)    
        geo.append(self.size)
        return geo

# c = Geocache('whatever',1,2,3,4)        

# print(c.get_LatLon())

	# def get_LatLon(self):
    #     geo = super().get_LatLon()
    #     print(geo)
    #     geo.append(self.difficulty)
    #     geo.append(self.size)
    #     return geo

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.get_LatLon())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache.get_LatLon())
