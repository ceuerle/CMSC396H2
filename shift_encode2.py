# Input: One line denoting a shift amount followed by text
# Output: text shift-encoded by shift amount

import sys
from ciphers import arr_to_str, str_to_arr, shift_encode

v = sys.stdin.read()
i = v.index('\n')
shift_amt = int(v[:i])
message = str_to_arr(v[i+1:-1])

print arr_to_str(shift_encode(message, shift_amt))
