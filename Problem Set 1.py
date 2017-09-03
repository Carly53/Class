# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:23:10 2017

Answers to Problem set 1

@author: Carly

"""






s = 'azcbobbobegghakl'

# Problem 1

vowel = 0
for letter in s:
    if (letter=='a') or (letter=='e') or (letter=='i') or (letter=='o') or (letter=='u'):
        vowel = vowel + 1
print(vowel)



# Problem 2

count = 0
for x in range(len(s)):
    if s[x:x+3] == 'bob':
        count = count +1
print(count)



# Problem 3

longest = ''
s = s + '1'
for letter in range(len(s[:-1])):
    x = letter
    substring = s[x]
    while s[x] <= s[x+1]:
        x = x + 1
        substring = substring + s[x]
    if len(substring) >= len(longest):
        longest = substring

print(longest)