'''
Solving the hackerrank Game Of Thrones - I puzzle

https://www.hackerrank.com/challenges/game-of-thrones

----------------------

Problem Statement

Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

<picture of an old-school door in an arch-way>

But, to lock the door he needs a key that is an anagram of a certain palindrome string.

The king has a string composed of lowercase English letters. Help him figure out whether any anagram of the string can be a palindrome or not.

Input Format 
A single line which contains the input string.

Constraints 
1<= length of string <=105 
Each character of the string is a lowercase English letter.

Output Format 
A single line which contains YES or NO in uppercase.
----------------------

Alternatively, find if any more that one char has more than one odd numbers of occurances 

I looked at 4 or 5 solutions, and couldn't find a prettier one than mine.
Which is nice.

Created on 31 Dec 2015

@author: chris
'''
inputString = raw_input().strip()
uniqueChars = set(inputString)

numOddCountChars = 0
output = 'YES'
for char in uniqueChars:
    numOddCountChars += inputString.count(char)%2
    if numOddCountChars > 1:
        output = 'NO'
        break

print output


