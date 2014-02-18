import random

class CreatePoint(object):
	''' Class will digest a bounding box specified by four
	numbers and create a point within it. Must instantiate
	object, call calculate and generate_point methods
	then use new_northing and new_easting attributes '''
	def __init__(self, north, south, east, west):
		self.north = north
		self.south = south
		self.east = east
		self.west = west
	
	def calculate(self):
		''' Calculates the center of the bounding box and
		half the height and length '''
		self.center_northing = (self.north + self.south)/2.0
		self.center_easting = (self.east + self.west)/2.0
		
		self.northing_range = self.north - self.center_northing
		self.easting_range = self.east - self.center_easting
		
	def generate_point(self):
		''' Generates a point with even distribution across
		the given bounding box '''
		self.new_northing = self.northing_range * (random.random() - 0.5) * 2 + self.center_northing
		self.new_easting = self.easting_range * (random.random() - 0.5) * 2 + self.center_easting
		
	def generate_point_normal_dist(self):
		''' Generates a point using a normal distribution
		with mean = 0 and standard deviation = 0.5 '''
		self.new_northing = self.northing_range * (random.gauss(0, 0.5)) + self.center_northing
		self.new_easting = self.easting_range * (random.gauss(0, 0.5)) + self.center_easting