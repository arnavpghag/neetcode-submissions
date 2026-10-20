class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","").lower()
        # s="".join(filter(str.isalnum,s)).lower()#had to go to geeks for geeks to get this the
        # above one was mine i did not want to do character by character in for loop i wanted pythonic 
        i=0
        j=len(s)-1

        while i<j:
            if s[i].isalnum()==False:
                i+=1
                continue
            elif s[j].isalnum()==False:
                j-=1
                continue
            elif s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
            

        