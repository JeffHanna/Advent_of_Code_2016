# -*- coding: utf-8 -*- 
'''
--- Part Two ---
Now that you've helpfully marked up their design documents, it occurs to you 
that triangles are specified in groups of three vertically. Each set of three 
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds 
digit would be part of the same triangle:
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed 
triangles are possible?

PERSONAL NOTES:
* The verification code is still valid. The puzzle here is massaging the input 
  data by reading down each column and grouping each set of 3 items together.
'''

import os


def process_input( ):
	'''
	'''

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'03_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		input = file.readlines( )

	temp_lines = [ ]
	for line in input:
		vals = line.lstrip( ).rstrip( ).split( '  ' )
		vals = [ int( x ) for x in vals if x ]
		temp_lines.append( vals )

	triangles = [ ]
	current_triangle = [ ]
	for column in range( 3 ): # Going to iterate over temp_lines 3 times.
		for val in temp_lines:
			current_triangle.append( val[ column ])
			if len( current_triangle ) == 3:
				triangles.append( current_triangle )
				current_triangle = [ ]	 

	return triangles


def verify_triangles( triangles ):
	'''
	'''

	valid_triangle_count = 0
	
	for t in triangles:
		if t[ 0 ] + t[ 1 ] > t[ 2 ] and \
			t[ 1 ] + t[ 2 ] > t[ 0 ] and \
			t[ 2 ] + t[ 0 ] > t[ 1 ]:
				valid_triangle_count += 1

	return valid_triangle_count
										


if __name__ == '__main__':
	triangles = process_input( )
	number_of_triangles = verify_triangles( triangles )
	print( 'There are {0} valid triangles in the list.'.format( number_of_triangles ) )