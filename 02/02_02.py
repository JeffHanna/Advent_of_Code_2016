# -*- coding: utf-8 -*- 
'''
--- Part Two ---
You finally arrive at the bathroom (it's a several minute walk from the lobby so
visitors can behold the many fancy conference rooms and water coolers on this 
floor) and go to punch in the code. Much to your bladder's dismay, the keypad is 
not at all like you imagined it. Instead, you are confronted with the result of 
hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same 
instructions as above, the outcome is very different:
- You start at "5" and don't move at all (up and left are both edges), ending 
  at 5.
- Continuing from "5", you move right twice and down three times (through "6", 
  "7", "B", "D", "D"), ending at D.
- Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), 
  ending at B.
- Finally, after five more moves, you end at 3.

So, given the actual keypad layout, the code would be 5DB3.
Using the same instructions in your puzzle input, what is the correct 
bathroom code?

PERSONAL NOTES:
* So now it is a 5 x 5 grid with slightly less than half of the 
  coordinates unused.
  ( 0, 4 ), ( 1, 4 ), ( 2, 4 ), ( 3, 4 ), ( 4, 4 )	-> ..1..
  ( 0, 3 ), ( 1, 3 ), ( 2, 3 ), ( 3, 3 ), ( 4, 3 )	-> .234.
  ( 0, 2 ), ( 1, 2 ), ( 2, 2 ), ( 3, 2 ), ( 4, 2 )	->	56789
  ( 0, 1 ), ( 1, 1 ), ( 2, 1 ), ( 3, 1 ), ( 4, 1 )	-> .ABC.
  ( 0, 0 ), ( 1, 0 ), ( 2, 0 ), ( 3, 0 ), ( 4, 0 )	->	..D..
* Other than refactoring KEYPAD_MAP to account for the new coordinates the
  code from 02 01 should handle this.
'''

import os

puzzle_input_filepath = os.path.abspath( os.path.join( os.getcwd( ), 
																		'02_puzzle_input.txt' ) )

with open( puzzle_input_filepath ) as file:
	input = file.read( )
	PUZZLE_INPUT = input.split( '\n' )


KEYPAD_MAP = { ( 2, 4 ) : '1',
				   ( 1, 3 ) : '2',
					( 2, 3 ) : '3',
					( 3, 3 ) : '4',
					( 0, 2 ) : '5',
					( 1, 2 ) : '6',
					( 2, 2 ) : '7',
					( 3, 2 ) : '8', 
					( 4, 2 ) : '9', 
					( 1, 1 ) : 'A',
					( 2, 1 ) : 'B',
					( 3, 1 ) : 'C', 
					( 2, 0 ) : 'D', 
				 }

DIRECTION_MAP = { 'U' : ( 0, 1 ),
						'D' : ( 0, -1 ),
						'L' : ( -1, 0 ),
						'R' : ( 1, 0 ),
					 }


def find_code( lines, starting_pos ):
	code = ''
	pos = starting_pos

	for line in lines:
		for l in line:
			direction_coords = DIRECTION_MAP.get( l )
			new_pos = tuple( map( sum, zip( pos, direction_coords ) ) )
			if new_pos in KEYPAD_MAP.keys( ):
				pos = new_pos
			
		digit = KEYPAD_MAP.get( pos )
		code += digit

	return code			  



if __name__ == '__main__':
	 code = find_code( PUZZLE_INPUT, ( 1, 1 ) )
	 print( code )