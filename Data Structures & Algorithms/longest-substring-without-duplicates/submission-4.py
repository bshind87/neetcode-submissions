class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l, r = 0, 0
        n = len(s)
        if n == 0: return 0
        maxlen = 1
        visited = [s[l]]

        while r < n-1:
            r += 1
            if s[r] not in visited:
                visited.append(s[r])
            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
                visited.append(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen
                

        