# -*- coding: utf-8 -*-
"""
--- Part Two ---
The second disk you have to fill has length 35651584. Again using the initial 
state in your puzzle input, what is the correct checksum for this disk?

Your puzzle input is still 10001001100000001.
"""								  

def calculate_checksum( state ):
	"""
	for every 2 characters
	if they are identical append 1 to the checksum
	otherwise append 0
	recursive calculate checksum of the checksum until
	it has an odd # of digits.
	"""
	
	checksum = ''
	for i in range( 0, len( state ), 2 ):
		pair = state[ i : i + 2 ]
		if pair in [ '00', '11' ]:
			checksum += '1'
		else:
			checksum += '0'

	return checksum


def dragon_curve( state ):
	"""
	"""

	a = state + '0'
	b = list( state )
	b.reverse( )
	for i in range( len( b ) ):
		b[ i ] = '0' if b[ i ] == '1' else '1'
	a += ''.join( b )

	return a


def fill_disk( state, length ):
	state = str( state )
	while len( state ) < length:
		state = dragon_curve( state )

	state = state[ : length ]
	checksum = calculate_checksum( state )
	while len( checksum ) % 2 == 0:
		checksum = calculate_checksum( checksum )

	return checksum


if __name__ == '__main__':
	checksum = fill_disk( 10001001100000001, 35651584 )
	print( 'The checksum for the generated data is {0}.'.format( checksum ) )