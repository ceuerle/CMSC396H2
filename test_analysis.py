# Takes a directory of decoded files and analyses them compared to original

inpath = './tests/decodes/'
srcpath = './tests/texts/'
outpath = './analysis.txt'

fout = open(outpath, 'w+')

fout.write('File Name\tCorrectness (%)\n')

from os import listdir

fs = listdir(inpath)

for fn in fs:
	f = open(inpath+fn)
	decoded = f.read()
	f.close()

	name = fn[:fn.find('_')]
	f = open(srcpath+name)
	src = f.read()
	f.close()

	correct = 0
	total = 0
	for i in range(len(decoded)):
		n = ord(decoded[i]) - ord('A')
		if n >= 0 and n < 26:
			total += 1
			if decoded[i] == src[i]:
				correct += 1
	correct = correct / (total + 0.0)
	fout.write(fn + '\t' + str(correct) + '\n')

fout.close()
