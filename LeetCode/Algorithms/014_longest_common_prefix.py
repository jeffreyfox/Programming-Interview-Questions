class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        first = strs[0]
        def is_same(i: int) -> bool:
            for s in strs: # avoids strs[1:] repeated slicing
                if i >= len(s) or s[i] != first[i]:
                    return False
            return True

        end = 0
        while end < len(first):
            if not is_same(end):
                break
            end += 1
        
        return first[:end]
