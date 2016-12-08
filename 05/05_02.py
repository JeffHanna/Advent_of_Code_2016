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

import hashlib


def find_password( door_id ):
	'''
	'''

	password = [ '', '', '', '', '', '', '', '' ]
	incrementor = 0

	for _i in range( 8 ):
		char = ''
		while not char:
			m = hashlib.md5( )
		
			input = door_id + str( incrementor )
			m.update( input.encode( 'utf-8' ) )
			hash = m.hexdigest( )
		
			if hash.startswith( '00000' ):
				loc = hash[ 5 ]
				char = hash[ 6 ]
				if loc.isdigit( ):
					loc = int( loc ) - 1
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