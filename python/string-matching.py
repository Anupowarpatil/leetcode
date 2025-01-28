class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        n = len(words)
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                abc = words[i] 
                xyz = words[j]   
                if abc in xyz:
                    if abc not in ans:
                        ans.append(abc)
        return ans

        
