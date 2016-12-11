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
*  
* For each instruction in the input data if it is a bot creation command
  execute it. If it is a value assignment command cache it.
* After the entire input file has been parsed walk through the assignment
  command cache and execute those commands in order.
* Whenever a bot contains two values call an update on it, which should trigger 
  cascade updates as it inevitably causes other bots to get two values.
* Whenever a bot gets two values check to see if they are 61 and 17. If so, that
  is the solution. Get the bot's number and return it.
"""

import os
import sys


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
		Compares the two values in the bot's self._values list to determine if the
		values are 17 and 63. If so, this puzzle has been solved, the bot prints
		out its identification number, and the program exits.

		Otherwise the two values are compared, with the lower and higher values
		being sent to other bots or bins based on this bots sorting rules.			

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

		if 61 in self._values and 17 in self._values:
			# THIS IS IT!
			print( 'The bot that processes both values 63 and 17 is bot {0}.'.format( self._NUMBER ) )
			os.system( 'pause' )
			sys.exit( 0 )					 

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



def find_bot( ):
	"""
	Parses input data to create an army of sorting bots with sorting rules and to
	then simulate those bots being given values and following their rules on
	how to sort and deliver the provided values. The goal is to find the one
	bot that has to sort the values of 17 and 63. Once that bot is identified
	it prints out its identification number and the simulation stops.

	**Arguments:**
	
		None

	**Keyword Arguments:**
	
		None

	**Returns:**

		None
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



if __name__ == '__main__':
	find_bot( )