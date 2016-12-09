# -*- coding: utf-8 -*- 
'''
2016 Advent of Code puzzle 01-02.

Then, you notice the instructions continue on the back of the Recruiting 
Document. Easter Bunny HQ is actually at the first location you visit twice.
For example, if your instructions are R8, R4, R4, R8, the first location you 
visit twice is 4 blocks away, due East.
How many blocks away is the first location you visit twice?

PERSONAL NOTES:
* Assume a 2D grid, +Y is 'North' and +X is 'East'.
* Assume you start at ( 0, 0 ) facing down the +Y axis (aka North).
* At each loop iteration the direction (L or R) will need to be converted to
  a new vector (-X, +X, -Y, or +Y) depending on the current facing. 
'''

import os


locations = [ ( 0, 0 ) ]

def _write_each_step( pos, distance, axis ):
	'''
	# since _get_new_heading is written with 0-2 being Y and 1-3 being X,
	# yet the X value being the 0 index of the position tuple this needs
	# to be done. Whether it's done  here, in _get_new_heading() or
	# by swapping the pos tuple to be ( Y, X ) it is still cumbersome.
	axis = axis - 1 
	pos = cur_pos
	'''

	inc = 1 if distance >= 0 else -1
	for _i in range( abs( distance ) ):
		if axis == 0:
			pos = ( pos[ 0 ] + inc, pos[ -1 ] )
		else:
			pos = ( pos[ 0 ], pos[ -1 ] + inc )

		if pos in locations:
			# If the path is being crossed, return that coordinate
			# as that is the answer for Day 1, puzzle 2!
			return pos, True

		locations.append( pos )
		
	return pos, False
				 
				 
def _get_distance_to_hq( heading ):
	'''
	Starting at 0, 0 take each new turn and distance from the list _PUZZLE_INPUT.
	Add each new component as if the user is walking on a 2D coordinate grid.
	At the end combine the X and Y values to get a total count of blocks
	from the start the user has walked.
	'''

	pos = ( 0, 0 )

	puzzle_input_filepath = os.path.abspath( os.path.join( os.getcwd( ), 
																		 '01_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for vector in file.read( ).split( ', ' ):
			turn_char = vector[ 0 ]
			heading = _get_new_heading( heading, turn_char ) 		
			distance = int( vector[ 1: ] )
		
			if heading > 1:
				distance *= -1

			# Don't just capture the end point, write out each step in the journey
			axis = 1 if heading in [ 1, 3 ] else 0
			pos, match = _write_each_step( pos, distance, axis )
			if match:
				break
			
	return abs( pos[ 0 ] ) + abs( pos[ -1 ] )
				 		
				 
def _get_new_heading( current_heading, direction ):
	'''
	4 possibilities for current_heading, 0 (N), 1 (E), 
	2 (S), and 3 (W), and 2 possibilities for turn_char, 
	'L' or 'R'. 		

	If turn_char is 'R'  then increase current_heading
   by 1, otherwise decrease it by 1.
	'''

	inc = 1 if direction == 'R' else -1
	current_heading += inc
	if current_heading < 0:
		current_heading = 3
	elif current_heading > 3:
		current_heading = 0

	return current_heading

													
																	 
if __name__ == '__main__':
	distance = _get_distance_to_hq( 0 )
	print( "The shortest distance to the Easter Bunny's hideout is {0} blocks.".format( distance ) )