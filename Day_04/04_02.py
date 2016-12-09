# -*- coding: utf-8 -*- 
"""
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
* The trick in the instructions is that the encrypted room name has to be
  decrypted by rotating each character through the alphabet by the id a number 
  of times equal to the id. For instance, the id of the first room is 660, so
  each character has to be rot_660'd 660 times. Only doing rot_660 1 time will 
  lead to false positive answsers.
"""

import os
import string


def _decode_room_name( encrypted_room_name, id ):
	"""
	Using the value of the id each character of the encrypted room name is 
	rot'd that value that number of times. So, if the id is 660 each character is
	rot_660's 660 times. Only lowercase alphanumeric characters are decoded.
	
	**Arguments:**
	
		:``encrypted_room_name``:	`str` The encrypted room name from the
													input data
		:``id``: 'int'							The room id from the input data.
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`str` The decrypted room name
	"""

	lower = string.ascii_lowercase
	lower_start = ord( lower[ 0 ] )
	room_name = encrypted_room_name

	for _i in range( id ):
		temp_room_name = ''
		for char in room_name:
			if char in lower:
				temp_room_name += chr( lower_start + 
								  ( ord( char ) - lower_start + -id ) % 26 )
			elif char == '-':
				temp_room_name += ' '
			else:
				temp_room_name += char

		room_name = temp_room_name

	return room_name
				 									  


def _make_letter_usage_map( room_name ):
	"""
	Counts the useage of each letter in the encrypted room name and returns the
	data as a dictionary of { letter : count } pairs.
	
	**Arguments:**
	
		:``room_name``:	`str` The room name to perform the letter frequency
										count on
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`dict`
	"""

	letter_usage_map = { }

	for c in room_name:
		letter_usage_map[ c ] = letter_usage_map.get( c, 0 ) + 1

	return letter_usage_map



def _verify_real_room( letter_usage_map, checksum ):
	"""
	Using the letter frequency data and the checksum from the input data
	the checksum is validated using the following rules:
	# Characters in checksum are in order of highest usage to lowest.
	# Usage ties are won by alphabetical order.
	# For instance in the first line of the data (which is a valid room) the
	# checksum is 'qhiwf'. i and w are both used 4 times in the room name.
	# Since i comes before w in the checksum they are in the correct locations.
	* Idea: Iterate over checksum. If any char in it is
	  not in letter_usage_map, early return False.
	* Otherwise use weighting values in letter_usage_map to verify the char is

	**Arguments:**
	
		:``letter_usage_map``:	`dict`	The frequency data of each letter in the
													encrypted room name.
		:``checksum``: `string`				The room checksum from the input data
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`bool` True if the checksum passes for the real name, otherwise False.
	"""

	

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



def find_north_pole_object_room( ):
	"""
	Parses each line in the input file to divide the line into an id, a checksum,
	and an encrypted room name. The encrypted room name and the checksum are used
	to create a character frequency map and to decode the room name. If the
	decoded room name contains the words "northpole object" it is the room that
	is being searched for and the room id is returned.
	
	**Arguments:**
	
		None
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`int` The id of the room holding Santa's toys.
	"""

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'04_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:
			parts = line.rstrip( ']\n' ).split( '-' )

			# Last element in parts contains the ID and the checksum.
			id, checksum = parts[ -1 ].split( '[' )
			id = int( id )

			encrypted_room_name = ''
			for i in range( len( parts ) - 1 ):
				encrypted_room_name += parts[ i ] + '-'

			encrypted_room_name = encrypted_room_name.rstrip( '-' )
			letter_usage_map = _make_letter_usage_map( encrypted_room_name )
			
			if _verify_real_room( letter_usage_map, checksum ):
				room_name = _decode_room_name( encrypted_room_name, id )
			
				if 'northpole object' in room_name:
					return id


	return -1


												 
if __name__ == '__main__':
	id = find_north_pole_object_room( )
	print( 'The sector ID of the room where the North Pole objects are stored is {0}.'.format( id ) )
