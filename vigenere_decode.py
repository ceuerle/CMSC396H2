# Input: 1 line specifying key length followed by text
# Output: Most probable vigenere-decoded message of text, where key is length n

import sys
from ciphers import str_to_arr, arr_to_str, encode, vigenere_decode

v = sys.stdin.read()
i = v.index('\n')
n = int(v[:i])
message = str_to_arr(v[i+1:-1])

print arr_to_str(encode(message, n, vigenere_decode(message, n)))
