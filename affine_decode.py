import sys
from ciphers import arr_to_str, str_to_arr, encode, affine_decode

message = str_to_arr(sys.stdin.read()[:-1])

print arr_to_str(encode(message, 1, affine_decode(message)))
