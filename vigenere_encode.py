import sys
from ciphers import arr_to_str, str_to_arr, vigenere_encode

v = sys.stdin.read()
i = v.index('\n')
key = str_to_arr(v[0:i])
message = str_to_arr(v[i+1:-1])

print arr_to_str(vigenere_encode(message, key))
