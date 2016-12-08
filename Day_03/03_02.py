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

valid_triangle_count = 0

def _verify_triangle( triangle ):
	'''
	'''
	
	if triangle[ 0 ] + triangle[ 1 ] > triangle[ 2 ] and \
		triangle[ 1 ] + triangle[ 2 ] > triangle[ 0 ] and \
		triangle[ 2 ] + triangle[ 0 ] > triangle[ 1 ]:
		global valid_triangle_count
		valid_triangle_count += 1


def process_input( ):
	'''
	'''

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'03_puzzle_input.txt' ) )
	
	input = [ ]
	with open( puzzle_input_filepath ) as file:
		for line in file:
			vals = line.lstrip( ).rstrip( ).split( ' ' )
			vals = [ int( x ) for x in vals if x ]
			input.append( vals )

	triangle = [ ]
	for column in range( 3 ): # Going to iterate over temp_lines 3 times.
		for val in input:
			triangle.append( val[ column ])
			if len( triangle ) == 3:
				_verify_triangle( triangle )
				triangle = [ ]	 

										
		
if __name__ == '__main__':
	process_input( )
	print( 'There are {0} valid triangles in the list.'.format( valid_triangle_count ) )