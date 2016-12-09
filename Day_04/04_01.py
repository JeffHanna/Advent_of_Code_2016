# -*- coding: utf-8 -*- 
"""
--- Day 4: Security Through Obscurity ---
Finally, you come across an information kiosk with a list of rooms. Of course, 
the list is encrypted and full of decoy data, but the instructions to decode the 
list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) 
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in 
the encrypted name, in order, with ties broken by alphabetization. For example:

- aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are 
  a (5), b (3), and then a tie between x, y, and z, which are 
  listed alphabetically.
- a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all 
  tied (1 of each), the first five are listed alphabetically.
- not-a-real-room-404[oarel] is a real room.
- totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

PERSONAL NOTES:
* Not awfully complex. Iterate over each line in the input
* Assume everything after the last - is the ID and the checksum. 
* Iterate over everything before that to tally up the usage of the letters.
* Knowing regex would be useful, but not necessary.
"""

import os


def _make_letter_usage_map( room_name ):
	"""
	Enter a description of the function here.
	
	**Arguments:**
	
		:``Argument``:	`arg_type` Enter a description for the argument here.
	
	**Keyword Arguments:**
	
		:``Argument``:	`arg_type` Enter a description for the keyword argument here.
	
	**Returns:**
	
		`arg_type` If any, enter a description for the return value here.
	"""

	letter_usage_map = { }

	for c in room_name:
		letter_usage_map[ c ] = letter_usage_map.get( c, 0 ) + 1

	return letter_usage_map


def _verify_real_room( letter_usage_map, checksum ):
	"""
	Enter a description of the function here.
	
	**Arguments:**
	
		:``Argument``:	`arg_type` Enter a description for the argument here.
	
	**Keyword Arguments:**
	
		:``Argument``:	`arg_type` Enter a description for the keyword argument here.
	
	**Returns:**
	
		`arg_type` If any, enter a description for the return value here.
	"""
	"""
	* Idea: Iterate over checksum. If any char in it is
	  not in letter_usage_map, early return False.
	* Otherwise use weighting values in letter_usage_map to verify the char is
	  in the correct location.

	"""

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
	"""
	Enter a description of the function here.
	
	**Arguments:**
	
		:``Argument``:	`arg_type` Enter a description for the argument here.
	
	**Keyword Arguments:**
	
		:``Argument``:	`arg_type` Enter a description for the keyword argument here.
	
	**Returns:**
	
		`arg_type` If any, enter a description for the return value here.
	"""

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