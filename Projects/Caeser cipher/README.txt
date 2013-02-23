Caeser Cipher
-------------
Author: Karan Tamhane
Course: Introduction to Computer Science and Programming
School: MITx (edX)
Problem Set: 5

Summary:
	Encrypts and decrypts file using ceaser cipher. Caeser cipher substitutes letters in input text such that each subsitute letter is a fixed number of letters ahead in the alphabet than the original letter. E.g. if shift = 4, a -> e, b -> f, c -> g and so on.

Source code: caeser_cipher.py

Files:

	"words.txt" - loads valid wordlist.

	"story.txt" - example input file(encrypted) for decryption.

Modules imported:
	random, string

Usage:
	
	Program must be run in a python shell.
	
	Call applyShift(filename, shift) to encrypt file 'filename' by shifting each letter, 'shift' characters ahead in the alphabet.

	filename (string) => file to be encrypted. The file must contain only one string.
	shift (int) => number of letters to move ahead in the alphabet.

	Call decryptStory(filename) to decrypt the encrypted file 'filename'.

	filename (string) => file to be decrypted. The file must contain only one string.