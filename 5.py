class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Dumb Brute Force O(n^3)
        # right = len(s)
        # while right > 0:
        #     for i in range(len(s)-right+1):
        #         window = s[i:right+i]
        #         if window == window[::-1]:
        #             return window
        #     right -= 1
        # Dynamic Programming O(n^2)
        longest = ""
        palindromes = [[False]*len(s) for _ in s]
        for i in range(len(s)):
            palindromes[i][i] = True
            longest = s[i]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                palindromes[i][i+1] = True
                longest = s[i:i+2]

        for window_size in range(3, len(s)+1):
            for window in range(len(s)-window_size+1):
                left, right = window, window+window_size-1
                if s[left] == s[right] and palindromes[left+1][right-1]:
                    palindromes[left][right] = True
                    longest = s[left:right+1]
        
        return longest

        

        # babadcbbd