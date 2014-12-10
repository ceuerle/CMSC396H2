CMSC396H Final Programming Project: Fundamentals of Cryptographic Ciphers
Group Member Names: Chris Euerle, Eric Harrison, Claire Pitman, Kenneth Wayman

Description:
Using the cipher encoding/decoding functions and a series of test scripts, our programming project as a whole measures the correctness of four cipher decoding algorithms (shift, affine, Vigenere, generic).

Components of Programming Project:
ciphers.py:
	Contains functions to encode and decode strings
	Supports shift encode/decode, affine encode/decode, Vigenere encode/decode, and also generic encode/decode (any mapping of one alphabet to another)

test_encode.py:
	Generates files encoded by different ciphers
	These files are then used in analyzing the accuracy of decoding algorithms

test_decode.py:
	Once the encoded files have been generated, this script then attempts to decode all the files back to their original non-encoded version.

test_analysis.py:
	After generating all decoded files using test_decode.py, this script measures the correctness (percentage of all letters correctly decoded) of each decoded file compared to the originals, and writes the results to analysis.txt.

analysis.txt:
	This file is the result of running all of the test scripts in order (test_encode.py, test_decode.py, test_analysis.py), and provides us with the final data for our project. It measures the correctness of each decoded file compared to its original.

tests/texts/:
	Directory containing all of the source texts to be used during encoding. Texts are a mix of Wikipedia articles, IETF RFC Pages, and random gibberish.

tests/encodes/:
	Directory containing all of the encoded files during testing.

tests/decodes/:
	Directory containing all of the decoded files during testing.
