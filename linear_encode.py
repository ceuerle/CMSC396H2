#gets a string, removes all non alphabetic characters, breaks into group of five, capitilizes, linearly encodes, then prints. 
a = int(input("Enter the a value (must be rel prime to 26 aka odd number less than 26 thats not 13): "))
b = int(input("Enter the b value [0-25]: "))
string = input("Enter the string: ")
string = string.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dict = {}
for i in range(26):
    alphabet_dict[alphabet[i]] = i

new_string = ""
for i in range(len(string)):
    if alphabet.count(string[i]) == 1:
        new_string += string[i]

string = new_string
new_string = ""
counter = 0

for i in range(len(string)):
    new_string += alphabet[(alphabet_dict[string[i]] * a + b) % 26]
    counter = counter + 1
    if counter == 5:
        counter = 0
        new_string += " "

print(new_string)