import random

def	generate_key(len = 5):
	key = [chr(x + ord('A')) for x in list(range(ord('Z') - ord('A') + 1))]
	random.shuffle(key)
	return "".join(key[: len])

def encrypt(plaintext, key):
	ciphertext = ""
	key = key.upper()
	i = 0
	for c in plaintext.upper():
		if c.isalpha():
			char = ((ord(key[i]) - ord('A') + ord(c) - ord('A')) % 26) + ord('A')
			ciphertext += chr(char)
			i += 1
		else:
			ciphertext += c
		if i == len(key):
			i = 0
	return ciphertext

def decrypt(ciphertext, key):
	plaintext = ""
	key = key.upper()
	i = 0
	for c in ciphertext:
		if c.isalpha():
			char = ((ord(c) - ord('A') - ord(key[i]) - ord('A')) % 26) + ord('A')
			plaintext += chr(char)
			i += 1
		else:
			plaintext += c
		if i == len(key):
			i = 0
	return plaintext
