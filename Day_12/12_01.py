# -*- coding: utf-8 -*-
"""
--- Day 12: Leonardo's Monorail ---
You finally reach the top floor of this building: a garden with a slanted glass 
ceiling. Looks like there are no more stars to be had.

While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt 
some of the files you extracted from the servers downstairs.

According to these documents, Easter Bunny HQ isn't just this building - it's a 
collection of buildings in the nearby area. They're all connected by a local 
monorail, and there's another building not far from here! Unfortunately, being 
night, the monorail is currently not operating.

You remotely connect to the monorail control systems and discover that the boot 
sequence expects a password. The password-checking logic (your puzzle input) is 
easy to extract, but the code it uses is strange: it's assembunny code designed 
for the new computer you just assembled. You'll have to execute the code and get 
the password.

The assembunny code you've extracted operates on four registers (a, b, c, and d) 
that start at 0 and can hold any integer. However, it seems to make use of only 
a few instructions:
  cpy x y copies x (either an integer or the value of a register) into register y.
  inc x increases the value of register x by one.
  dec x decreases the value of register x by one.
  jnz x y jumps to an instruction y away (positive means forward; negative means 
			 backward), but only if x is not zero.

  The jnz instruction moves relative to itself: an offset of -1 would continue 
  at the previous instruction, while an offset of 2 would skip over the 
  next instruction.

For example:
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a

The above code would set register a to 41, increase its value by 2, decrease its 
value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 
skips it), leaving register a at 42. When you move past the last instruction, 
the program halts.

After executing the assembunny code in your puzzle input, what value is left in 
register a?

PERSONAL NOTES:
* WOOHOO, all of my time in TIS-100 is about to pay off.
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
						  'c' : Register( 0 ),
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