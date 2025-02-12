class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        add = 0
        maxsum = -1
        dic={}
        add=0
        for i in nums:
            add=self.addDigit(i)
            if add in dic:
                maxsum=max(i+dic[add],maxsum)
            dic[add] = max(dic.get(add, 0), i)
        return maxsum    
            
    def addDigit(self,i):
        abc=0
        while i>0:
            abc+=i%10
            i=i//10
        return abc    
