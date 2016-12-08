# -*- coding: utf-8 -*- 
'''
--- Part Two ---
As the door slides open, you are presented with a second door that uses a 
slightly more inspired security mechanism. Clearly unimpressed by the last 
version (in what movie is the password decrypted in order?!), the Easter Bunny 
engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also 
indicates the position within the password to fill. You still look for hashes 
that begin with five zeroes; however, now, the sixth character represents the 
position (0-7), and the seventh character is the character to put in 
that position.

A hash result of 000001f means that f is the second character in the password. 
Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:
- The first interesting hash is from abc3231929, which produces 0000015...; 
  so, 5 goes in position 1: _5______.
- In the previous method, 5017308 produced an interesting hash; however, it is 
  ignored, because it specifies an invalid position (8).
- The second interesting hash is at index 5357525, which produces 000004e...; 
  so, e goes in position 4: _5__e___.

You almost choke on your popcorn as the final character falls into place, 
producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra 
proud of your solution if it uses a cinematic "decrypting" animation.

Your puzzle input is still cxdnnyjw.

PERSONAL NOTES:
'''

import copy
import hashlib
import os
import random


def _do_stupid_movie_password_animation( password, digits_solved ):
	'''
	Useless Hollywood style password digit spinning animation to run during decryption.
	This was added because the Day 5, puzzle 2 instructions allude to one.
	It is not curretnly called in find_password() because it slows down decryption MASSIVELY.
	'''

	pwd = copy.copy( password )
	for i in range( len( pwd ) - digits_solved ):
		char = ''
		while not char:
			val = random.randint( 48, 102)
			if not 58 <= val <= 96:
				char = chr( val )

		valid_idx = False
		idx = -1
		while not valid_idx:
			idx = random.randint(0, 7)
			if not pwd[ idx ]:
				valid_idx = True
		
		pwd[ idx ] = char

	pwd = ''.join( pwd )
	os.system( 'cls' )
	print( pwd )


def find_password( door_id ):
	'''
	'''

	password = [ '', '', '', '', '', '', '', '' ]
	incrementor = 0
	
	for _i in range( 8 ):
		char = ''
		while not char:
			#_do_stupid_movie_password_animation( password, _i )

			input = door_id + str( incrementor )
			m = hashlib.md5( )
			m.update( input.encode( 'utf-8' ) )
			hash = m.hexdigest( )

			if hash.startswith( '00000' ):
				loc = hash[ 5 ]
				char = hash[ 6 ]
				if loc.isdigit( ):
					loc = int( loc )
					if 0 <= loc <= ( len( password ) - 1 ) and not password[ loc ]:
						password[ loc ] = char	
					else:
						char = ''
				else:
					char = ''
			
			incrementor += 1

	password = ''.join( password )
	return password


if __name__ == '__main__':
	password = find_password( 'cxdnnyjw' )
	print( 'The door password is {0}'.format( password ) )