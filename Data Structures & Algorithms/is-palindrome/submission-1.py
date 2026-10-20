class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.replace(" ","").lower().replace("?","")
        s="".join(filter(str.isalnum,s)).lower()#had to go to geeks for geeks to get this the
        # above one was mine i did not want to do character by character in for loop i wanted pythonic 
        return True if  s == s[::-1] else False
        