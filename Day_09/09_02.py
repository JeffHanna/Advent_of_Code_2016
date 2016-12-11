# -*- coding: utf-8 -*-
"""
--- Part Two ---
Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data are 
decompressed. This, the documentation explains, provides much more substantial 
compression capabilities, allowing many-gigabyte files to be stored in only a 
few kilobytes.

For example:
- (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains 
  no markers.
- X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data 
  from the (8x2) marker is then further decompressed, thus triggering the (3x3) 
  marker twice for a unpacked_length of six ABC sequences.
- (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 
  241920 times.
- (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 
  characters long.
- Unfortunately, the computer you brought probably doesn't have enough memory to 
  actually decompress the file; you'll have to come up with another way to get 
  its decompressed length.
- What is the decompressed length of the file using this improved format?

PERSONAL NOTES:
* Very similar to 09 01 except that each unpacked section will need to be
  recursively unpacked.
"""

import os


def get_length_of_unpacked_data( line ):	
	"""
	For the provided line of input data each character is walked to find
	decompression commands, specified as (#x#). When a decompression command is
	found the first integer is used to gather up that many characters in the 
	input line after the command. The second integer is used as a multiplicaiton
	factor to 'unpack' the data and add the unpacked string length to the running
	total kept in the unpacked_length variable. If the unpacked string starts
	with a decompression command it is passed into this function recursively
	until the resulting unpacked string does not start with a 
	decompression command. 
	When this function, and all recursively spawned instances of this function,
	is complete the total length of the unpacked data is returned.

	**Arguments:**
	
		:``line``: `str`	A string of compressed data including embedded 
								decompression commands.

	**Keyword Arguments:**
	
		None

	**Returns:**

		`int` Total character count (not including spaces) of decompressed data.
	"""

	unpacked_length = 0
	
	i = 0
	while i < len( line ):
		if line[ i ] == '(':
			i += 1
			unpack_command = ''
			
			while line[ i ] != ')':
				unpack_command += line[ i ]
				i += 1

			parts = unpack_command.split( 'x' )
			chars = int( parts[ 0 ] )
			factor = int( parts[ 1 ] )
			unpacked_length += factor * get_length_of_unpacked_data( 
				line[ i + 1 : i + chars + 1 ] )

			i += chars
		else:
			unpacked_length += 1
		i += 1
	return unpacked_length
						


if __name__ == '__main__':
	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'09_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		lines = file.readlines( )
	
	line = lines[ 0 ].rstrip( )

	unpacked_data_length = get_length_of_unpacked_data( line )
	print( 'The length of the unpacked data is {0}.'.format( unpacked_data_length) ) 