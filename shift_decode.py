# Input: Encoded text
# Output: Most probable shift-decoded message of text

import sys
from ciphers import str_to_arr, arr_to_str, encode, shift_decode

message = str_to_arr(sys.stdin.read()[:-1])

print arr_to_str(encode(message, 1, shift_decode(message)))
