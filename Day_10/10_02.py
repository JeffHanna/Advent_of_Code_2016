# -*- Coding: UTF-8 -*-
"""
--- Part Two ---
What do you get if you multiply together the values of one chip in each of 
outputs 0, 1, and 2?

PERSONAL NOTES:
* Expand the ouput bin class from puzzle 1to return a random value from 
  the list.
* Run the simulation to completion then query bins 0, 1 and 2 for a value
  and multiply them.
"""

import os
import random


_bots = { }
_output_bins = { }

class Output_Bin( object ):
	"""
	Simple container to hold values when a bot is instructed to deliver a chip
	to a numbered output bin.

	**Arguments:**
	
		:``number``:	`int` The identification number of the bin

	**Keyword Arguments:**
	
		None
	"""

	def __init__( self, number ):
		self._NUMBER = number
		self._values = [ ]


	def add_value( self, val ):
		"""
		Adds an integer value to the output bin's self._values list

		**Arguments:**
	
			:``value``:	`int` The number to be added to the list.

		**Keyword Arguments:**
	
			None

		**Returns:**

			None
		"""

		self._values.append( val )


	@property
	def random_value( self ):
		"""
		Returns a random value from the bin's self._values list.
		Presented as a property for ease of use.

		**Arguments:**
	
			None

		**Keyword Arguments:**
	
			None

		**Returns:**

			`int` A random value from self._values.
		"""

		i = random.randint( 0, len( self._values ) - 1 )
		return self._values[ i ]



class Bot( object ):
	"""
	A representation of one of the factory bots. A bot takes two values, compares
	them, and hands them off based on static rules of 'low value goes to...' and
	'high value goes to...'

	**Arguments:**
	
		:``number``:	`int` The identification number of the bot.

	**Keyword Arguments:**
	
		:``low_to_bin``:	`bool`	If true the low value goes to a output bin.
		:``low_to``:		`int`		The numbered bot or bin to deliver the 
											low value.
		:``high_to_bin``:	`bool`	If true the high value goes to a bin.
		:``high_to``:		`int`		The numbered bot or bin to deliver the 
											high value.
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
		Adds an integer value to the bot's self._values list. If the addition
		results in the bot's self._values list to have 2 elements the bot's
		_update() function is called to compare the data and move the values to
		the appropriate destination bots and bins.

		**Arguments:**
	
			:``value``:	`int` The number to be added to the list.

		**Keyword Arguments:**
	
			None

		**Returns:**

			None
		"""

		if len( self._values ) <= 1:
			self._values.append( val )
			if len( self._values ) == 2:
				self._update( )
		else:
			raise IndexError( 'Bot {0} already has two values!'.format( self._NUMBER ) )


	def _update( self ):
		"""
		The two values in the bot's self._values list are compared, with the lower 
		and higher values being sent to other bots or bins based on this bots 
		sorting rules.			

		**Arguments:**
	
			None

		**Keyword Arguments:**
	
			None

		**Returns:**

			None
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
	Parses input data to create an army of sorting bots with sorting rules and to
	then simulate those bots being given values and following their rules on
	how to sort and deliver the provided values. The goal is to run the 
	simulation to completion, grab a single value from each of the 0, 1, and 2
	output bins, and multiply them. That result is returned.

	**Arguments:**
	
		None

	**Keyword Arguments:**
	
		None

	**Returns:**

		`int` The result of multiplying together single values from output bins
				0, 1, and 2.
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