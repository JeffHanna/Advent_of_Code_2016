# -*- Coding: UTF-8 -*-
"""
--- Part Two ---
What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

PERSONAL NOTES:
"""

import os
import random


_bots = { }
_output_bins = { }

class Output_Bin( object ):
	"""
	"""

	def __init__( self, number ):
		self._NUMBER = number
		self._values = [ ]


	def add_value( self, val ):
		"""
		"""

		self._values.append( val )


	@property
	def random_value( self ):
		"""
		"""

		i = random.randint( 0, len( self._values ) - 1 )
		return self._values[ i ]



class Bot( object ):
	"""
	"""

	def __init__( self, number, low_to_bin = False, low_to = -1, high_to_bin = False, high_to = -1 ):
		self._NUMBER = number
		self._low_to_bin = low_to_bin
		self._low_to = low_to
		self._high_to_bin = high_to_bin
		self._high_to = high_to
		self._values = [ ] # max of 2 items


	def add_value( self, val ):
		"""
		"""

		if len( self._values ) <= 1:
			self._values.append( val )
			if len( self._values ) == 2:
				self._update( )
		else:
			raise IndexError( 'Bot {0} already has two values!'.format( self._NUMBER ) )


	def _update( self ):
		"""
		"""

		low_value = 99999
		low_idx = -1
		high_idx = 3

		if self._low_to >= 0 and self._high_to >= 0:
			for i in range( 2 ):
				if self._values[ i ] < low_value:
					low_value = self._values[ i ]
					low_idx = i
					high_idx = low_idx - 1

			if self._low_to_bin:
				low_dest = _output_bins.get( self._low_to, None )
			else:
				low_dest = _bots.get( self._low_to, None )
			low_dest.add_value( self._values[ low_idx ])

			if self._high_to_bin:
				high_dest = _output_bins.get( self._high_to, None )
			else:
				high_dest = _bots.get( self._high_to, None )
			high_dest.add_value( self._values[ high_idx ] )



def find_output_bin_product( ):
	"""
	"""

	# Setup output bins
	for i in range( 21 ):
		_output_bins[ i ] = Output_Bin( i )	

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'10_puzzle_input.txt' ) )

	current_line = 0
	val_assignments = [ ]
	with open( puzzle_input_filepath ) as file:
		for line in file:
			current_line += 1
			line = line.rstrip( )
			parts = line.split( ' ' )
			if parts[ 0 ] == 'bot':
				bot_num = int( parts[ 1 ] )
				low_bot = len( parts[ 5 ] ) == 3
				low_to = int( parts[ 6 ] )
				high_bot = len( parts[ -2 ] ) == 3
				high_to = int( parts[ -1 ] )

				if not bot_num in _bots.keys( ):
					_bots[ bot_num ] = Bot( bot_num,
													low_to_bin = not low_bot, 
													low_to = low_to,
													high_to_bin = not high_bot, 
													high_to = high_to )
					
			else:
				val = int( parts[ 1 ] )
				bot_num = int( parts[ -1 ] )
				val_assignments.append( ( bot_num, val ) )

	for v in val_assignments:
		bot = _bots.get( v[ 0 ] )
		bot.add_value( v[ -1 ] )
		
	val = _output_bins[ 0 ].random_value * _output_bins[ 1 ].random_value * _output_bins[ 2 ].random_value								  
	return val



if __name__ == '__main__':
	val = find_output_bin_product( )
	print( 'The result of multiplying together a single value from output bins 0, 1, and 2 is {0}.'.format( val ) )