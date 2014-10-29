def dot_product(list1, list2):
    sum = 0
    for i in range(len(list1)):
        sum  = sum + list1[i] * list2[i]
    return sum


string = input("Enter the string to decode")
counts = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(alphabet)):
    counts[alphabet[i]] = 0

for c in string:
     counts[c] = counts[c] + 1