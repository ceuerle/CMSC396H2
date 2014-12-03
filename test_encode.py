# Purpose: encodes a set of sample texts to use in analyzing decoding algorithms
# List of encodings produced per input file:
# Shift, affine, vigenere - key length known, vigenere - key length unknown, generic

inpath = './tests/texts/'
outpath = './tests/encodes/'

import ciphers
from os import listdir

fs = listdir(inpath)

for fn in fs:
	f = open(inpath+fn)
	text = f.read()
	f.close()

	text = ciphers.str_to_arr(text)
	outname = outpath+fn

	# Shift, n = 1
	encoded = ciphers.arr_to_str(ciphers.shift_encode(text, 1))
	fout = open(outname+'_shift_1.in', mode='w+')
	fout.write(encoded)
	fout.close()
	
	# Affine, a = 3, b = 4
	encoded = ciphers.arr_to_str(ciphers.affine_encode(text,3,4))
	fout = open(outname+'_affine_1.in', mode='w+')
	fout.write(encoded)
	fout.close()

	# Vigenere length known & unknown, key = apple
	key = ciphers.str_to_arr('apple')
	encoded = ciphers.arr_to_str(ciphers.vigenere_encode(text, key))
	fout = open(outname+'_vig5_1.in', mode='w+')
	fout.write(encoded)
	fout.close()
	
	fout = open(outname+'_viggen_1.in', mode='w+')
	fout.write(encoded)
	fout.close()

	# Generic - uses a randomly generated mapping
	m = [8,5,11,18,10,6,4,3,14,0,25,1,12,
			2,24,23,13,9,19,15,20,7,17,22,21,16]
	m = map(lambda x:[x], iter(m))
	encoded = ciphers.arr_to_str(ciphers.encode(text, 1, m))
	fout = open(outname+'_generic_1.in', mode='w+')
	fout.write(encoded)
	fout.close()

