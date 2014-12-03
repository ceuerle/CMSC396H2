# Input: A generic, single substitution encoded text
# Output: Most probable single substitution decoded text

import sys
from ciphers import arr_to_str, str_to_arr, encode, generic_decode

message = str_to_arr(sys.stdin.read()[:-1])

print arr_to_str(encode(message, 1, generic_decode(message)))
