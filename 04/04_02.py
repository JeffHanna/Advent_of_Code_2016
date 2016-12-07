# -*- coding: utf-8 -*- 
'''
--- Part Two ---
With all the decoy data out of the way, it's time to decrypt this list and get 
moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly 
unbreakable without the right software. However, the information kiosk designers 
at Easter Bunny HQ were not expecting to deal with a master cryptographer 
like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number 
of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, 
and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

PERSONAL NOTES:
* WTF?
'''

import os


def _make_letter_usage_map( room_name ):
	'''
	'''

	letter_usage_map = { }

	for c in room_name:
		letter_usage_map[ c ] = letter_usage_map.get( c, 0 ) + 1

	return letter_usage_map


def _verify_real_room( letter_usage_map, checksum ):
	'''
	* Idea: Iterate over checksum. If any char in it is
	  not in letter_usage_map, early return False.
	* Otherwise use weighting values in letter_usage_map to verify the char is
	  in the correct location.

	'''

	# Characters in checksum are in order of highest usage to lowest.
	# Usage ties are won by alphabetical order.
	# For instance in the first line of the data (which is a valid room) the
	# checksum is 'qhiwf'. i and w are both used 4 times in the room name.
	# Since i comes before w in the checksum they are in the correct locations.

	# Checksums must be exactly five characters.
	if len( checksum ) != 5:
	  return False 
	
	value = 9999 # ridiculously large to start with.
	char = ''
	for c in checksum:

		if c not in letter_usage_map.keys( ):
			return False
		else:
			v = letter_usage_map.get( c )
			if v < value:
				value = v
				char = c
			elif v == value:
				# use ASCII codes to determine if items are in the correct order.
				if ord( char ) < ord( c ):
					value = v
					char = c
				else:
					return False
			else:
				return False

	return True



def find_real_rooms( ):
	'''
	'''

	id_sum = 0
	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'04_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:
			parts = line.rstrip( ']\n' ).split( '-' )

			# Last element in parts contains the ID and the checksum.
			id, checksum = parts[ -1 ].split( '[' )
			id = int( id )

			room_name = ''
			for i in range( len( parts ) - 1 ):
				room_name += parts[ i ] + '-'

			room_name = room_name.rstrip( '-' )
			letter_usage_map = _make_letter_usage_map( room_name )
			
			if _verify_real_room( letter_usage_map, checksum ):
				id_sum += id

	return id_sum


												 
if __name__ == '__main__':
	id_sum = find_real_rooms( )
	print( 'The sum of the sector IDs of the real rooms is {0}.'.format( id_sum ) )