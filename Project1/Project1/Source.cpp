#include<string>
#include <iostream>

using namespace std;

class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		char* alphabeta[26];
		int len = s.length();
		int result=0;
		printf("%d", len);
		for (int i = 0; i <= len; i++) {
			string sub = s.substr(i, len);
			int sublen = sub.length();
			for (int j = 0; j <= sublen;j++ ) {
				char cur = sub[j];
				alphabeta[cur] += 1;
				
			}
		}
		return result;
	}
};


int main() {
	string s = "pwwkew";
	Solution solu;
	int res = solu.lengthOfLongestSubstring(s);
}