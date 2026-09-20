class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Your logic goes here!def longestCommonPrefix(strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Sort the array alphabetically
        strs.sort()
        
        # Compare the first and last strings in the sorted array
        first = strs[0]
        last = strs[-1]
        
        prefix_len = 0
        while prefix_len < len(first) and prefix_len < len(last) and first[prefix_len] == last[prefix_len]:
            prefix_len += 1
            
        return first[:prefix_len]