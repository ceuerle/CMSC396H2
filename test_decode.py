# Purpose: decodes different encoded texts according to encoding rule

inpath = './tests/encodes/'
outpath = './tests/decodes/'

import ciphers
from os import listdir

fs = listdir(inpath)

for fn in fs:
	print 'Decoding ', fn
	f = open(inpath+fn)
	text = f.read()
	f.close()

	text = ciphers.str_to_arr(text)
	i = fn.find('_')
	j = fn.rfind('_')
	rule = fn[i+1:j]
	decoded = []
	if rule == 'shift':
		decoded = ciphers.shift_decode(text)
	elif rule == 'affine':
		decoded = ciphers.affine_decode(text)
	elif rule[0:3] == 'vig' and rule[3] != 'g':
		n = int(rule[3:j])
		decoded = ciphers.vigenere_decode(text, n)
	elif rule == 'viggen':
		decoded = ciphers.vigenere_generic_decode(text)
	elif rule == 'generic':
		decoded = ciphers.generic_decode(text)
	else:
		continue # file name not supported
	message = ciphers.arr_to_str(ciphers.encode(text, len(decoded[0]), decoded))
	fout = open(outpath+fn[:fn.rfind('.')]+'.out', 'w+')
	fout.write(message)
	fout.close()
