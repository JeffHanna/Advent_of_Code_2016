# -*- coding: utf-8 -*-
"""
--- Day 14: One-Time Pad ---
In order to communicate securely with Santa while you're on this mission, you've 
been using a one-time pad that you generate using a pre-agreed algorithm. 
Unfortunately, you've run out of keys in your one-time pad, and so you need to 
generate some more.

To generate keys, you first get a stream of random data by taking the MD5 of a 
pre-arranged salt (your puzzle input) and an increasing integer index (starting 
with 0, and represented in decimal); the resulting MD5 hash should be 
represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for your 
one-time pad. A hash is a key only if:
- It contains three of the same character in a row, like 777. Only consider the 
  first such triplet in a hash.
- One of the next 1000 hashes in the stream contains that same character five 
  times in a row, like 77777.

Considering future hashes for five-of-a-kind sequences does not cause those 
hashes to be skipped; instead, regardless of whether the current hash is a key, 
always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:
- The first index which produces a triple is 18, because the MD5 hash of abc18 
  contains ...cc38887a5.... However, index 18 does not count as a key for your 
  one-time pad, because none of the next thousand hashes (index 19 through index 
  1018) contain 88888.
- The next index which produces a triple is 39; the hash of abc39 contains eee. 
  It is also the first key: one of the next thousand hashes (the one at index 
  816) contains eeeee.
- None of the next six triples are keys, but the one after that, at index 92, 
  is: it contains 999 and index 200 contains 99999.
- Eventually, index 22728 meets all of the criteria to generate the 64th key.

So, using our example salt of abc, index 22728 produces the 64th key.

Given the actual salt in your puzzle input, what index produces your 64th 
one-time pad key?

Your puzzle input is ngcjuoqr.

PERSONAL NOTES:
* re, hashlib, and a list of previously generated hashes is all that
  is needed.
"""

import hashlib
import re

triplet = re.compile( r'(.)\1{2}' )
hashes = [ ]
valid_hash_count = 0
i = 0

while valid_hash_count < 64:
	try:
		hash = hashes[ i ]
	except IndexError:
		m = hashlib.md5( )					
		input ='abc{0}'.format( i )  	
		#input = 'ngcjuoqr{0}'.format( i )
		m.update( input.encode( 'utf-8' ) )
		hash = m.hexdigest( ).lower( ) 
		hashes.append( hash )
	
	# validate
	m = triplet.search( hash )
	if m:
		# triplet found. Now check for a quintuple in the next 1000 hashes.
		# There's no reason to not generate all 1000, as they will be used anyway.
		char = m.group( )[ 0 ]
		quintuple = re.compile( r'(' + char + ')\1{4}' )
		for x in range( i + 1, i + 1001 ):
			try:
				hash = hashes[ x ]
			except IndexError:
				m = hashlib.md5( )
				input ='abc{0}'.format( i )  	
				#input = 'ngcjuoqr{0}'.format( i )
				m.update( input.encode( 'utf-8' ) )
				hash = m.hexdigest( ).lower( )
				hashes.append( hash )

				# validate
				m = quintuple.search( hash )
				if m:
					valid_hash_count += 1
	
	i += 1


if __name__ == '__main__':
	pass