# -*- coding: utf-8 -*- 
"""
--- Part Two ---
You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the 
supernet sequences (outside any square bracketed sections), and a corresponding 
Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any 
three-character sequence which consists of the same character twice with a 
different character between them, such as xyx or aba. A corresponding BAB is the 
same characters but in reversed positions: yxy and bab, respectively.

For example:
- aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab 
  within square brackets).
- xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
- aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; 
  the aaa sequence is not related, because the interior character must 
  be different).
- zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a 
  corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

PERSONAL NOTES:

"""

import os


def _compare_aba_triplets( a, b ):
	"""
	The provied pair of aba triplets is compared to ensure that they are
	opposites of each other. For instance if a is 'xyx', then b must be 'yxy'.
	
	**Arguments:**
	
		:``a``:	`str` The first aba triplet to compare.
		:``b``:	`str` The second aba triplet to compare.
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`bool` True the triplets are opposites, else False.
	"""

	if len( a ) == len( b ) == 3:
		if a[ 0 ] == b[ 1 ] == a[ 2 ] or b[ 0 ] == a[ 1 ] == b[ 2 ]:
			return True

	return False


def _has_aba_triplet( chars ):
	"""
	The provided string is parsed to see if it has any characters in the 
	form of 'aba'. The outer two characters must be identical. The inner 
	character must not be the same as the outer two.
	
	**Arguments:**
	
		:``chars``:	`str` A string to examine for aba triplets.
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`bool` True if an abba pair is found, otherwise false.
	"""

	for i in range( 1, len( chars ) - 1 ):
		if chars[ i - 1 ] == chars[ i + 1 ] and chars[ i - 1 ] != chars[ i ]:
			return chars[ i - 1 : i + 2 ]

	return ''
		

def find_ssl_support( ):
	"""
	For every line in the input file the data is processed to determine if
	the 'IP' address supports the SSL protocol. Any address with an 
	aba triplet that has a corresponding bab triplet within a square bracketted
	section is valid. A count of valid addresses is kept and returned when
	all of the data has been parsed.

	Some data rules that simplify things:
	* A line will neither start with, nor end with, a square bracketted section.
	* Square bracketted sections will never be adjacent within the address.
		
	**Arguments:**
	
		None
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`int` The number of addresses that proved TLS support.
	"""

	num_ssl_addresses = 0
	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'07_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:
			line = line.rstrip( ).replace( '[', '/' ).replace( ']', '/' )
			parts = line.split( '/' )
				
			# Early out if square-bracketed do not contain ABA triples.
			inner_aba_triplet = ''
			for i in range( 1, len( parts ) - 1, 2 ):
				inner_aba_triplet =  _has_aba_triplet( parts[ i ] )
				if inner_aba_triplet:
					break
			
			if inner_aba_triplet:
				for i in range( 0, len( parts ), 2 ):
					outer_aba_triplet = _has_aba_triplet( parts[ i ] )
					if outer_aba_triplet:
						if _compare_aba_triplets( inner_aba_triplet, outer_aba_triplet ):
							num_ssl_addresses += 1
							break

	return num_ssl_addresses



if __name__ == '__main__':
	val = find_ssl_support( )
	print( 'The number of addresses that support SSL is {0}.'.format( val ) )
