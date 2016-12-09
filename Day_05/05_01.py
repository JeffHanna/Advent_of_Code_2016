# -*- coding: utf-8 -*- 
"""
--- Day 5: How About a Nice Game of Chess? ---
You are faced with a security door designed by Easter Bunny engineers that seem 
to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time 
by finding the MD5 hash of some Door ID (your puzzle input) and an increasing 
integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal 
representation starts with five zeroes. If it does, the sixth character in the 
hash is the next character of the password.

For example, if the Door ID is abc:
- The first index which produces a hash that starts with five zeroes is 3231929, 
  which we find by hashing abc3231929; the sixth character of the hash, and thus 
  the first character of the password, is 1.
- 5017308 produces the next interesting hash, which starts with 000008f82..., 
  so the second character of the password is 8.
- The third time a hash starts with five zeroes is for abc5278568, 
  discovering the character f.

In this example, after continuing this search a total of eight times, 
the password is 18f47a30.

Given the actual Door ID, what is the password?

Your puzzle input is cxdnnyjw.

PERSONAL NOTES:
* hashlib to the rescue!!
* In Python 3.x strings passed to hashlib need to be encoded, so b"" instead 
  of "".
* There's no need to use regex to count the leading zeros or find the sixth
  character. .startswith() and indexing will be fast enough.
* Overall this is SLOW!! When running to find the solution it is best to not
  run it in debug.
"""

import hashlib


def find_password( door_id ):
	"""
	Decodes the inputed door_id string character by character.
	For a loop that iterates for the length of the door_id an integer is 
	added to the name and an MD5 has is cacluated. If the hex result of the hash
	starts with 5 zeros, '00000' the sixth digit of the hash is the next valid
	character in the password and is added to the return string. Whether or not
	the hash is valid the incrementer is increased by 1, added back on to the 
	door_id (so: door_id0, door_id1,...door_id999, and another hash 
	is calculated. This continues until a password equal to the length of the
	door_id is found.
	
	**Arguments:**
	
		:``door_id``:	`str` 
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`string` The decoded password
	"""

	password = ''
	incrementor = 0

	for _i in range( len( door_id ) ):
		char = ''
		while not char:
			m = hashlib.md5( )
		
			input = door_id + str( incrementor )
			m.update( input.encode( 'utf-8' ) )
			hash = m.hexdigest( )
		
			if hash.startswith( '00000' ):
				char = hash[ 5 ]
				password += char
			
			incrementor += 1

	return password


if __name__ == '__main__':
	password = find_password( 'cxdnnyjw' )
	print( 'The door password is {0}'.format( password ) )