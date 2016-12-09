# -*- coding: utf-8 -*- 
"""
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
The same as Day 06, puzzle 1 except the Character_Frequency classes need to
return the lowest used character.
"""

import os

class Character_Frequency( ):
	"""
	Holds all of the characters for a given column of each row
	of the input data. The frequency of each added character is held in
	a dictionary of { char : frequency } pairs. The class can be queried
	to return the lowest used character in the map.
	
	**Arguments:**
	
		None
	
	**Keyword Arguments:**
	
		None 	
	"""

	def __init__( self ):
		self._character_frequency_map = { }
		self._lowest_frequency_character = ''


	@property
	def lowest_frequency_character( self ):
		"""
		Public property to return self._lowest_frequency_character.
		If self._lowest_frequency_character is null when this property
		is first called then the entire self._character_frequency_map is
		processed to find the character with a frequency lower than all of the
		others. That character is assigned to self._lowest_frequency_character
		and returned.
	
		**Arguments:**
	
			None
	
		**Keyword Arguments:**
	
			None
	
		**Returns:**
	
			`arg_type` If any, enter a description for the return value here.
		"""

		if not self._lowest_frequency_character:
			frequency = 999
			for char in self._character_frequency_map.keys( ):
				val = self._character_frequency_map.get( char, 0 )
				if val < frequency:
					frequency = val
					self._lowest_frequency_character = char

		return self._lowest_frequency_character
	
	
	def add_character( self, char ):
		"""
		Adds a character to self._character_frequency_map with a frequency value
		of 1. If the character already exists in the map then its frequency value
		is increased by 1
	
		**Arguments:**
	
			:``char``:	`str` The character to add to the frequency map.
	
		**Keyword Arguments:**
	
			None
	
		**Returns:**
	
			None
		"""

		val = self._character_frequency_map.get( char, 0 ) + 1
		self._character_frequency_map[ char ] = val 
		

																  
def find_message( ):
	"""
	Reads lines of strings from the input file. For each character in the string
	a Character_Frequency class is instantiated. If the class already exists
	the character is added to the class's frequency map. When the entire 
	input file has been parsed each of the classes is queried in order to 
	retrieve the lowest used character. Those characters comprise the message.
	
	**Arguments:**
	
		None
	
	**Keyword Arguments:**
	
		None
	
	**Returns:**
	
		`str` The message
	"""

	cf_classes = [ ]
	puzzle_input_filepath = os.path.abspath( 
									os.path.join( os.getcwd( ),'06_puzzle_input.txt' ) )

	with open( puzzle_input_filepath ) as file:
		for line in file:
			line = line.rstrip( )
			if not cf_classes:
				for i in range( len( line ) ):
					cf_classes.append( Character_Frequency( ) )

			for i in range( len( line ) ):
				cf_classes[ i ].add_character( line[ i ] )

	
	message = ''
	for cf_c in cf_classes:
		message += cf_c.lowest_frequency_character

	return message
						  

						  
if __name__ == '__main__':
	message = find_message( )
	print( 'The message from Santa is, "{0}".'.format( message ) )
