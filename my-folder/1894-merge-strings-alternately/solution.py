class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        
        word = []

        for i in range(min_length):
            word.append(word1[i])
            word.append(word2[i])

        
        if len(word2) < len(word1):
            word.append(word1[min_length:])
        elif len(word2) > len(word1):
            word.append(word2[min_length:])

        
        return "".join(word)
