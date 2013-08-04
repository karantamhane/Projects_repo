# Facebook Hacker Cup qualification
# Problem 1: Beuatiful Strings

# When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on.
# So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.
# Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it.
# The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. 
# Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter.
# (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)
# You're a student writing a report on the youth of this famous hacker. 
# You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?

# Input
# The input file consists of a single integer m followed by m lines.
# Output
# Your output should consist of, for each test case, a line containing the string "Case #x: y" 
# where x is the case number (with 1 being the first case in the input file, 2 being the second, etc.) 
# and y is the maximum beauty for that test case.
# Constraints
# 5 ≤ m ≤ 50
# 2 ≤ length of s ≤ 500

#Solution:

#counter to keep track of line no
#no of distinct letters in string
#sort by max occurence of letter
#assign values to letters in desc order of occurences
#calculate value

##Output Format = Case #1: 152

class letterObj:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

def beautifulStrings(filename):
    contents = open(filename, 'r')
    m = int(contents.readline())
    lines = contents.readlines()
    output = []
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for line in lines:
        letter_dict = {}
        for letter in line:
            if letter.lower() in letter_dict and letter in alphabet:
                letter_dict[letter.lower()] += 1
            elif letter.lower() in alphabet:
                letter_dict[letter.lower()] = 1
        #print line
        #print letter_dict
        keys = letter_dict.keys()
        values = letter_dict.values()
        obj_list = [letterObj(keys[i], values[i]) for i in range(len(keys))]
        obj_list = sorted(obj_list, key=lambda letterObj:letterObj.value)
        obj_list.reverse()
        value = 0
        max_letter_val = 26
        for obj in obj_list:
            value += obj.value*max_letter_val
            #print str(obj.value)+'*'+str(max_letter_val)
            max_letter_val -= 1
        output.append('Case #'+str(lines.index(line)+1)+': '+str(value))
    for case in output:
        print case

