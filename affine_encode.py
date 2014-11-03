import sys
from ciphers import arr_to_str, str_to_arr, affine_encode

v = sys.stdin.read()
i = v.index('\n')
[a,b] = v[:i].split(' ')
a = int(a)
b = int(b)
message = str_to_arr(v[i+1:-1])

print arr_to_str(affine_encode(message, a, b))
