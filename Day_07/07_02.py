# -*- coding: utf-8 -*- 
'''
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

'''

import os


def _compare_aba_triples( a, b ):
	'''
	'''
	if len( a ) == len( b ) == 3:
		if a[ 0 ] == b[ 1 ] == a[ 2 ] or \
			b[ 0 ] == a[ 1 ] == b[ 2 ]:
				return True

	return False


def _has_aba_set( chars ):
	'''
	'''

	for i in range( 1, len( chars ) - 1 ):
		if chars[ i - 1 ] == chars[ i + 1 ] and chars[ i - 1 ] != chars[ i ]:
			return chars[ i - 1 : i + 2 ]

	return ''
		

def find_ssl_support( ):
	'''
	'''

	num_ssl_addresses = 0

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'07_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:
			line = line.rstrip( ).replace( '[', '/' ).replace( ']', '/' )
			parts = line.split( '/' )
				
			# Early out if square-bracketed do not contain ABA triples.
			inner_aba_triple = ''
			for i in range( 1, len( parts ) - 1, 2 ):
				inner_aba_triple =  _has_aba_set( parts[ i ] )
				if inner_aba_triple:
					break
			
			if inner_aba_triple:
				for i in range( 0, len( parts ), 2 ):
					outer_aba_triple = _has_aba_set( parts[ i ] )
					if outer_aba_triple:
						if _compare_aba_triples( inner_aba_triple, outer_aba_triple ):
							num_ssl_addresses += 1
							break

	return num_ssl_addresses



if __name__ == '__main__':
	val = find_ssl_support( )
	print( 'The number of addresses that support SSL is {0}.'.format( val ) )
