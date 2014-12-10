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

# Decode a message using a set of encoding tables
# Finds the encoding that maximizes the dot product of expected frequencies and observed frequencies
# Returns a mapping for decoding, and the score of it
# Note: to get decoded string itself, just use encode function on the map
def decode(message, n, mappings):
	dotproducts = []
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
		dotproducts.append(dotproduct)
		if dotproduct > max_product:
			max_product = dotproduct
			mapping = m

	# Print out dotproducts for comparison
	dotproducts = sorted(iter(dotproducts))
	# for d in dotproducts:
	#	print d

	# Compute inverse of the encoding to make it act as a decoder
	inversemap = [ [0]*n for i in range(26) ]
	for i in range(26):
		for j in range(n):
			inversemap[mapping[i][j]][j] = i
	return (inversemap, max_product)

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

# Vigenere decode, known key length: just a group of shift decodes
def vigenere_decode(message, n):
	# Go through entire message
	# Construct a group of substrings of message
	  # corresponding to groups of same positions, mod n
	substrs = [[] for i in range(n)]
	pos = 0
	for i in range(len(message)):
		if message[i] >= 0 and message[i] < 26:
			substrs[pos].append(message[i])
			pos = (pos + 1) % n
	mapping = [[] for i in range(26)]
	for s in substrs:
		(m,score) = shift_decode(s)
		for i in range(26):
			mapping[i].append(m[i][0])
	return (mapping, 0)

# Generic vigenere decode : run Vignere on all key lengths
# Choose the key length resulting in a maximal dot product
def vigenere_generic_decode(message, key_limit=10):
	mapping = None
	max_product = -1
	for k in range(1, key_limit+1):
		m = vigenere_decode(message, k)[0]
		letter_count = 0
		# Observed count of each letter at position (i mod n)
		g = [0]*26
		for i in range(len(message)):
			if message[i] >= 0 and message[i] < 26:
				g[m[message[i]][letter_count % k]] += 1
				letter_count += 1
		dotproduct = 0.0
		for i in range(26):
			dotproduct += (freq[i] * g[i])/letter_count
		if dotproduct > max_product:
			max_product = dotproduct
			mapping = m
	return (mapping, max_product)

# Given a 26! random cipher, find it:
# Assign a mapping of most frequent observed letters to letters
# Try to perform swaps that increase the score
def generic_decode(message):
	letter_count = 0.0
	# g is a frequency table; second entry per row is a letter index
	g = []
	for i in range(26):
		g.append([0, i])
	for i in range(len(message)):
		if message[i] >= 0 and message[i] < 26:
			g[message[i]][0] += 1
			letter_count += 1
	f2 = []
	for i in range(26):
		f2.append([freq[i], i])
	# Sort both arrays
	f2.sort(key=lambda x:x[0])
	g2 = sorted(g, key=lambda x:x[0])

	# Construct initial mapping
	mapping = [0]*26
	for i in range(26):
		mapping[g2[i][1]] = [f2[i][1]]

	# Keep trying to swap 2 elements to improve dot product
	cont = 1
	while cont:
		cont = 0
		for i in range(26):
			for j in range(26):
				for k in range(26):
					combs = [(i, j, k), (i, k, j), (j, i, k), (j, k, i), (k, i, j), (k, j, i)]
					comb = max(combs, key=lambda x: g[x[0]][0]*freq[mapping[i][0]]+g[x[1]][0]*freq[mapping[j][0]]+g[x[2]][0]*freq[mapping[k][0]])
					m = map(lambda x: mapping[x][0], comb)
					if (i, j, k) != comb:
						cont = 1
					mapping[i][0] = m[0]
					mapping[j][0] = m[1]
					mapping[k][0] = m[2]
	return mapping
