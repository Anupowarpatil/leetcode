class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowel = {"a", "e", "i", "o", "u"}
        
        
        n = len(words)
        prefix = [0] * (n + 1)
        for i in range(n):
            if words[i][0] in vowel and words[i][-1] in vowel:  
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        ansr = []
        for li, ri in queries: 
            ansr.append(prefix[ri + 1] - prefix[li])  
        
        return ansr
