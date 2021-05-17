"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
"""


class Solution:
    def removeVowels(self, S: str) -> str:
        result = []
        for i in range(len(S)):
            if S[i] not in 'aeiou':
                result.append(S[i])
        return ''.join(result)
