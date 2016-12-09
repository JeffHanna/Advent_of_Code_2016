# -*- coding: utf-8 -*- 
'''
--- Day 7: Internet Protocol Version 7 ---
While snooping around the local network of EBHQ, you compile a list of IP 
addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to 
figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. 
An ABBA is any four-character sequence which consists of a pair of two different 
characters followed by the reverse of that pair, such as xyyx or abba. However, 
the IP also must not have an ABBA within any hypernet sequences, which are 
contained by square brackets.

For example:
- abba[mnop]qrst supports TLS (abba outside square brackets).
- abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even 
  though xyyx is outside square brackets).
- aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters 
  must be different).
- ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even 
  though it's within a larger string).

How many IPs in your puzzle input support TLS?

PERSONAL NOTES:
* The real data has lines with multiple square-bracketed sections.
* A line neither starts nor ends with a square-bracketed section.
* A line never contains square-bracketed sections that are adjacent.

* Go through each line. For each character see if the next character is 
  the same.
* If it is go -1 of the first character and +1 of the second and see if those
  are the same.
* Go to the characters within the square brackets and run the check again.
  If there is a match there the entire thing is invalid.
* I should really learn regex.
'''

import os


def _has_abba_set( chars ):
	'''
	'''

	for i in range( 1, len( chars ) - 2 ):
		if chars[ i ] == chars[ i + 1 ] and \
			chars[ i - 1 ] == chars[ i + 2 ] and \
			chars[ i - 1 ] != chars[ i ]:
			return True

	return False
				  

def find_tls_support( ):
	'''
	'''

	num_tls_addresses = 0
	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'07_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:
			line = line.rstrip( ).replace( '[', '/' ).replace( ']', '/' )
			parts = line.split( '/' )
				
			# Early out if square-bracketed sections contain ABBA pairs.
			found_inner = False
			for i in range( 1, len( parts ) - 1, 2 ):
				if _has_abba_set( parts[ i ] ):
					found_inner = True
					break
			
			if not found_inner:
				for i in range( 0, len( parts ), 2 ):
					if _has_abba_set( parts[ i ] ):
						num_tls_addresses += 1
						break

	return num_tls_addresses



if __name__ == '__main__':
	val = find_tls_support( )
	print( 'The number of addresses that support TLS is {0}.'.format( val ) )