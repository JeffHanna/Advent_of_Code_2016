# -*- coding: utf-8 -*- 
"""
2016 Advent of Code puzzle 01-01.

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", 
unfortunately, is as close as you can get - the instructions on the Easter Bunny 
Recruiting Document the Elves intercepted start here, and nobody had time to 
work them out further.

The Document indicates that you should start at the given coordinates (where you 
just landed) and face North. Then, follow the provided sequence: either turn 
left (L) or right (R) 90 degrees, then walk forward the given number of blocks,
ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you 
take a moment and work out the destination. Given that you can only walk on the 
street grid of the city (https://en.wikipedia.org/wiki/Taxicab_geometry ), how
far is the shortest path to the destination?

For example:
Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 
blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

PERSONAL NOTES:
* Assume a 2D grid, +Y is 'North' and +X is 'East'.
* Assume you start at ( 0, 0 ) facing down the +Y axis (aka North).
* At each loop iteration the direction (L or R) will need to be converted to
  a new vector (-X, +X, -Y, or +Y) depending on the current facing. 
"""

import os


def _write_each_step( cur_pos, distance, axis ):
	"""
	Since _get_new_heading is written with 0-2 being Y and 1-3 being X,
	yet the X value being the 0 index of the position tuple this needs
	to be done. Whether it's done  here, in _get_new_heading() or
	by swapping the pos tuple to be ( Y, X ) it is still cumbersome.

	**Arguments:**
	
		:``cur_pos``:	`tuple` The current position of the user as ( X, y )
		:``distance``:	`int` The distance to travel
		:``axis``:		`int` The axis on which to travel.
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		:`tuple` The new location of the user as ( X, Y )
		:`bool`  True If the user is at a previously visited coordinate, 
					otherwise False.
	"""

	axis -= 1
	pos = cur_pos

	inc = 1 if distance >= 0 else -1
	for _i in range( abs( distance ) ):
		if axis == 0:
			pos = ( pos[ 0 ] + inc, pos[ -1 ] )
		else:
			pos = ( pos[ 0 ], pos[ -1 ] + inc )
		
	return pos, False

				 
def _get_distance_to_hq( heading ):
	"""
	Starting at 0, 0 take each new turn and distance from the list _PUZZLE_INPUT.
	Add each new component as if the user is walking on a 2D coordinate grid.
	At the end combine the X and Y values to get a total count of blocks
	from the start the user has walked.

	**Arguments:**
	
		:``heading``:	`int` A value representing the current facing direction.
									0 = N, 1 = E, 2 = S, and 3 = W
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		:`int` The shortest distance, in blocks, to the destination.
	"""

	pos = ( 0, 0 )

	puzzle_input_filepath = os.path.abspath( os.path.join( os.getcwd( ), 
																		 '01_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for vector in file.read( ).split( ', ' ):
			direction = vector[ 0 ]
			heading = _get_new_heading( heading, direction ) 		
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
	"""
	4 possibilities for current_heading, 0 (N), 1 (E), 2 (S), and 3 (W), and 
	2 possibilities for turn_char, 'L' or 'R'. 		

	If turn_char is 'R'  then increase current_heading	by 1, otherwise decrease 
	it by 1.

	**Arguments:**
	
		:``current_heading``:	`int` The current facing direction
		:``direction``:			`str` Either R or L, the direction in which the
												current facing should be turned.
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		:`int` The new facing direction.
	"""

	inc = 1 if direction == 'R' else -1

	new_heading = current_heading + inc
	if new_heading < 0:
		new_heading = 3
	elif new_heading > 3:
		new_heading = 0

	return new_heading

													
																	 
if __name__ == '__main__':
	distance = _get_distance_to_hq( 0 )
	print( "The shortest distance to the Easter Bunny's hideout is {0} blocks.".format( distance ) )