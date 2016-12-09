# -*- coding: utf-8 -*- 
"""
--- Day 6: Signals and Noise ---
Something is jamming your communications with Santa. Fortunately, your signal is 
only partially jammed, and protocol in situations like this is to switch to a 
simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the 
repeating message signal (your puzzle input), but the data seems quite 
corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each 
position. For example, suppose you had recorded the following messages:
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar

The most common character in the first column is e; in the second, a; in the 
third, s, and so on. Combining these characters returns the error-corrected 
message, easter.

Given the recording in your puzzle input, what is the error-corrected version of 
the message being sent?

PERSONAL_NOTES:
* Make a bin (list? class?) for each column. Read each line and sort each 
  character to the correct bin. Then, query each bin for the highest 
  value character.
* All rows contain exactly 8 characters.
"""

import os

class Character_Frequency( ):
	"""
	Holds all of the characters for a given column of each row
	of the input data. The frequency of each added character is held in
	a dictionary of { char : frequency } pairs. The class can be queried
	to return the highest used character in the map.
	
	**Arguments:**
	
		None
	
	**Keyword Arguments:**
	
		None	
	"""

	def __init__( self ):
		self._character_frequency_map = { }
		self._highest_frequency_character = ''


	@property
	def highest_frequency_character( self ):
		"""
		Public property to return self._highest_frequency_character.
		If self._highest_frequency_character is null when this property
		is first called then the entire self._character_frequency_map is
		processed to find the character with a frequency higher than all of the
		others. That character is assigned to self._highest_frequency_character
		and returned.
	
		**Arguments:**
	
			None
	
		**Keyword Arguments:**
	
			None
	
		**Returns:**
	
			`arg_type` If any, enter a description for the return value here.
		"""

		if not self._highest_frequency_character:
			frequency = 0
			for char in self._character_frequency_map.keys( ):
				val = self._character_frequency_map.get( char, 0 )
				if val > frequency:
					frequency = val
					self._highest_frequency_character = char

		return self._highest_frequency_character
	
	
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
	retrieve the highest used character. Those characters comprise the message.
	
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
		message += cf_c.highest_frequency_character

	return message
									
									

if __name__ == '__main__':
	message = find_message( )
	print( 'The message from Santa is, "{0}".'.format( message ) )