''' Creates CSV file of points centered around Indianapolis using
the normal distribution method. Rounded to four decimal places
because three creates noticeable bands within points. Imported
into ArcGIS using 'NAD 1983 HARN'. '''

from CreatePoint import CreatePoint
import csv

number_of_points = 300000

with open('point_list.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	csvwriter.writerow(['id', 'east', 'north'])
	for each in range(0, number_of_points):
		new_point = CreatePoint(39.964, 39.654, -85.851, -86.473)
		new_point.calculate()
		new_point.generate_point_normal_dist()
		csvwriter.writerow([each, round(new_point.new_easting, 4), round(new_point.new_northing, 4)])