# -*- coding: utf-8 -*-
"""
--- Part Two ---
You notice that the screen is only capable of displaying capital letters; in the 
font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

PERSONAL NOTES:
* Call Display.draw( ) after all commands have been run and 
  look at the output. Cheap, but effective. Should I write a parse to 
  'screen scrape' and present the result as a string?
"""

import os 


class Display( object ):
	"""
	Simple class to emulate the pixels of a hypothetical display.
	The data is a list of lists, with each inner list containing 1s and 0s 
	indicating the state of each pixel in that row.
	0 = off pixel
	1 = on pixel  		

	**Arguments:**
	
		:``rows``:	`int`  The number of rows in the display
		:``columns``: `int` The number of columns in each row.
	
	**Keyword Arguments:**
	
		None
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


	def draw( self ):
		"""		
		Simple function to draw each 'screen' after a command has been processed.
		Useless for calculating the solution, but useful for some debugging.

		**Arguments:**
	
			None
	
		**Keyword Arguments:**
	
			None
	
		**Returns:**
	
			None
		"""
		
		os.system( 'cls' )
		for r in self._rows:
			data = [ str( x ) for x in r ]
			line =  ''.join( data )
			line = line.replace( '0', ' ' ).replace( '1', '#' )
			print( line )


	def _transpose( self, data, amount ):
		"""		
		Private helper function for the 'rotate' command. Given a list
		of pixels each pixel is moved by the provided amount. When a pixel
		moves 'off' of the list it is wrapped around to the opposite side.

		**Arguments:**
	
			:``data``:	`list` A list of integers representing lit and 
			                   unlit pixels.
			:``amount``: 'int` The number of 'pixels' each value in the list should
			                   be moved.
	
		**Keyword Arguments:**
	
			None
	
		**Returns:**
	
			`list`  A list of integers representing lit and unlit pixels after
			       they have been moved.
		"""

		new_data = [ ]

		# Initialize new data:
		for _i in range( len( data ) ):
			new_data.append( 0 )

		for idx in range( len( data ) ):
			new_idx = idx + amount
			if new_idx > len( data ) - 1 :
				new_idx -= len( data )

			new_data[ new_idx ] = data[ idx ]

		return new_data


	def rotate( self, type, index, amount ):
		"""		
		Maps to the 'rotate' command in the input data. For the type, either
		row or column and the index of the row or column every pixel in that
		row or column is shifted (right or down, depending) by the provided
		amount		

		**Arguments:**
	
		:``type``:		`str` row or column
		:``index``:		`int` row or column to rotate
		:``amount``:	`int` The amount of rotation.
	
		**Keyword Arguments:**
	
			None
	
		**Returns:**
	
			None
		"""

		if type == 'row':
			new_row = self._transpose( self._rows[ index ], amount )
			self._rows[ index ] = new_row			

		else:
			column = [ ]
			for r in self._rows:
				column.append( r[ index ] )

			new_column = self._transpose( column, amount )
			for i in range( len( self._rows ) ):
				self._rows[ i ][ index ] = new_column[ i ]				
														  		

	def rect( self, width, height ):
		"""
		Starting at ( 0, 0 ), the upper left corner, pixels are filled to make a
		rectangle of size ( width, height ). If a value goes out of bounds for the
		display size the value rolls over to the opposite edge. For instance width 
		values less than 0 will draw on the right edge of the display.	
		
		**Arguments:**
	
			:``width``:		`int`	The width, in pixels of the rect
			:``height``:	`int`	The height, in pxels of the rect.
	
		**Keyword Arguments:**
	
			None
	
		**Returns:**
	
			None
		"""

		for r in range( height ):
			if r < 0:
				r = len( self._rows ) - r
			elif r > len( self._rows ):
				r -= len( self._rows ) + 1

			for c in range( width ):
				self._rows[ r ][ c ] = 1


def display_message( ):
	"""
	Parses the input data to determine the list of draw commands that need to be 
	run. Those commands are emulated on an instance of the Display class. 
	After all input commands are run the Display class is queried for the number
	of pixels that would be lit.

	**Arguments:**
	
		None
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`int` The number of lit pixels
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



if __name__ == '__main__':
	display_message( )
