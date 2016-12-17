# -*- coding: utf-8 -*-
"""
--- Part Two ---
Of course, in order to make this process even more secure, you've also 
implemented key stretching.

Key stretching forces attackers to spend more time generating hashes. 
Unfortunately, it forces everyone else to spend more time, too.

To implement key stretching, whenever you generate a hash, before you use it, 
you first find the MD5 hash of that hash, then the MD5 hash of that hash, and so 
on, a total of 2016 additional hashings. Always use lowercase hexadecimal 
representations of hashes.

For example, to find the stretched hash for index 0 and salt abc:
- Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.					 
- Then, find the MD5 hash of that hash: eec80a0c92dc8a0777c619d9bb51e910.
- Then, find the MD5 hash of that hash: 16062ce768787384c81fe17a7a60c7e3.	 
- ...repeat many times...																	 
- Then, find the MD5 hash of that hash: a107ff634856bb300138cac6568c0f24.

So, the stretched hash for index 0 in this situation is a107ff.... 
In the end, you find the original hash (one use of MD5), then find the 
hash-of-the-previous-hash 2016 times, for a total of 2017 uses of MD5.

The rest of the process remains the same, but now the keys are 
entirely different. 
Again for salt abc:
- The first triple (222, at index 5) has no matching 22222 in the next 
  thousand hashes.
- The second triple (eee, at index 10) hash a matching eeeee at index 89, and so 
  it is the first key.
- Eventually, index 22551 produces the 64th key (triple fff with matching fffff 
  at index 22859.

Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key 
stretching, what index now produces your 64th one-time pad key?

Your puzzle input is still ngcjuoqr.

PERSONAL NOTES:

"""

import hashlib
import re


def generate_hash( input ):
	"""
	"""
	m = hashlib.md5( )	
	m.update( input.encode( 'utf-8' ) )
	hash = m.hexdigest( ).lower( )
	return hash	


def find_64th_hash_index( ):
	"""
	"""

	triplet = re.compile( r'(.)\1{2}' )
	hashes = [ ]
	valid_hash_count = 0

	i = 0			 
	while valid_hash_count < 64:
		try:
			hash = hashes[ i ]
		except IndexError:
			hash = generate_hash( 'ngcjuoqr' + str( i ) ) # )
			for _ in range( 2016 ):
				hash = generate_hash( hash )
			hashes.append( hash )
	
		# validate
		m = triplet.search( hash )
		if m:
			# triplet found. Now check for a quintuple in the next 1000 hashes.
			# There's no reason to not generate all 1000, as they will be used anyway.
			char = m.group( )[ 0 ]
			re_str = r'(' + char + r')\1{4}'
			quintuple = re.compile( re_str )
		
			x = i + 1
			while x < i + 1000:		
				try:
					hash = hashes[ x ]
				except IndexError:
					hash = generate_hash( 'ngcjuoqr' + str( x ) )
					for _ in range( 2016 ):
						hash = generate_hash( hash )
					hashes.append( hash )

				# validate
				m = quintuple.search( hash )
				if m:
					valid_hash_count += 1
					#print( i, char, x, hash )
					x = i + 1000
				x += 1					
		i += 1

	return( i - 1 ) 



if __name__ == '__main__':
	idx = find_64th_hash_index( )
	print( 'The index of the 64th valid hash is {0}.'.format( idx ) )
