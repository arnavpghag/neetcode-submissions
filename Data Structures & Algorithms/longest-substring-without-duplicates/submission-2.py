class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longest=0
        main=set()
        for right in range(len(s)):
            
            while s[right] in main:
                main.remove(s[left])
                left+=1
                
            
            main.add(s[right])
            longest=max(longest,right-left+1)
        return longest
        # s="abcabcbb"                      set=[a,b,c]              longest=3