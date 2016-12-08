# -*- coding: utf-8 -*- 
'''
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
'''

import os

class Character_Frequency( ):
	def __init__( self ):
		self._character_map = { }


	def add_character( char ):
		val = self._character_map.get( char, 0 ) + 1
		self._character_map[ char ] = val



def find_message( ):
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
		for line.rstrip( ) in file:
			for i in range( len( line ) ):
				cf_classes[ i ].add_character( puzzle_input_filepath[ i ] )




if __name__ == '__main__':
	find_message( )