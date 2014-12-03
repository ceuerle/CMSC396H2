# Input: Text
# Output: Most probable vigenere-decoded message of text, where key length is unknown

import sys
from ciphers import str_to_arr, arr_to_str, encode, vigenere_decode

v = sys.stdin.read()
i = v.index('\n')
message = str_to_arr(v[i+1:-1])

m = vigenere_generic_decode(message)
# Grab key length from mapping
n = len(m[0])
print arr_to_str(encode(message, n, m))
