class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for i in strs:
            freq=[0]*26

            for char in i:
                position=ord(char)-ord('a')
                freq[position]+=1
            if tuple(freq) in anagram:
                anagram[tuple(freq)].append(i)
            else:
                anagram[tuple(freq)]=[i]
        return list(anagram.values())
            