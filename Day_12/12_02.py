# -*- coding: utf-8 -*-
"""
--- Part Two ---
As you head down the fire escape to the monorail, you notice it didn't start; 
register c needs to be initialized to the position of the ignition key.

If you instead initialize register c to be 1, what value is now left in 
register a?

PERSONAL NOTES:
* Just change 'c = 0' to 'c = 1' and run.
"""

import os


class Register( object ):
	"""
	"""

	def __init__( self, initial_value ):
		self._value = initial_value

	@property
	def value( self ):
		return self._value

	@value.setter
	def value( self, val ):
		self._value = val



def find_value_of_register_a( ):
	"""
	"""

	register_map = { 'a' : Register( 0 ),
						  'b' : Register( 0 ),
						  'c' : Register( 1 ),
						  'd' : Register( 0 ), }

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'12_puzzle_input.txt' ) )

	input = [ ]
	with open( puzzle_input_filepath ) as file:
		input = file.readlines( )

	i = 0
	while i < len( input ):
		line = input[ i ].strip( ) 
		parts = line.split( ' ' )
		command = parts[ 0 ]

		if command == 'cpy':
			val = parts[ 1 ]
			val = int( val ) if val.isdigit( ) else register_map.get( val ).value
			destination = parts[ -1 ]
			register_map.get( destination ).value = val
			i += 1

		elif command == 'dec':
			register = parts[ -1 ]
			register_map.get( register ).value -= 1
			i += 1

		elif command == 'inc':
			register = parts[ -1 ]
			register_map.get( register ).value += 1
			i += 1

		elif command == 'jnz':
			val = parts[ 1 ]
			val = int( val ) if val.isdigit( ) else register_map.get( val ).value
			if val != 0:
				i += int( parts[ -1 ] )
			else:
				i += 1
			
		else:
			raise Exception( 'Input error, no valid command!' )

	return register_map.get( 'a' ).value


if __name__ == '__main__':
	val = find_value_of_register_a( )
	print( 'The value of register A is {0}.'.format( val ) )