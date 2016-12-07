# -*- coding: utf-8 -*- 
'''
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
'''

import os

puzzle_input_filepath = os.path.abspath( os.path.join( os.getcwd( ), 
																		 '03_puzzle_input.txt' ) )
PUZZLE_INPUT = [ ]
with open( puzzle_input_filepath ) as file:
	input = file.readlines( )

for line in input:
	vals = line.lstrip( ).rstrip( ).split( '  ' )
	vals = [ int( x ) for x in vals if x ]
	PUZZLE_INPUT.append( vals )


def verify_triangles( triangles ):
	valid_triangle_count = 0
	
	for t in triangles:
		if t[ 0 ] + t[ 1 ] > t[ 2 ] and \
			t[ 1 ] + t[ 2 ] > t[ 0 ] and \
			t[ 2 ] + t[ 0 ] > t[ 1 ]:
				valid_triangle_count += 1

	return valid_triangle_count
										


if __name__ == '__main__':
	number_of_triangles = verify_triangles( PUZZLE_INPUT )
	print( number_of_triangles )