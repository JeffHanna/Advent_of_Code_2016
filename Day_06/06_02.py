# -*- coding: utf-8 -*- 
'''
--- Part Two ---
Of course, that would be the message - if you hadn't agreed to use a modified 
epetition code instead.

In this modified code, the sender instead transmits what looks like random data, 
but for each character, the character they actually want to send is slightly 
less likely than the others. Even after signal-jamming noise, you can look at 
the letter distributions in each column and choose the least common letter to 
reconstruct the original message.

In the above example, the least common character in the first column is a; in 
the second, d, and so on. Repeating this process for the remaining characters 
produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what 
is the original message that Santa is trying to send?

PERSONAL NOTES:
'''

import os

class Character_Frequency( ):
	'''
	'''

	def __init__( self ):
		self._character_frequency_map = { }
		self._lowest_frequency_character = ''


	@property
	def lowest_frequency_character( self ):
		'''
		'''

		if not self._lowest_frequency_character:
			frequency = 999
			for char in self._character_frequency_map.keys( ):
				val = self._character_frequency_map.get( char, 0 )
				if val < frequency:
					frequency = val
					self._lowest_frequency_character = char

		return self._lowest_frequency_character
	
	
	def add_character( self, char ):
		'''
		'''

		val = self._character_frequency_map.get( char, 0 ) + 1
		self._character_frequency_map[ char ] = val 
		

																  
def find_message( ):
	'''
	'''

	CF_0 = Character_Frequency( )
	CF_1 = Character_Frequency( )
	CF_2 = Character_Frequency( )
	CF_3 = Character_Frequency( )
	CF_4 = Character_Frequency( )
	CF_5 = Character_Frequency( )
	CF_6 = Character_Frequency( )
	CF_7 = Character_Frequency( )	

	cf_classes = [ CF_0, CF_1, CF_2, CF_3, CF_4, CF_5, CF_6, CF_7 ]

	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'06_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:
			line = line.rstrip( )
			for i in range( len( line ) ):
				cf_classes[ i ].add_character( line[ i ] )

	
	message = ''
	for cf_c in cf_classes:
		message += cf_c.lowest_frequency_character

	return message





if __name__ == '__main__':
	message = find_message( )
	print 'The message from Santa is, "{0}".'.format( message )
