class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.replace(" ","").lower().replace("?","")
        s="".join(filter(str.isalnum,s)).lower()
        print(s[::-1])
        return True if  s == s[::-1] else False
        