class Solution:

    # whether s[i..j] inclusive is a palindrome
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        n = len(s)

        def dfs(i) -> None:
            if i == n:
                result.append(path[:])
                return
            
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return result
