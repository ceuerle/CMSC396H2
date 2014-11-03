# Library of functions to perform encoding and decoding using substitution ciphers

# Convert a message from a string to an equivalent array
def str_to_arr(message):
	arr = []
	for c in message:
		arr.append(ord(c) - ord('A'))
	return arr

# Convert array back to string
def arr_to_str(message):
	s = ""
	for x in message:
		s += chr(x + ord('A'))
	return s

# Expected frequency values for each letter in a string
# Expected frequency of A is freq[0], etc.
freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
	0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
	0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
	0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

# Encode a message n characters at a time using the rules of a mapping table
# mapping is a mapping table from an unencoded letter to an encoded letter
  # Rows are the letters to encode (A=0, ..., Z=25)
  # Columns are the index of the letter mod n (for multi-letter encoding)
def encode(message, n, mapping):
	newmsg = []
	pos = 0
	for i in range(len(message)):
		if message[i] >= 0 and message[i] < 26:
			newmsg.append(mapping[message[i]][pos % n])
			pos += 1
		else:
			newmsg.append(message[i])
	return newmsg

# Decode a message using a set of mapping tables for possible encodes mappings[]
# Finds the mapping table that maximizes the dot product of expected frequencies and observed frequencies
# Returns a mapping for decoding
# Note: to get decoded string itself, just use encode function
def decode(message, n, mappings):
	letter_count = 0
	# Observed count of each letter at position (i mod n)
	g = [[0]*n for i in range(26)]
	for i in range(len(message)):
		if message[i] >= 0 and message[i] < 26:
			g[message[i]][letter_count % n] += 1
			letter_count += 1

	max_product = 0.0
	mapping = None
	for m in mappings:
		dotproduct = 0.0
		for i in range(26):
			observed_count = 0
			for j in range(n):
				observed_count += g[m[i][j]][j]
			dotproduct += (freq[i] * observed_count)/letter_count
		if dotproduct > max_product:
			max_product = dotproduct
			mapping = m

	# Compute inverse of the encoding to make it act as a decoder
	inversemap = [ [0]*n for i in range(26) ]
	for i in range(26):
		for j in range(n):
			inversemap[mapping[i][j]][j] = i
	return inversemap

# Shift cipher encode/decode implementation
def shift_encode(message, shift_amt):
	mapping = []
	for i in range(26):
		mapping.append([ (i + shift_amt) % 26 ])
	return encode(message, 1, mapping)

def shift_decode(message):
	mappings = []
	for i in range(26):
		mappings.append([[0] for x in range(26) ])
		for j in range(26):
			mappings[i][j][0] = (j + i) % 26

	return decode(message, 1, mappings)

# Affine cipher encode/decode implementation
# Encoded message is y = ax + b
def affine_encode(message, a, b):
	mapping = []
	for i in range(26):
		mapping.append([ (a*i + b) % 26 ])
	return encode(message, 1, mapping)

def affine_decode(message):
	a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
	mappings = []
	for i in range(len(a)):
		for b in range(26):
			mapping = [[0] for x in range(26) ]
			for j in range(26):
				mapping[j][0] = (a[i]*j + b) % 26
			mappings.append(mapping)

	return decode(message, 1, mappings)

# Vigenere cipher encode/decode implementation
def vigenere_encode(message, key):
	mapping = [ [0]*len(key) for i in range(26) ]
	for i in range(26):
		for j in range(len(key)):
			mapping[i][j] = (i + key[j]) % 26
	return encode(message, len(key), mapping)

# TODO: Vigenere cipher decode implementation, given n
def vigenere_decode(message, n):
	return 0

# TODO: Global decode implementation - decode using all possible mappings, given n
def global_decode(message, n):
	return 0
