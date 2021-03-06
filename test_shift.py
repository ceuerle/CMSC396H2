import sys
from ciphers import arr_to_str, str_to_arr, shift_encode, shift_decode, encode


v = sys.stdin.read().upper()
i = v.index('\n')
shift_amt = int(v[:i])
message = str_to_arr(v[i+1:-1])


encoded = arr_to_str(shift_encode(message, shift_amt))
print encoded
decoded = arr_to_str(encode(str_to_arr(encoded), 1, shift_decode(str_to_arr(encoded))))
message = arr_to_str(message)
if message == decoded:
    print "TRUE: 100% MATCH"
else:
    matches = 0
    total = 0
    for i in range(len(encoded)):
        if "ABCDEFGHIJKLMNOPQRSTUVWXYZ".count(message[i]) == 1:
            if message[i] == decoded[i]:
                matches += 1
            total += 1
    print "FAlSE: " + str(float(matches)/total * 100) + "% MATCH"