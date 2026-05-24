class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            count1={}
            count2={}
            for ch1 in s:
                if ch1 in count1:
                    count1[ch1]+=1
                else:
                    count1[ch1]=1
            for ch2 in t:
                if ch2 in count2:
                    count2[ch2]+=1
                else:
                    count2[ch2]=1
            if count1==count2:
                return True
            else:
                return False