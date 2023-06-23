# Python3 program to count distinct strings with
# even odd swapping allowed.
MAX_CHAR = 26

# Returns encoding of string that can be used
# for hashing. The idea is to return same encoding
# for strings which can become same after swapping
# a even positioned character with other even characters
# OR swapping an odd character with other odd characters.
def encodeString(string):

	# hashEven stores the count of even indexed character
	# for each string hashOdd stores the count of odd
	# indexed characters for each string
	hashEven = [0] * MAX_CHAR
	hashOdd = [0] * MAX_CHAR

	# creating hash for each string
	for i in range(len(string)):
		c = string[i]
		if i & 1: # If index of current character is odd
			hashOdd[ord(c) - ord('a')] += 1
		else:
			hashEven[ord(c) - ord('a')] += 1

	# For every character from 'a' to 'z', we store its
	# count at even position followed by a separator,
	# followed by count at odd position.
	encoding = ""
	for i in range(MAX_CHAR):
		encoding += str(hashEven[i])
		encoding += str('-')
		encoding += str(hashOdd[i])
		encoding += str('-')

	return encoding

# This function basically uses a hashing based set to
# store strings which are distinct according
# to criteria given in question.
def countDistinct(input, n):
	countDist = 0 # Initialize result

	# Create an empty set and store all distinct
	# strings in it.
	s = set()
	for i in range(n):

		# If this encoding appears first time, increment
		# count of distinct encodings.
		if encodeString(input[i]) not in s:
			s.add(encodeString(input[i]))
			countDist += 1

	return countDist

# Driver Code
if __name__ == "__main__":
	input = ["abcd", "acbd", "adcb",
			"cdba", "bcda", "badc"]
	n = len(input)
	print(countDistinct(input, n))

# This code is contributed by
# sanjeev2552
