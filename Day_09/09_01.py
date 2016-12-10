# -*- coding: utf-8 -*-
"""
--- Day 9: Explosives in Cyberspace ---
Wandering around a secure area, you come across a datalink port to a new part of 
the network. After briefly scanning it for interesting files, you find one file 
in particular that catches your attention. It's compressed with an experimental 
format, but fortunately, the documentation for the format is nearby.

The format compresses a sequence of characters. Whitespace is ignored. 
To indicate that some sequence should be repeated, a marker is added to the 
file, like (10x2). To decompress this marker, take the subsequent 10 characters 
and repeat them 2 times. Then, continue reading the file after the 
repeated data. The marker itself is not included in the decompressed output.

If parentheses or other characters appear within the data referenced by a 
marker, that's okay - treat it like normal data, not a marker, and then resume 
looking for markers after the decompressed section.

For example:
- ADVENT contains no markers and decompresses to itself with no changes, 
  resulting in a decompressed length of 6.
- A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a 
  decompressed length of 7.
- (3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
- A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a 
  decompressed length of 11.
- (6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because 
  it's within a data section of another marker, it is not treated any 
  differently from the A that comes after it. It has a decompressed length of 6.
- X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), 
  because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped 
  and not processed further.

What is the decompressed length of the file (your puzzle input)? 
Don't count whitespace.

PERSONAL NOTES:
* The goal for this puzzle is to only come up with the length (not including
  whitespace) of the unpacked data. There's no need to actually unpack it.
"""

import os


def get_length_of_unpacked_data( ):
	"""
	Parses the input data to get the one line of compressed data.
	Each character in the data is walked and then checked against the 
	decompression rules. A running total of the length of the uncompressed data
	is kept and returned when the function is complete.

	**Arguments:**
	
		None

	**Keyword Arguments:**
	
		None

	**Returns:**

		`int` Total character count (not including spaces) of decompressed data.
	"""

	unpacked_data_length = 0

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'09_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		lines = file.readlines( )

	line = lines[ 0 ].rstrip( )	
	unpack_command = ''
	
	i = 0
	while i < len( line):
		c = line[ i ]
		if c != '(' and c != ' ' and not unpack_command:
			unpacked_data_length += 1

		elif unpack_command:
			parts = unpack_command.split('x')
			unpack_length = int( parts[ 0 ] )
			mult = int( parts[ -1 ] )
			unpacked_data_length += ( unpack_length * mult)
			unpack_command = ''
			i += unpack_length - 1

		elif c == '(':
			for j in range( i + 1, len( line ) ):
				if line[ j ] != ')':
					unpack_command += line[ j ]
				else:
					i = j
					break
		i += 1

	return unpacked_data_length


if __name__ == '__main__':
	unpacked_data_length = get_length_of_unpacked_data( )
	print( 'The length of the unpacked data is {0}.'.format( unpacked_data_length) ) 