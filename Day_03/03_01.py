# -*- coding: utf-8 -*- 
"""
--- Day 3: Squares With Three Sides ---
Now that you can think clearly, you move deeper into the labyrinth of hallways 
and office furniture that makes up this part of Easter Bunny HQ. This must be a 
graphic design department; the walls are covered in specifications 
for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 
5 10 25? Some of these aren't triangles. You can't help but mark the 
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining 
side. For example, the "triangle" given above is impossible, because 5 + 10 is 
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

PERSONAL NOTES:
* Find the largest and smallest values. Ensure L + M > S and S + M > L
"""

import os


def verify_triangles( ):
	"""
	Parses the input file to remove leading and trailing spaces and returns on 
	each line. Each line is then converted to 3 integers representing the length 
	of the sides of a triangle. Each pair of adjacent sides is summed to 
	determine if their combined length is greater than the third side. If so
	the triangle is valid and the valid triangle counter is incremented by 1.
	
	**Arguments:**
	
		None
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`int` The number of valid triangles in the input.
	"""

	valid_triangle_count = 0

	puzzle_input_filepath = os.path.abspath( os.path.join( os.getcwd( ), 
																		 '03_puzzle_input.txt' ) )

	PUZZLE_INPUT = [ ]
	with open( puzzle_input_filepath ) as file:
		for line in file:
			vals = line.lstrip( ).rstrip( ).split( '  ' )
			tri = [ int( x ) for x in vals if x ]
			if tri[ 0 ] + tri[ 1 ] > tri[ 2 ] and \
				tri[ 1 ] + tri[ 2 ] > tri[ 0 ] and \
				tri[ 2 ] + tri[ 0 ] > tri[ 1 ]:
					valid_triangle_count += 1

	return valid_triangle_count
										


if __name__ == '__main__':
	number_of_triangles = verify_triangles( )
	print( 'There are {0} valid triangles in the list.'.format( number_of_triangles ) )