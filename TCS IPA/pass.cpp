#include<bits/stdc++.h>
using namespace std;

int MAX_CHAR = 26;

string encodeString(char str[], int m) {
	// hashEven stores the count of even indexed character
	// for each string hashOdd stores the count of odd
	// indexed characters for each string
	int hashEven[MAX_CHAR];
	int hashOdd[MAX_CHAR];

	memset(hashEven,0,sizeof(hashEven));
	memset(hashOdd,0,sizeof(hashOdd));
	// creating hash for each string
	for (int i = 0; i < m; i++) {
		char c = str[i];
		if ((i & 1) != 0) // If index of current character is odd
			hashOdd[c-'a']++;
		else
			hashEven[c-'a']++;

	}


	// For every character from 'a' to 'z', we store its
	// count at even position followed by a separator,
	// followed by count at odd position.
	string encoding = "";
	for (int i = 0; i < MAX_CHAR; i++) {
		encoding += (hashEven[i]);
		encoding += ('-');
		encoding += (hashOdd[i]);
		encoding += ('-');
	}
	return encoding;
}

// This function basically uses a hashing based set to
// store strings which are distinct according
// to criteria given in question.
int countDistinct(string input[], int n) {
	int countDist = 0; // Initialize result

	// Create an empty set and store all distinct
	// strings in it.
	set<string> s;
	for (int i = 0; i < n; i++) {
		// If this encoding appears first time, increment
		// count of distinct encodings.
		char char_array[input[i].length()];
		strcpy(char_array, input[i].c_str());
		if (s.find(encodeString(char_array, input[i].length())) == s.end()) {
			s.insert(encodeString(char_array,input[i].length()));
			countDist++;
		}
	}

	return countDist;
}

int main() {
	string input[] = {"abcd", "acbd", "adcb", "cdba",
			"bcda", "badc"};
	int n = sizeof(input)/sizeof(input[0]);

	cout << countDistinct(input, n) << "\n";
}

// This code is contributed by Harshit Sharma.
