class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1={}
        word2={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in word1:
                word1[i]+=1
            else:
                word1[i]=1
        for i in t:
            if i in word2:
                word2[i]+=1
            else:
                word2[i]=1
        if word1 == word2:
            return True
        else:
            return False