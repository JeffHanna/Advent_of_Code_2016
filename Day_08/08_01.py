# -*- coding: utf-8 -*-
"""
--- Day 8: Two-Factor Authentication ---
You come across a door implementing what you can only assume is an 
implementation of two-factor authentication after a long game of 
requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a 
nearby desk). Then, it displays a code on a little screen, and you type that 
code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken 
everything apart and figured out how it works. Now you just have to work out 
what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for 
the screen; these instructions are your puzzle input. The screen is 50 pixels 
wide and 6 pixels tall, all of which start off, and is capable of three somewhat 
peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen 
which is A wide and B tall.

rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right 
by B pixels. Pixels that would fall off the right end appear at the left end of 
the row.

rotate column x=A by B shifts all of the pixels in column A (0 is the left 
column) down by B pixels. Pixels that would fall off the bottom appear at the 
top of the column.

For example, here is a simple sequence on a smaller screen:
  rect 3x2 creates a small rectangle in the top-left corner:
  ###....
  ###....
  .......

  rotate column x=1 by 1 rotates the second column down by one pixel:
  #.#....
  ###....
  .#.....

  rotate row y=0 by 4 rotates the top row right by four pixels:
  ....#.#
  ###....
  .#.....

  rotate column x=1 by 1 again rotates the second column down by one pixel, 
  causing the bottom pixel to wrap back to the top:
  .#..#.#
  #.#....
  .#.....

As you can see, this display technology is extremely powerful, and will soon 
dominate the tiny-code-displaying-screen market. That's what the advertisement 
on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: 
after you swipe your card, if the screen did work, how many pixels should 
be lit?

PERSONAL NOTES:
* I think a Display class with 5 lists of 50 elements each and rect( ),
  rotate_column( ), and rotate_row( ) methods may be best. It provides a
  fairly close 1:1 mapping with the input data and naturally saves state.
"""

import os 


class Display( object ):
	"""
	0 = off pixel
	1 = on pixel
	"""

	def __init__( self, rows, columns ):
		self.max_row = rows - 1
		self.max_column = columns - 1
		self._rows = [ ]

		# initialize blank 'display'
		for _r in range( rows ):
			row = [ ]
			for _c in range( columns ):				
				row.append( 0 )

			self._rows.append( row )


	@property
	def number_of_lit_pixels( self ):
		num = 0
		for r in self._rows:
			c = [ x for x in r if x == 1 ]
			num += len( c )
		
		return num


	def draw( self ):
		os.system( 'cls' )
		for r in self._rows:
			data = [ str( x ) for x in r ]
			line =  ''.join( data )
			print( line )


	def _column( self, column, amount ):
		"""
		"""

		new_column = [ ]

		# Initialize new column:
		for _i in range( len( column ) ):
			new_column.append( 0 )

		# TODO: FINISH!


	def _row( self, row, amount ):
		"""
		"""

		new_row = [ ]
		
		# Initialize new row.
		for _i in range( len( row ) ):
			new_row.append( 0 )

		for idx in range( len( row ) ):
			new_idx = idx + amount
			if new_idx > len( row ) - 1:
				new_idx -= len( row )

			new_row[ new_idx ] = row[ idx ]

		return new_row


	def rotate( self, type, index, amount ):
		"""
		:``type``:	`str` row or column
		:``index``:	`int` row or column to rotate
		:``amount``: `int` The amount of rotation.
		"""

		if type == 'row':
			new_row = self._row( self._rows[ index ], amount )
			self._rows[ index ] = new_row			

		else:
			column = [ ]
			for r in self._rows:
				column.append( r[ index ] )

			new_column = _column( column, amount )
			for r in self._rows:
				r[ index ] = new_column[ index ]				
														  		

	def rect( self, width, height ):
		"""
		Starting at ( 0, 0 ), the upper left corner, pixels are filled to make a
		rectangle of size ( width, height ). If a value goes out of bounds for the
		display size the value rolls over to the opposite edge. For instance width 
		values less than 0 will draw on the right edge of the display.

		"""

		for r in range( height ):
			if r < 0:
				r = len( self._rows ) - r
			elif r > len( self._rows ):
				r -= len( self._rows ) + 1

			for c in range( width ):
				self._rows[ r ][ c ] = 1


def get_number_of_lit_pixels( ):
	"""
	"""

	display = Display( 6, 50 )
	
	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'08_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:	
			line = line.rstrip( )
			parts = line.split( ' ' )
			if len( parts ) == 2:
				# rect command
				args = parts[ -1 ].split( 'x' )
				display.rect( int( args[ 0 ] ), int( args[ -1 ] ) )
			else:
				# rotate command
				args = parts[ 1: ]
				display.rotate( str( args[ 0 ] ), 
									 int( args[ 1 ][ 2: ] ),
									 int( args[ -1 ] ) )	  

			display.draw( )
			pass
	

	return display.number_of_lit_pixels






if __name__ == '__main__':
	lit_pixels = get_number_of_lit_pixels( )
	print( 'The number of pixels that should be lit is {0}.'.format( lit_pixels ) )
