# -*- Coding: UTF-8 -*-
"""
--- Day 10: Balance Bots ---
You come upon a factory in which many robots are zooming around handing small 
microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two 
microchips, and once it does, it gives each one to a different bot or puts it in 
a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single 
number; the bots must use some logic to decide what to do with each chip. 
You access the local control computer and download the bots' instructions 
(your puzzle input).

Some of the instructions specify that a specific-valued microchip should be 
given to a specific bot; the rest of the instructions indicate what a given bot 
should do with its lower-value or higher-value chip.

For example, consider the following instructions:
  value 5 goes to bot 2
  bot 2 gives low to bot 1 and high to bot 0
  value 3 goes to bot 1
  bot 1 gives low to output 1 and high to bot 0
  bot 0 gives low to output 2 and high to output 0
  value 2 goes to bot 2

- Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 
  chip and a value-5 chip.
- Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its 
  higher one (5) to bot 0.
- Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives 
  the value-3 chip to bot 0.
- Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in 
  output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a 
value-2 microchip, and output bin 2 contains a value-3 microchip. In this 
configuration, bot number 2 is responsible for comparing value-5 microchips with 
value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible 
for comparing value-61 microchips with value-17 microchips?

PERSONAL NOTES:
* The input data does not have to be parsed to completion, it only has to 
  run to the point that the bot that handles 61 <> 17 sorting.
* Value 61 ALWAYS goes to bot 166 to start. (yeah, I searched the input data)
* Value 17 ALWAYS goes to bot 63 to start.
* Input data is always
  bot <INT> gives low to bot <INT> and high to bot <INT>
	or
  value <INT> goes to bot <INT>

  So the input parse can be constructed to be optimal to those 2 options.
* Make a Bot class. 
* For each instruction in the input data search the list of
  existing bot classes to see if it already exists. 
* If not, create it. 
* If it does, populate it with the data from the input. 
* Whenever a bot contains two values call an update on it, which should trigger 
  cascade updates as it inevitably causes other bots to get two values.
* Whenever a bot gets two values check to see if they are 61 and 17. If so, that
  is the solution. Get the bot's number and return it.
"""

import os


_bots = { }

class Bot( object ):
	"""
	"""

	def __init__( self, number, low_to = -1, high_to = -1 ):
		self._NUMBER = number
		self._low_to = low_to
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

	def assign_low_to( self, val ):
		"""
		"""

		self._low_to = val


	def assign_high_to( self, val ):
		"""
		"""

		self._high_to = val


	def _update( self ):
		"""
		"""

		low_value = 99999
		low_idx = -1
		high_idx = 3

		if 61 in self._values and 17 in self._values:
			# THIS IS IT!
			print( 
				'Bot number {0} is reponsible for sorting values 17 and 61'.format( self._NUMBER ) )
			sys.exit( 0 )

		else:
			for i in range( 2 ):
				if self._values[ i ] < low_value:
					low_value = self._values[ i ]
					low_idx = i
					high_idx = low_idx - 1

		low_bot = _bots.get( self._low_to, None )
		if not low_bot and self._low_to >= 0:
			_bots[ self._low_to ] = Bot( self._low_to )
		else:
			raise Exception( 'Bot number {0} trying to assign a low value without a valid bot number to send it.'.format( self._NUMBER ) )

		low_bot.add_value( self._values[ low_idx ])

		high_bot = _bots.get( self._high_to, None )
		if not high_bot and self._high_to >= 0:
			_bots[ self._high_to ] = Bot( self._high_to )
		else:
			raise Exception( 'Bot number {0} trying to assign a high value without a valid bot number to send it.'.format( self._NUMBER ) )
			
		high_bot.add_value( self._values[ high_idx ] )



def find_bot( ):
	"""
	"""

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'10_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		# TODO: Maybe use a global FOUND flag instead of having the bot class
		#       end the program?
		for line in file:
			line = line.rstrip( )
			parts = line.split( ' ' )
			if parts[ 0 ] == 'bot':
				bot_num = int( parts[ 1 ] )
				low_to = int( parts[ 6 ] )
				high_to = int( parts[ -1 ] )
				if not bot_num in _bots.keys( ):
					_bots[ bot_num ] = Bot( bot_num, low_to = low_to, high_to = high_to )
					
			else:
				val = int( parts[ 1 ] )
				bot_num = int( parts[ -1 ] )
				if not bot_num in _bots.keys( ):
					_bots[ bot_num ] = Bot( bot_num )
				bot = _bots.get( bot_num, None )
				bot.add_value( val )
								


if __name__ == '__main__':
	find_bot( )