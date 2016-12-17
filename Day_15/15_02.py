# -*- coding: utf-8 -*-
"""
--- Part Two ---
After getting the first capsule (it contained a star! what great fortune!), the 
machine detects your success and begins to rearrange itself.

When it's done, the disks are back in their original configuration as if it were 
time=0 again, but a new disc with 11 positions and starting at position 0 has 
appeared exactly one second below the previously-bottom disc.

With this new disc, and counting again starting from time=0 with the 
configuration in your puzzle input, what is the first time you can press the 
button to get another capsule?

PERSONAL NOTES:
* Insert the new disk before the two lists are returned in parse_input( )
"""

import os


def parse_input( ):
	"""
	"""

	disks = [ ]
	positions = [ ]
	
	puzzle_input_filepath = os.path.abspath( os.path.join( os.getcwd( ), 
																		 '15_puzzle_input.txt' ) )
	with open( puzzle_input_filepath ) as file:
		lines = file.read( ).strip( ).split( '\n' )
	
	for l in lines:
		data = l.rstrip( '.' ).split( ' ' )
		disks.append( int( data[ 3 ] ) )
		positions.append( int( data[ -1 ] ) )

	disks.append( 11 )
	positions.append( 0 )
	return ( disks, positions )


def calculate_solution_positions( disks, positions ):
	"""
	"""

	solution = [ ]
	for x in range( len( disks ) ):
		solution.append( ( disks[ x ] - ( x + 1 ) ) % disks[ x ] )

	return solution


def increment( current_pos, total_positions ):
	"""
	"""

	new_pos = current_pos + 1
	if new_pos % total_positions == 0:
		return 0
	return new_pos


def find_first_time_to_win( ):
	"""	
	"""

	disks, positions = parse_input( )
	solution = calculate_solution_positions( disks, positions )

	i = 1
	while i:
		for x in range( len( disks ) ):
			positions[ x ] = increment( positions[ x ], disks[ x ] )

		if positions == solution:
			return i

		i += 1



if __name__ == '__main__':
	time = find_first_time_to_win( )
	print( 'The first time the capsule will fall through is {0}'.format( time ) )