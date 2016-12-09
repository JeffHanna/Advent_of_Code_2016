# -*- coding: utf-8 -*- 
"""
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
"""

import os


valid_triangle_count = 0

def _process_input( ):
	"""
	The input data, consisting of 3 space delimeted values per line is read
	columnwise. Every three rows in a column is converted to a list of integers
	representing the lengths of the sides of a triangle. Each list of sides is
	added to a single list [ [ a, b, c ], [ a, b, c ], ... ] to be returned.

	**Arguments:**

		None

	**Keyword Arguments:**

		None

	**Returns:**

		`list` A list of lists of lenths of sides of a triangle.
	"""

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'03_puzzle_input.txt' ) )
	
	input = [ ]
	with open( puzzle_input_filepath ) as file:
		for line in file:
			vals = line.lstrip( ).rstrip( ).split( ' ' )
			vals = [ int( x ) for x in vals if x ]
			input.append( vals )

	triangles = [ ]
	triangle = [ ]
	for column in range( 3 ): # Going to iterate over temp_lines 3 times.
		for val in input:
			triangle.append( val[ column ])
			if len( triangle ) == 3:
				triangles.append( triangle )
				triangle = [ ]	 

	return triangles


def verify_triangles( ):
	"""
	Gets a list of triangles from the _process_input( ) function.
	For each triangle in the list each pair of adjacent sides is summed to 
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
	
	for tri in _process_input( ):
		if tri[ 0 ] + tri[ 1 ] > tri[ 2 ] and \
			tri[ 1 ] + tri[ 2 ] > tri[ 0 ] and \
			tri[ 2 ] + tri[ 0 ] > tri[ 1 ]:
				valid_triangle_count += 1

	return valid_triangle_count
										
		
if __name__ == '__main__':
	number_of_triangles = verify_triangles( )
	print( 'There are {0} valid triangles in the list.'.format( number_of_triangles ) )