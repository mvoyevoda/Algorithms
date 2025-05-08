class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        freqs = {}
        for string in strs:
            freq = [0]*26
            for letter in string:
                freq[ord(letter) - ord("a")] += 1
            key = tuple(freq)
            if key in freqs:
                freqs[key].append(string)
            else:
                freqs[key] = [string]

        return [[anagram for anagram in group] for group in freqs.values()]