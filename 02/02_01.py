# -*- coding: utf-8 -*- 
'''
--- Day 2: Bathroom Security ---
You arrive at Easter Bunny Headquarters under cover of darkness. However, you 
left in such a rush that you forgot to use the bathroom! Fancy office buildings 
like this one usually have keypad locks on their bathrooms, so you search the 
front desk for the code. 

"In order to improve security," the document you find says, "bathroom codes will 
no longer be written down. Instead, please memorize and follow the procedure 
below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by 
starting on the previous button and moving to adjacent buttons on the keypad: 
U moves up, D moves down, L moves left, and R moves right. Each line of 
instructions corresponds to one button, starting at the previous button (or, for 
the first line, the "5" button); press whatever button you're on at the end of 
each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk 
to the bathroom. You picture a keypad like this:

1 2 3
4 5 6		 
7 8 9

Suppose your instructions are:
ULL
RRDDD
LURDL
UUUUD

- You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and 
  stay on "1"), so the first button is 1.
- Starting from the previous button ("1"), you move right twice (to "3") and 
  then down three times (stopping at "9" after two moves and ignoring the 
  third), ending up with 9.
- Continuing from "9", you move left, up, right, down, and left, ending with 8.
- Finally, you move up four times (stopping at "2"), then down once, ending 
  with 5.

So, in this example, the bathroom code is 1985.
Your puzzle input is the instructions from the document you found at the front 
desk. What is the bathroom code?

PERSONAL NOTES
( 0, 2 ), ( 1, 2 ), ( 2, 2 )	->		1, 2, 3
( 0, 1 ), ( 1, 1 ), ( 2, 1 )	->		4, 5, 6
( 0, 0 ), ( 1, 0 ), ( 2, 0 )	->		7, 8, 9

Start at ( 1, 1 ). If any coord is < 0 or > 3 then it is off the grid.

{	( 0, 2 ) : 1,
	( 1, 2 ) : 2,
	( 2, 2 ) : 3,
	( 0, 1 ) : 4,
	( 1, 1 ) : 5,
	( 2, 1 ) : 6,
	( 0, 0 ) : 7,
	( 1, 0 ) : 8, 
	( 2, 0 ) : 9, }
'''

import os

puzzle_input_filepath = os.path.abspath( os.path.join( os.getcwd( ), 
																		'02_puzzle_input.txt' ) )

with open( puzzle_input_filepath ) as file:
	input = file.read( )
	PUZZLE_INPUT = input.split( '\n' )


KEYPAD_MAP = { ( 0, 2 ) : '1',
				   ( 1, 2 ) : '2',
					( 2, 2 ) : '3',
					( 0, 1 ) : '4',
					( 1, 1 ) : '5',
					( 2, 1 ) : '6',
					( 0, 0 ) : '7',
					( 1, 0 ) : '8', 
					( 2, 0 ) : '9', 
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